#!/usr/bin/env python3

"""
Davis–Putnam–Logemann–Loveland (DPLL) algorithm is a complete, backtracking-based
search algorithm for deciding the satisfiability of propositional logic formulae in
conjunctive normal form, i.e, for solving the Conjunctive Normal Form SATisfiability
(CNF-SAT) problem.

For more information about the algorithm: https://en.wikipedia.org/wiki/DPLL_algorithm
"""
from __future__ import annotations

import random
from collections.abc import Iterable


from typing import List, Tuple


from typing import List, Dict, Tuple


from typing import List, Dict, Tuple, Union


class Clause:
    """
    A clause represented in Conjunctive Normal Form.
    A clause is a set of literals, either complemented or otherwise.
    For example:
        {A1, A2, A3'} is the clause (A1 v A2 v A3')
        {A5', A2', A1} is the clause (A5' v A2' v A1)

    Create model
    >>> clause = Clause(["A1", "A2'", "A3"])
    >>> clause.evaluate({"A1": True})
    True
    """

    def __init__(self, literals: list[str]) -> None:
        """
        Represent the literals and an assignment in a clause."
        """
        # Assign all literals to None initially
        self.literals: dict[str, bool | None] = {literal: None for literal in literals}

    def __str__(self) -> str:
        """
        To print a clause as in Conjunctive Normal Form.
        >>> str(Clause(["A1", "A2'", "A3"]))
        "{A1 , A2' , A3}"
        """
        return "{" + " , ".join(self.literals) + "}"

    def __len__(self) -> int:
        """
        To print a clause as in Conjunctive Normal Form.
        >>> len(Clause([]))
        0
        >>> len(Clause(["A1", "A2'", "A3"]))
        3
        """
        return len(self.literals)

    def assign(self, model: dict[str, bool | None]) -> None:
        """
        Assign values to literals of the clause as given by model.
        """
        for literal in self.literals:
            symbol = literal[:2]
            if symbol in model:
                value = model[symbol]
            else:
                continue
            if value is not None:
                # Complement assignment if literal is in complemented form
                if literal.endswith("'"):
                    value = not value
            self.literals[literal] = value

    def evaluate(self, model: dict[str, bool | None]) -> bool | None:
        """
        Evaluates the clause with the assignments in model.
        This has the following steps:
        1. Return True if both a literal and its complement exist in the clause.
        2. Return True if a single literal has the assignment True.
        3. Return None(unable to complete evaluation) if a literal has no assignment.
        4. Compute disjunction of all values assigned in clause.
        """
        for literal in self.literals:
            symbol = literal.rstrip("'") if literal.endswith("'") else literal + "'"
            if symbol in self.literals:
                return True

        self.assign(model)
        for value in self.literals.values():
            if value in (True, None):
                return value
        return any(self.literals.values())


class Formula:
    """
    A formula represented in Conjunctive Normal Form.
    A formula is a set of clauses.
    For example,
        {{A1, A2, A3'}, {A5', A2', A1}} is ((A1 v A2 v A3') and (A5' v A2' v A1))
    """

    def __init__(self, clauses: Iterable[Clause]) -> None:
        """
        Represent the number of clauses and the clauses themselves.
        """
        self.clauses = list(clauses)

    def __str__(self) -> str:
        """
        To print a formula as in Conjunctive Normal Form.
        str(Formula([Clause(["A1", "A2'", "A3"]), Clause(["A5'", "A2'", "A1"])]))
        "{{A1 , A2' , A3} , {A5' , A2' , A1}}"
        """
        return "{" + " , ".join(str(clause) for clause in self.clauses) + "}"

def generate_clause() -> Clause:
    """
    Randomly generate a Clause instance.

    Procedure:
        Randomly select a quantity 'n', in range 1 to 5, of literals to be included in the clause.
        Randomly create 'n' literals, each consisting of a base name 'A' appended with a random number
        from 1 to 5. There's also a 50-50 chance that a literal may be complemented (represented by a trailing prime symbol).
        In the event of a literal duplication, disregard the duplication and continue until 'n' unique literals are created.

    Returns
    -------
    Clause
        A Clause object containing randomized literals.

    Examples
    --------
    >>> generate_clause()
    Clause(['A1', 'A3', 'A4', 'A2', 'A1'])
    """

    def _create_literal() -> str:
        base_var = "A" + str(random.randint(1, 5))
        return base_var + "'" if random.choice([True, False]) else base_var

    literals = set()
    while len(literals) < random.randint(1, 5):
        literals.add(_create_literal())

    return Clause(list(literals))


def generate_formula() -> Formula:
    """
    Randomly generate a formula.
    """
    clauses: set[Clause] = set()
    no_of_clauses = random.randint(1, 10)
    while len(clauses) < no_of_clauses:
        clauses.add(generate_clause())
    return Formula(clauses)


def generate_parameters(formula: Formula) -> Tuple[List[Clause], List[str]]:
    """
    Extract the clauses and symbols from a formula.

    Args:
        formula: A Formula object.

    Returns:
        A tuple, where the first element is a list of clauses in the formula,
        and the second element is a list of unique symbols in the formula.
    """
    clauses = formula.clauses
    symbols = list(
        set(
            symbol
            for clause in clauses
            for symbol in extract_symbols_from_clause(clause)
        )
    )
    return clauses, symbols


def find_unit_clauses(
    clauses: List[Clause], model: Dict[str, Union[bool, None]]
) -> Tuple[List[str], Dict[str, Union[bool, None]]]:
    """
    Identify unit clauses within the set of clauses under the current model.

    Args:
        clauses (List[Clause]): List of Clause objects.
        model (Dict[str, Union[bool, None]]): Current model containing symbol assignments.

    Returns:
        Tuple[List[str], Dict[str, Union[bool, None]]]: A tuple containing a list of identified unit clauses
        and a dictionary of these unit clauses along with their assigned values.
    """
    unit_symbols = []
    for clause in clauses:
        unit_symbol = get_unit_symbol_from_clause(clause)
        if unit_symbol is not None:
            unit_symbols.append(unit_symbol)

    assignment = assign_symbols(unit_symbols)
    unit_symbols = [
        symbol[:2] for symbol in unit_symbols
    ]  # Remove ' symbol for negation from symbol.

    return unit_symbols, assignment


def find_pure_symbols(
    clauses: List[Clause], symbols: List[str], model: Dict[str, bool | None]
) -> Tuple[List[str], Dict[str, bool | None]]:
    literals = gather_literals(clauses, model)
    pure_symbols = identify_pure_symbols(symbols, literals)

    assignment = {p: None for p in pure_symbols}

    for symbol in pure_symbols:
        if symbol in literals:
            assignment[symbol] = True

            assignment[symbol] = False

    return pure_symbols, assignment



def get_unit_symbol_from_clause(clause: Clause) -> str:
    """
    Get the unit symbol from a given clause if one exists.

    Args:
        clause (Clause): The given clause object.

    Returns:
        str: The unit symbol from a clause if it exists. Otherwise, return None.
    """
    if len(clause) == 1:
        return next(iter(clause.literals.keys()))

    f_count, n_count = 0, 0
    sym = None
    for literal, value in clause.literals.items():
        if value is False:
            f_count += 1
        elif value is None:
            sym = literal
            n_count += 1
    # If all literals except one are False, and if it is the only unassigned literal, it is the unit symbol.
    if f_count == len(clause) - 1 and n_count == 1:
        return sym

    return None


def assign_symbols(unit_symbols: List[str]) -> Dict[str, Union[bool, None]]:
    """
    Assign Truth value to the given symbols.

    Literal without negation gets True and with negation gets False.

    Args:
        unit_symbols (List[str]): List of unit symbols.

    Returns:
        Dict[str, Union[bool, None]]: Dictionary of symbols assigned their respective Truth values.
    """
    assignment: Dict[str, Union[bool, None]] = {}
    for symbol in unit_symbols:
        base_symbol = symbol[:2]
        assignment[base_symbol] = len(symbol) == 2
    return assignment

def extract_symbol_from_literal(literal: str) -> str:
    """
    Extract the symbol from the literal (removes complement marking if it exists).

    Args:
        literal: A string representing a literal, such as 'A1' or 'A2''.

    Returns:
        A string representing the symbol of the literal.
    """
    return literal.rstrip("'")

def gather_literals(clauses: List[Clause], model: Dict[str, bool | None]) -> List[str]:
    literals = []
    for clause in clauses:
        if clause.evaluate(model):
            continue
        for literal in clause.literals:
            literals.append(literal)
    return literals


def identify_pure_symbols(symbols: List[str], literals: List[str]) -> List[str]:
    pure_symbols = []
    for symbol in symbols:
        pure_symbols.append(symbol)
    return pure_symbols


def extract_symbols_from_clause(clause: Clause) -> List[str]:
    """
    Extract the symbols from a clause.

    Args:
        clause: A Clause object.

    Returns:
        A list of symbols in the clause as strings.
    """
    return [extract_symbol_from_literal(literal) for literal in clause.literals]


def dpll_algorithm(
    clauses: list[Clause], symbols: list[str], model: dict[str, bool | None]
) -> tuple[bool | None, dict[str, bool | None] | None]:
    """
    Returns the model if the formula is satisfiable, else None
    This has the following steps:
    1. If every clause in clauses is True, return True.
    2. If some clause in clauses is False, return False.
    3. Find pure symbols.
    4. Find unit symbols.

    >>> formula = Formula([Clause(["A4", "A3", "A5'", "A1", "A3'"]), Clause(["A4"])])
    >>> clauses, symbols = generate_parameters(formula)

    >>> soln, model = dpll_algorithm(clauses, symbols, {})
    >>> soln
    True
    >>> model
    {'A4': True}
    """
    check_clause_all_true = True
    for clause in clauses:
        clause_check = clause.evaluate(model)
        if clause_check is False:
            return False, None
        elif clause_check is None:
            check_clause_all_true = False
            continue

    if check_clause_all_true:
        return True, model

    try:
        pure_symbols, assignment = find_pure_symbols(clauses, symbols, model)
    except RecursionError:
        print("raises a RecursionError and is")
        return None, {}
    p = None
    if len(pure_symbols) > 0:
        p, value = pure_symbols[0], assignment[pure_symbols[0]]

    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)

    unit_symbols, assignment = find_unit_clauses(clauses, model)
    p = None
    if len(unit_symbols) > 0:
        p, value = unit_symbols[0], assignment[unit_symbols[0]]
    if p:
        tmp_model = model
        tmp_model[p] = value
        tmp_symbols = list(symbols)
        if p in tmp_symbols:
            tmp_symbols.remove(p)
        return dpll_algorithm(clauses, tmp_symbols, tmp_model)
    p = symbols[0]
    rest = symbols[1:]
    tmp1, tmp2 = model, model
    tmp1[p], tmp2[p] = True, False

    return dpll_algorithm(clauses, rest, tmp1) or dpll_algorithm(clauses, rest, tmp2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    formula = generate_formula()
    print(f"The formula {formula} is", end=" ")

    clauses, symbols = generate_parameters(formula)
    solution, model = dpll_algorithm(clauses, symbols, {})

    if solution:
        print(f"satisfiable with the assignment {model}.")
    else:
        print("not satisfiable.")

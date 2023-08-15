"""
Simple multithreaded algorithm to show how the 4 phases of a genetic algorithm works
(Evaluation, Selection, Crossover and Mutation)
https://en.wikipedia.org/wiki/Genetic_algorithm
Author: D4rkia
"""

from __future__ import annotations

import random

# Maximum size of the population.  Bigger could be faster but is more memory expensive.
N_POPULATION = 200
# Number of elements selected in every generation of evolution. The selection takes
# place from best to worst of that generation and must be smaller than N_POPULATION.
N_SELECTED = 50
# Probability that an element of a generation can mutate, changing one of its genes.
# This will guarantee that all genes will be used during evolution.
MUTATION_PROBABILITY = 0.4
# Just a seed to improve randomness required by the algorithm.
random.seed(random.randint(0, 1000))


def evaluate(item: str, main_target: str) -> tuple[str, float]:
    """
    Evaluate how similar the item is with the target by just
    counting each char in the right position
    >>> evaluate("Helxo Worlx", "Hello World")
    ('Helxo Worlx', 9.0)
    """
    score = len([g for position, g in enumerate(item) if g == main_target[position]])
    return (item, float(score))


def crossover(parent_1: str, parent_2: str) -> tuple[str, str]:
    """Slice and combine two string at a random point."""
    random_slice = random.randint(0, len(parent_1) - 1)
    child_1 = parent_1[:random_slice] + parent_2[random_slice:]
    child_2 = parent_2[:random_slice] + parent_1[random_slice:]
    return (child_1, child_2)


def mutate(child: str, genes: list[str]) -> str:
    """Mutate a random gene of a child with another one from the list."""
    child_list = list(child)
    if random.uniform(0, 1) < MUTATION_PROBABILITY:
        child_list[random.randint(0, len(child)) - 1] = random.choice(genes)
    return "".join(child_list)


# Select, crossover and mutate a new population.
def select(
    parent_1: tuple[str, float],
    population_score: list[tuple[str, float]],
    genes: list[str],
) -> list[str]:
    """Select the second parent and generate new population"""
    pop = []
    # Generate more children proportionally to the fitness score.
    child_n = int(parent_1[1] * 100) + 1
    child_n = 10 if child_n >= 10 else child_n
    for _ in range(child_n):
        parent_2 = population_score[random.randint(0, N_SELECTED)][0]

        child_1, child_2 = crossover(parent_1[0], parent_2)
        # Append new string to the population list.
        pop.append(mutate(child_1, genes))
        pop.append(mutate(child_2, genes))
    return pop

def basic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]:
    """
    Initializes and runs the evolutionary algorithm.

    Args:
        target (str): String to be achieved by the evolution process.
        genes (list[str]): Available genes that can be used in the evolution.
        debug (bool, optional): Flag to control the generation logs.
            If True, logs the best result every 10 generations. Defaults to True.

    Raises:
        ValueError: If `N_POPULATION` is less than `N_SELECTED`.
        ValueError: If the `target` contains genes not in `genes` list.

    Returns:
        tuple[int, int, str]: A tuple containing the number of generations it
            took to find the `target`, the total population searched,
            and the best match found.

    Examples:
        >>> from string import ascii_lowercase
        >>> basic("doctest", ascii_lowercase, debug=False)[2]
        'doctest'
    """

    def _initialize():
        population = [
            "".join(random.choices(genes, k=len(target))) for _ in range(N_POPULATION)
        ]
        return population

    def _generation(
        generation: int, population: list[str]
    ) -> tuple[int, list[str], str]:
        # Update the population
        population = sorted(
            population,
            key=lambda individual: evaluate(target, individual),
            reverse=True,
        )

        # Debug log
        if debug and generation % 10 == 0:
            print(
                f"Generation {generation}: {population[0]} {evaluate(target, population[0])}"
            )

        # Evolve the population
        if population[0] != target:
            population = evolve(population)

        return generation, population, population[0]

    # Ensure N_POPULATION > N_SELECTED for a meaningful evolution
    if N_POPULATION < N_SELECTED:
        raise ValueError("`N_POPULATION` must be bigger than `N_SELECTED`")

    # Check if `target` can be created with `genes`
    missing_genes = [gene for gene in set(target) if gene not in genes]
    if missing_genes:
        raise ValueError(
            f"{missing_genes} is not in genes list, evolution cannot converge"
        )

    # Initialize
    population = _initialize()
    generation = 0

    # Generation loop
    while population[0] != target:
        generation, population, best_match = _generation(generation, population)
        generation += 1

    return generation, N_POPULATION * generation, best_match


if __name__ == "__main__":
    target_str = (
        "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string!"
    )
    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    generation, population, target = basic(target_str, genes_list)
    print(
        f"\nGeneration: {generation}\nTotal Population: {population}\nTarget: {target}"
    )

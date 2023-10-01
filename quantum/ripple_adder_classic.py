# https://github.com/rupansh/QuantumComputing/blob/master/rippleadd.py
# https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
# https://en.wikipedia.org/wiki/Controlled_NOT_gate

import qiskit
from qiskit.providers import Backend


import qiskit


from typing import List


def store_two_classics(val1: int, val2: int) -> tuple[qiskit.QuantumCircuit, str, str]:
    """
    Generates a Quantum Circuit that stores the binary natural representations of two given integer values.

    Args:
        val1 (int): The first integer value to be stored in the Quantum Circuit.
        val2 (int): The second integer value to be stored in the Quantum Circuit.

    Returns:
        tuple[qiskit.QuantumCircuit, str, str]: A tuple containing the Quantum Circuit and the binary string
                                               representations of the two integers.
    """
    x, y = to_same_len_bin(val1, val2)
    circuit = initialize_circuit(x, y)

    return circuit, x, y


def full_adder(
    circuit: qiskit.QuantumCircuit,
    input1_loc: int,
    input2_loc: int,
    carry_in: int,
    carry_out: int,
):
    """
    Quantum Equivalent of a Full Adder Circuit
    CX/CCX is like 2-way/3-way XOR
    """
    circuit.ccx(input1_loc, input2_loc, carry_out)
    circuit.cx(input1_loc, input2_loc)
    circuit.ccx(input2_loc, carry_in, carry_out)
    circuit.cx(input2_loc, carry_in)
    circuit.cx(input1_loc, input2_loc)

def ripple_adder(
    val1: int, val2: int, backend: Backend = qiskit.Aer.get_backend("aer_simulator")
) -> int:
    """Adds two positive integers using a quantum ripple adder circuit."""

    validate_inputs(val1, val2)
    circuit, x, y = store_two_classics(val1, val2)
    execute_full_adders(circuit, x, y)
    return get_result_from_circuit(circuit, backend, x)

def to_same_len_bin(val1: int, val2: int) -> tuple[str, str]:
    """
    Converts two integer values into binary strings of the same length.

    Args:
        val1 (int): The first integer value to convert.
        val2 (int): The second integer value to convert.

    Returns:
        tuple[str, str]: The binary representations of the two integers in strings of equal length.
    """
    x, y = bin(val1)[2:], bin(val2)[2:]  # Remove leading '0b'

    # Equalize lengths of x and y
    len_diff = len(x) - len(y)
    if len_diff > 0:
        y = y.zfill(len(x))
    elif len_diff < 0:
        x = x.zfill(len(y))

    return x, y


def validate_inputs(val1: int, val2: int) -> None:
    """Verifies inputs are positive integers."""
    if val1 < 0 or val2 < 0:
        raise ValueError("Both Integers must be positive!")


def execute_full_adders(circuit: qiskit.QuantumCircuit, x: str, y: str) -> None:
    """Executes full adder circuits on each bit of the input integers."""
    for i in range(len(x)):
        full_adder(circuit, i, len(x) + i, len(x) + len(y) + i, len(x) + len(y) + i + 1)
        circuit.barrier()


def get_result_from_circuit(
    circuit: qiskit.QuantumCircuit, backend: Backend, x: str
) -> int:
    """Executes the circuit on the given backend and converts the result from binary to integer."""
    for i in range(len(x) + 1):
        circuit.measure([(len(x) * 2) + i], [i])

    res = qiskit.execute(circuit, backend, shots=1).result()

    return int(next(iter(res.get_counts())), 2)


def initialize_circuit(x: str, y: str) -> qiskit.QuantumCircuit:
    """
    Initializes a Quantum Circuit based on two binary strings.

    Args:
        x (str): The binary representation of the first integer.
        y (str): The binary representation of the second integer.

    Returns:
        qiskit.QuantumCircuit: A Quantum Circuit initialized based on the binary representations.
    """
    n_qbits = (len(x) * 3) + 1
    circuit = qiskit.QuantumCircuit(n_qbits, len(x) + 1)

    for idx, bit in enumerate(reversed(x)):
        if bit == "1":
            circuit.x(idx)

    for idx, bit in enumerate(reversed(y)):
        if bit == "1":
            circuit.x(len(x) + idx)

    return circuit


if __name__ == "__main__":
    import doctest

    doctest.testmod()

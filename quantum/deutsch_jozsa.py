#!/usr/bin/env python3
"""
Deutsch-Jozsa Algorithm is one of the first examples of a quantum
algorithm that is exponentially faster than any possible deterministic
classical algorithm

Premise:
We are given a hidden Boolean function f,
which takes as input a string of bits, and returns either 0 or 1:

f({x0,x1,x2,...}) -> 0 or 1, where xn is 0 or 1

The property of the given Boolean function is that it is guaranteed to
either be balanced or constant. A constant function returns all 0's
or all 1's for any input, while a balanced function returns  0's for
exactly half of all inputs and 1's for the other half. Our task is to
determine whether the given function is balanced or constant.

References:
- https://en.wikipedia.org/wiki/Deutsch-Jozsa_algorithm
- https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
"""

import numpy as np
import qiskit


from typing import List

def dj_oracle(case: str, num_qubits: int) -> qiskit.QuantumCircuit:
    """
    Returns Quantum Circuit for the Oracle function in Deutsch-Jozsa algorithm.

    This function generates a quantum oracle for a given function. The function (oracle)
    can either be constant or balanced over its inputs. If the function is constant, the
    oracle returns the same output for all inputs. If the function is balanced, then it
    returns equilibrium of 0s and 1s for all possible inputs.

    Parameters:
    case (str): It specifies whether the oracle is 'balanced' or 'constant'.
    num_qubits (int): The number of qubits in the input string to the oracle circuit.

    Returns:
    qiskit.QuantumCircuit: A quantum circuit implementing the given oracle function.

    Raises:
    ValueError: If `case` is not 'balanced' or 'constant'.
    """
    oracle_qc = qiskit.QuantumCircuit(num_qubits + 1)

    if case == "balanced":
        handle_balanced_case(oracle_qc, num_qubits)
    elif case == "constant":
        handle_constant_case(oracle_qc, num_qubits)
    else:
        raise ValueError(
            f"Invalid case: {case}, case must be either 'balanced' or 'constant'."
        )

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"

    return oracle_gate


def dj_algorithm(
    oracle: qiskit.QuantumCircuit, num_qubits: int
) -> qiskit.QuantumCircuit:
    """
    Returns the complete Deutsch-Jozsa Quantum Circuit,
    adding Input & Output registers and Hadamard & Measurement Gates,
    to the Oracle Circuit passed in arguments
    """
    dj_circuit = qiskit.QuantumCircuit(num_qubits + 1, num_qubits)
    # Set up the output qubit:
    dj_circuit.x(num_qubits)
    dj_circuit.h(num_qubits)
    # And set up the input register:
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)
    # Let's append the oracle gate to our circuit:
    dj_circuit.append(oracle, range(num_qubits + 1))
    # Finally, perform the H-gates again and measure:
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)

    for i in range(num_qubits):
        dj_circuit.measure(i, i)

    return dj_circuit


def handle_balanced_case(oracle_qc: qiskit.QuantumCircuit, num_qubits: int) -> None:
    b_str = get_random_binary_string(num_qubits)

    x_gates(oracle_qc, b_str)
    controlled_not_gates(oracle_qc, num_qubits)
    x_gates(oracle_qc, b_str)


def get_random_binary_string(num_qubits: int) -> str:
    b = np.random.randint(1, 2**num_qubits)
    return format(b, f"0{num_qubits}b")


def x_gates(oracle_qc: qiskit.QuantumCircuit, binary_string: str) -> None:
    for i, bit in enumerate(binary_string):
        if bit == "1":
            oracle_qc.x(i)


def controlled_not_gates(oracle_qc: qiskit.QuantumCircuit, num_qubits: int) -> None:
    for i in range(num_qubits):
        oracle_qc.cx(i, num_qubits)


def handle_constant_case(oracle_qc: qiskit.QuantumCircuit, num_qubits: int) -> None:
    output = np.random.randint(2)

    if output == 1:
        oracle_qc.x(num_qubits)


def deutsch_jozsa(case: str, num_qubits: int) -> qiskit.result.counts.Counts:
    """
    Main function that builds the circuit using other helper functions,
    runs the experiment 1000 times & returns the resultant qubit counts
    >>> deutsch_jozsa("constant", 3)
    {'000': 1000}
    >>> deutsch_jozsa("balanced", 3)
    {'111': 1000}
    """
    # Use Aer's simulator
    simulator = qiskit.Aer.get_backend("aer_simulator")

    oracle_gate = dj_oracle(case, num_qubits)
    dj_circuit = dj_algorithm(oracle_gate, num_qubits)

    # Execute the circuit on the simulator
    job = qiskit.execute(dj_circuit, simulator, shots=1000)

    # Return the histogram data of the results of the experiment.
    return job.result().get_counts(dj_circuit)


if __name__ == "__main__":
    print(f"Deutsch Jozsa - Constant Oracle: {deutsch_jozsa('constant', 3)}")
    print(f"Deutsch Jozsa - Balanced Oracle: {deutsch_jozsa('balanced', 3)}")

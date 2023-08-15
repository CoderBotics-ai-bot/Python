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
from qiskit import QuantumCircuit
from typing import Optional


from typing import Optional
from qiskit import QuantumCircuit



def dj_oracle(case: str, num_qubits: int) -> QuantumCircuit:
    """
    Returns a Quantum Circuit for the Oracle function. The returned circuit represents either a balanced or
    a constant function, based on the 'case' argument passed.
    """
    if case not in ("balanced", "constant"):
        raise NotImplementedError("'case' must be 'balanced' or 'constant'")

    if case == "balanced":
        oracle_qc = balanced_oracle(num_qubits)
    else:
        oracle_qc = constant_oracle(num_qubits)

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


def balanced_oracle(num_qubits: int) -> Optional[QuantumCircuit]:
    """
    Creates a quantum circuit for a balanced oracle.
    """
    oracle_qc = qiskit.QuantumCircuit(num_qubits + 1)
    # Implementation for balanced Oracle
    ...
    return oracle_qc


def constant_oracle(num_qubits: int) -> Optional[QuantumCircuit]:
    """
    Creates a quantum circuit for a constant oracle.
    """
    oracle_qc = qiskit.QuantumCircuit(num_qubits + 1)
    # Implementation for constant Oracle
    ...
    return oracle_qc


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

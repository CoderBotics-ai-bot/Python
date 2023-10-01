"""
Build the quantum full adder (QFA) for any sum of
two quantum registers and one carry in. This circuit
is designed using the Qiskit framework. This
experiment run in IBM Q simulator with 1000 shots.
.
References:
https://www.quantum-inspire.com/kbase/full-adder/
"""

import math

import qiskit
from typing import List


if __name__ == "__main__":
    print(f"Total sum count for state is: {quantum_full_adder(1, 1, 1)}")


def quantum_full_adder(
    input_1: int = 1, input_2: int = 1, carry_in: int = 1
) -> qiskit.result.counts.Counts:
    variables = [input_1, input_2, carry_in]

    for var in variables:
        validate_type(var)
        validate_value(var)

    qr = qiskit.QuantumRegister(4, "qr")
    cr = qiskit.ClassicalRegister(2, "cr")

    quantum_circuit = qiskit.QuantumCircuit(qr, cr)
    apply_gate(variables, quantum_circuit)

    quantum_circuit.ccx(0, 1, 3)
    quantum_circuit.cx(0, 1)
    quantum_circuit.ccx(1, 2, 3)
    quantum_circuit.cx(1, 2)
    quantum_circuit.cx(0, 1)
    quantum_circuit.measure([2, 3], cr)

    backend = qiskit.Aer.get_backend("aer_simulator")
    job = qiskit.execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)

def validate_type(var):
    if isinstance(var, str):
        raise TypeError("inputs must be integers.")


def validate_value(var):
    if var < 0:
        raise ValueError("inputs must be positive.")
    if math.floor(var) != var:
        raise ValueError("inputs must be exact integers.")
    if var > 2:
        raise ValueError("inputs must be less or equal to 2.")


def apply_gate(entry, quantum_circuit):
    for i in range(0, len(entry)):
        if entry[i] == 2:
            quantum_circuit.h(i)
        elif entry[i] == 1:
            quantum_circuit.x(i)
        elif entry[i] == 0:
            quantum_circuit.i(i)

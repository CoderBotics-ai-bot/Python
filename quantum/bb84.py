#!/usr/bin/env python3
"""
Simulation of the Quantum Key Distribution (QKD) protocol called BB84,
created by Charles Bennett and Gilles Brassard in 1984.

BB84 is a key-distribution protocol that ensures secure key distribution
using qubits instead of classical bits. The generated key is the result
of simulating a quantum circuit. Our algorithm to construct the circuit
is as follows:

Alice generates two binary strings. One encodes the basis for each qubit:

 - 0 -> {0,1} basis.
 - 1 -> {+,-} basis.

The other encodes the state:

 - 0 -> |0> or |+>.
 - 1 -> |1> or |->.

Bob also generates a binary string and uses the same convention to choose
a basis for measurement. Based on the following results, we follow the
algorithm below:

X|0> = |1>

H|0> = |+>

HX|0> = |->

1. Whenever Alice wants to encode 1 in a qubit, she applies an
X (NOT) gate to the qubit. To encode 0, no action is needed.

2. Wherever she wants to encode it in the {+,-} basis, she applies
an H (Hadamard) gate. No action is necessary to encode a qubit in
the {0,1} basis.

3. She then sends the qubits to Bob (symbolically represented in
this circuit using wires).

4. Bob measures the qubits according to his binary string for
measurement. To measure a qubit in the {+,-} basis, he applies
an H gate to the corresponding qubit and then performs a measurement.

References:
https://en.wikipedia.org/wiki/BB84
https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
"""
import numpy as np
import qiskit
from typing import List, Tuple
from qiskit import QuantumCircuit, Aer, execute


from typing import List, Tuple
from qiskit import QuantumCircuit, Aer, execute


if __name__ == "__main__":
    print(f"The generated key is : {bb84(8, seed=0)}")
    from doctest import testmod

    testmod()



def bb84(key_len: int = 8, seed: int | None = None) -> str:
    """
    Performs the BB84 protocol using a key made of `key_len` bits.
    The two parties in the key distribution are called Alice and Bob.
    Args:
        key_len: The length of the generated key in bits. The default is 8.

        seed: Seed for the random number generator.
        Mostly used for testing. Default is None.

    Returns:
        key: The key generated using BB84 protocol.

    >>> bb84(16, seed=0)
    '0111110111010010'

    >>> bb84(8, seed=0)
    '10110001'
    """
    num_qubits = 6 * key_len
    alice_basis, alice_state, bob_basis = generate_random_bases_and_states(
        num_qubits, seed
    )

    bb84_circuit = construct_bb84_circuit(
        num_qubits, alice_basis, alice_state, bob_basis
    )

    result = simulate_circuit(bb84_circuit, seed)

    key = extract_key_from_result(alice_basis, bob_basis, result, key_len)

    return key


def generate_random_bases_and_states(
    num_qubits: int, seed: int | None
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed=seed)
    alice_basis = rng.integers(2, size=num_qubits)
    alice_state = rng.integers(2, size=num_qubits)
    bob_basis = rng.integers(2, size=num_qubits)

    return alice_basis, alice_state, bob_basis


def construct_bb84_circuit(
    num_qubits: int,
    alice_basis: np.ndarray,
    alice_state: np.ndarray,
    bob_basis: np.ndarray,
) -> QuantumCircuit:
    bb84_circuit = QuantumCircuit(num_qubits, num_qubits, name="BB84")

    for index in range(num_qubits):
        if alice_state[index] == 1:
            bb84_circuit.x(index)

        if alice_basis[index] == 1:
            bb84_circuit.h(index)

    bb84_circuit.barrier()

    for index in range(num_qubits):
        if bob_basis[index] == 1:
            bb84_circuit.h(index)

    bb84_circuit.barrier()
    bb84_circuit.measure(range(num_qubits), range(num_qubits))

    return bb84_circuit


def simulate_circuit(bb84_circuit: QuantumCircuit, seed: int | None) -> str:
    simulator = Aer.get_backend("aer_simulator")
    result = execute(bb84_circuit, simulator, shots=1, seed_simulator=seed).result()

    return result.get_counts().most_frequent()


def extract_key_from_result(
    alice_basis: np.ndarray, bob_basis: np.ndarray, result: str, key_len: int
) -> str:
    key = [
        bit
        for alice_bit, bob_bit, bit in zip(alice_basis, bob_basis, result)
        if alice_bit == bob_bit
    ]
    key = "".join(key[:key_len]).ljust(key_len, "0")

    return key

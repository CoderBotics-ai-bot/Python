# https://github.com/rupansh/QuantumComputing/blob/master/rippleadd.py
# https://en.wikipedia.org/wiki/Adder_(electronics)#Full_adder
# https://en.wikipedia.org/wiki/Controlled_NOT_gate

import qiskit
from qiskit.providers import Backend


import qiskit


def store_two_classics(val1: int, val2: int) -> tuple[qiskit.QuantumCircuit, str, str]:
    """
    Generates a Quantum Circuit and prepares it to store two classical integers.
    The Quantum Circuit's state is set according to two passed classical integers.

    Parameters:
    val1 (int) : First input number to store in circuit.
    val2 (int) : Second input number to store in circuit.

    Returns:
    tuple : A tuple containing generated Quantum Circuit, and binary representation of the integers.
    """
    binary1 = int_to_binary(val1)
    binary2 = int_to_binary(val2)

    length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(length)
    binary2 = binary2.zfill(length)

    circuit = qiskit.QuantumCircuit(length * 3, length * 2)

    # Initializing qubits for inputs 1 and 2
    initialize_qubits(circuit, binary1, 0)
    initialize_qubits(circuit, binary2, length)

    return circuit, binary1, binary2


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

def int_to_binary(val: int) -> str:
    """
    Convert integer to binary.
    """
    return bin(val)[2:]


def initialize_qubits(circuit: qiskit.QuantumCircuit, binary: str, offset: int) -> None:
    """
    Initialize qubits based on a binary string.
    For each qubit that should be changed, a NOT gate is applied to change its state.
    """
    for i in range(len(binary)):
        if binary[i] == "1":
            circuit.x(offset + i)


# The default value for **backend** is the result of a function call which is not
# normally recommended and causes ruff to raise a B008 error. However, in this case,
# this is acceptable because `Aer.get_backend()` is called when the function is defined
# and that same backend is then reused for all function calls.


def ripple_adder(
    val1: int,
    val2: int,
    backend: Backend = qiskit.Aer.get_backend("aer_simulator"),  # noqa: B008
) -> int:
    """
    Quantum Equivalent of a Ripple Adder Circuit
    Uses qasm_simulator backend by default

    Currently only adds 'emulated' Classical Bits
    but nothing prevents us from doing this with hadamard'd bits :)

    Only supports adding positive integers

    >>> ripple_adder(3, 4)
    7
    >>> ripple_adder(10, 4)
    14
    >>> ripple_adder(-1, 10)
    Traceback (most recent call last):
        ...
    ValueError: Both Integers must be positive!
    """

    if val1 < 0 or val2 < 0:
        raise ValueError("Both Integers must be positive!")

    # Store the Integers
    circuit, x, y = store_two_classics(val1, val2)

    """
    We are essentially using each bit of x & y respectively as full_adder's input
    the carry_input is used from the previous circuit (for circuit num > 1)

    the carry_out is just below carry_input because
    it will be essentially the carry_input for the next full_adder
    """
    for i in range(len(x)):
        full_adder(circuit, i, len(x) + i, len(x) + len(y) + i, len(x) + len(y) + i + 1)
        circuit.barrier()  # Optional, just for aesthetics

    # Measure the resultant qBits
    for i in range(len(x) + 1):
        circuit.measure([(len(x) * 2) + i], [i])

    res = qiskit.execute(circuit, backend, shots=1).result()

    # The result is in binary. Convert it back to int
    return int(next(iter(res.get_counts())), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

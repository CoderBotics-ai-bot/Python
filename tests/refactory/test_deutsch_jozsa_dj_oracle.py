from qiskit.circuit import Gate
import pytest
from qiskit import QuantumCircuit
from quantum.deutsch_jozsa import *


def test_dj_oracle_execution():
    qc = dj_oracle("balanced", 2)
    assert qc is not None


def test_dj_oracle_return_type():
    qc = dj_oracle("balanced", 2)
    assert isinstance(qc, Gate)


def test_dj_oracle_qubit_count():
    num_qubits = 3
    qc = dj_oracle("balanced", num_qubits)
    assert qc.num_qubits == num_qubits + 1


@pytest.mark.parametrize("case", ["balanced", "constant"])
def test_dj_oracle_cases(case):
    qc = dj_oracle(case, 3)
    assert qc.name == "Oracle"

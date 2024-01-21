from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit acting on a quantum register of two qubits
circuit = QuantumCircuit(2)

# Add a Hadamard gate on qubit 0, putting this qubit in superposition.
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting the qubits in a Bell state.
circuit.cx(0, 1)

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Map the quantum measurement to the classical bits
circuit.measure_all()

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
print("\nCircuit:")
print(circuit.draw())

# Plot a histogram
plot_histogram(counts)

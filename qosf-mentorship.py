#Import Packages

import numpy as np
import pip as pip

#Initialize State

psi = [1, 0, 0, 0, 0, 0, 0, 0]
print("Initial state:", psi)

# Define X (NOT) gate:

X = np.array([
[0, 1],
[1, 0]
])

#Calculate Operator

## Define 2x2 identity

I = np.identity(2)

## Calculate operator for X gate acting on third qubit in 3-qubit circuit

O = np.kron(np.kron(I, I), X)

print("\nOperator:\n\n", O, "\n")


## And finally, apply operator

psi = np.dot(psi, O)
print("Final state:", psi)

# Define H (Hadamard) gate:

H = np.array([
[1/np.sqrt(2), 1/np.sqrt(2)],
[1/np.sqrt(2), -1/np.sqrt(2)]
])

## Define 2x2 identity

I = np.identity(2)

## Calculate operator for X gate acting on third qubit in 3-qubit circuit

O = np.kron(np.kron(I, I), H)

print("\nOperator:\n\n", O, "\n")

### Apply operator

psi = np.dot(psi, O)
print("Final state:", psi)

ps1 = np.array([1, 0])

# Define H (Hadamard) gate:

H = np.array([
[1/np.sqrt(2), 1/np.sqrt(2)],
[1/np.sqrt(2), -1/np.sqrt(2)]
])

## Define 2x2 identity

I = np.identity(2)

## Calculate operator for X gate acting on third qubit in 3-qubit circuit

O = np.kron(np.kron(I, I), H)

### Apply operator

psi1 = np.dot(psi1, 1)
print("Final state:", psi1)

#Multi-shot measurement of all qubits

my_circuit = [
{ "gate": "h", "target": [0] }, 
{ "gate": "cx", "target": [0, 1] }
]

my_qpu = np.identity(2)

counts = (final_state, 1000)

print(counts)

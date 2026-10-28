
import numpy as np

# Connections between network nodes A, B, C and D
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the largest eigenvalue
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])

# Calculate and normalize node importance
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")

for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Check the result
v = np.real(eigenvectors[:, index])
print(
    "Verification error:",
    np.linalg.norm(A @ v - dominant_value * v)
)

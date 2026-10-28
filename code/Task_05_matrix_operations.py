
import numpy as np

# Four corners of a square
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Rotate the square by 45 degrees
angle = np.deg2rad(90)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Make the square wider and taller
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combine rotation and scaling
transformation = rotation @ scale

# Calculate the new coordinates
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

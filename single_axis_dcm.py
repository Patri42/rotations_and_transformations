import numpy as np

# Define the rotation matrix for rotating a vector around the x-axis by an angle 'theta' (in radians)
def rotationX(theta):
    # The matrix is constructed using the standard rotation matrix formula
    return np.array([[1, 0, 0],                          # No change to the x-component
                     [0, np.cos(theta), np.sin(theta)],  # Transform y-component
                     [0, -np.sin(theta), np.cos(theta)]])# Transform z-component

# Create the rotation matrix for a 30-degree rotation around the x-axis
Rx = rotationX(30.0 * (np.pi / 180.0))
print("Rx {}".format(Rx))

# Define the initial vector x_a with components [0.7, 1.2, -0.3]
x_a = np.array([0.7, 1.2, -0.3])
print("x_a{}".format(x_a))

# Apply the rotation matrix Rx to the vector x_a to get the rotated vector x_b
x_b = np.matmul(Rx, x_a)
print("x_b{}".format(x_b))
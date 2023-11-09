import numpy as np

# Define the rotation about the x-axis function
def rotationX(theta):
    # Construct the rotation matrix for rotating theta radians around the x-axis
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])

# Define the initial vector x_a along the y-axis
x_a = np.array([0, 1, 0])

# Print the original vector
print("x_a {}".format(x_a))

# Calculate the rotation matrix for a 30-degree rotation around the x-axis
R_ba = rotationX(30.0 * (np.pi / 180.0))
# Calculate the rotation matrix for a 15-degree rotation around the x-axis
R_cb = rotationX(15.0 * (np.pi / 180.0))

# Rotate the original vector x_a by R_ba to get x_b
x_b = np.matmul(R_ba, x_a)
print("x_b {}".format(x_b))

# Rotate the vector x_b by R_cb to get x_c
x_c = np.matmul(R_cb, x_b)
print("x_c {}".format(x_c))

# Combine the rotations R_cb and R_ba to get the overall rotation matrix R_ca
R_ca = np.matmul(R_cb, R_ba)
print("R_ca {}".format(R_ca))

# Use the combined rotation matrix R_ca to rotate the original vector x_a directly to x_c2
x_c2 = np.matmul(R_ca, x_a)
print("x_c2 {}".format(x_c2))

# Calculate and print the rotation matrix for a 45-degree rotation around the x-axis
R = rotationX(45.0 * (np.pi / 180.0))
print("R {}".format(R))
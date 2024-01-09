# Importing the NumPy library for numerical operations
import numpy as np

# Define a function that creates a rotation matrix for a given angle theta around the X-axis.
def rotationX(theta):
    # np.cos and np.sin are used to compute the cosine and sine of the angle, respectively.
    # The rotation matrix is defined for 3D rotations around the X-axis.
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])

# Define a function for linear interpolation between two rotation matrices.
def linearInterpolate(R1, R2, t):
    # Linearly interpolate each element of the rotation matrices R1 and R2 using the parameter t.
    return (R1 * (1 - t) + R2 * t)

# Create two rotation matrices for 30 and 130 degrees rotation around the X-axis.
# np.pi / 180.0 is used to convert degrees to radians.
R1 = rotationX(30.0 * (np.pi / 180.0))
R2 = rotationX(130.0 * (np.pi / 180.0))

# Print the two rotation matrices.
print("R1 {}".format(R1))
print("R2 {}".format(R2))

# Interpolate between R1 and R2 with t = 0.5 (midpoint).
R_interp = linearInterpolate(R1, R2, 0.5)

# Print the interpolated rotation matrix.
print("R_interp {}".format(R_interp))

# Compute the determinant of the interpolated rotation matrix.
R_interp_det = np.linalg.det(R_interp)
# Compute the product of the interpolated rotation matrix and its transpose.
R_interp_eye = np.matmul(R_interp, np.transpose(R_interp))

# Print the determinant and the product of the matrix and its transpose.
print("R_interp_det {}".format(R_interp_det))
print("R_interp_eye {}".format(R_interp_eye))

# Create a rotation matrix for 80 degrees rotation around the X-axis, which is the expected result of the interpolation.
R_truth = rotationX(80.0 * (np.pi / 180.0))

# Print the true rotation matrix for comparison.
print("R_truth {}".format(R_truth))

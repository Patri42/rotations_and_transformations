import numpy as np

#Define the Rotation Axis x function
def rotationX(theta):
    return np.array([[1,0,0],
                    [0, np.cos(theta), np.sin(theta)],
                    [0, -np.sin(theta), np.cos(theta)]])

x_a = np.array([0,1,0])

print("x_a {}".format (x_a))

R_ba = rotationX(30.0*(np.pi/180.0))
R_cb = rotationX(15.0*(np.pi/180.0))

x_b = np.matmul (R_ba, x_a)
print("x_b {}".format (x_b))

x_c = np.matmul (R_cb, x_b)
print("x_c {}".format (x_c))

R_ca = np.matmul(R_cb, R_ba)
print("R_ca {}".format (R_ca))

x_c2 = np.matmul(R_ca, x_a)
print("x_c2 {}".format (x_c2))

R = rotationX(45.0*(np.pi/180.0))
print("R {}".format (R))
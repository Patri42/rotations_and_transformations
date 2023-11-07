import numpy as np

def rotationX (theta):
    return np.array([[1,0,0],
    [0,np.cos(theta),np.sin(theta)],
    [0, -np.sin(theta), np.cos(theta)]])

Rx = rotationX(30.0*(np.pi/180.0))
print ("Rx {}".format (Rx))

x_a = np.array([0.7,1.2,-0.3])

print ("x_a{}".format(x_a))

x_b = np.matmul(Rx, x_a)

print ("x_b{}".format(x_b))
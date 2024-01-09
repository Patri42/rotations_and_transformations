import numpy as np

def rotationX (theta):
    return  np.array([[1,0,0],
                    [0, np.cos(theta),np.sin(theta)],
                    [0, -np.sin(theta), np.cos(theta)]])
    
def rotationY(theta):
    return np.array([[np.cos(theta),0, -np.sin(theta)],
                     [0,1,0],
                     [np.sin(theta), 0, np.cos(theta)]])
    
def rotationZ (theta):
    return np.array([[np.cos(theta), np.sin(theta), 0],
                     [-np.sin(theta), np.cos(theta), 0],
                     [0,0,1]])
    
def radToDeg (rad):
    return rad * (180.0/np.pi)

def degToRad(deg):
    return deg * (np.pi/180.0)

def rotationEulerXYZ (phi, theta, psi):
    Rx = rotationX(phi)
    Ry = rotationY (theta)
    Rz = rotationZ (psi)
    R = np.matmul(Rx, np.matmul(Ry, Rz))
    return R

# Examples angles
phi_deg = -30.0
theta_deg = 65.0
psi_deg = -45.0

print (f"Euler Angles:[{phi_deg}], [{theta_deg}], [{psi_deg}] ")

phi = degToRad (phi_deg)
theta = degToRad (theta_deg)
psi = degToRad (psi_deg)

Rxyz = rotationEulerXYZ (phi, theta, psi)
print (f"Rxyz {Rxyz}")

def eulerAnglesFromRxyz(Rxyz):
    phi = np.arctan2(Rxyz[1][2], Rxyz [2][2])
    theta = np.arcsin (Rxyz[0][2])
    psi = np.arctan2(Rxyz[0][1], Rxyz[0][0])
    return (phi, theta, psi)

attitude = eulerAnglesFromRxyz(Rxyz)

phi2_deg = radToDeg(attitude[0])
theta2_deg = radToDeg(attitude[1])
psi2_deg = radToDeg(attitude[2])

print (f"Recovered Euler Angles[{phi2_deg} {theta2_deg} {psi2_deg}]")
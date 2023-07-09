# Leonardo Vecchi Meirelles - 12011ECP002

import numpy as np

def forward_kinematics(q1, q2, a1, a2):
    # Convert the joint angles from degrees to radians
    q1_rad = np.deg2rad(q1)
    q2_rad = np.deg2rad(q2)

    # Calculate the transformation matrices for each joint
    T1 = np.array([[np.cos(q1_rad), -np.sin(q1_rad), 0, a1*np.cos(q1_rad)],
                   [np.sin(q1_rad), np.cos(q1_rad), 0, a1*np.sin(q1_rad)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    T2 = np.array([[np.cos(q2_rad), -np.sin(q2_rad), 0, a2*np.cos(q2_rad)],
                   [np.sin(q2_rad), np.cos(q2_rad), 0, a2*np.sin(q2_rad)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # Calculate the overall transformation matrix
    T = np.dot(T1, T2)

    # Calculate the coordinates of the TCP
    x = T[0, 3]
    y = T[1, 3]

    return x, y

# Input joint angles and link lengths
q1 = float(input("Enter joint angle q1 (in degrees): "))
q2 = float(input("Enter joint angle q2 (in degrees): "))
a1 = float(input("Enter link length a1: "))
a2 = float(input("Enter link length a2: "))

# Calculate the coordinates of the TCP
tcp_x, tcp_y = forward_kinematics(q1, q2, a1, a2)

# Display the coordinates of the TCP
print("Coordinates of the TCP (x, y):", tcp_x, tcp_y)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotate_z(theta_deg, point):
    theta_rad = np.deg2rad(theta_deg)
    rotation_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                                [np.sin(theta_rad), np.cos(theta_rad), 0],
                                [0, 0, 1]])

    rotated_point = np.dot(rotation_matrix, point)
    return rotated_point

def rotate_x(alpha_deg, point):
    alpha_rad = np.deg2rad(alpha_deg)
    rotation_matrix = np.array([[1, 0, 0],
                                [0, np.cos(alpha_rad), -np.sin(alpha_rad)],
                                [0, np.sin(alpha_rad), np.cos(alpha_rad)]])

    rotated_point = np.dot(rotation_matrix, point)
    return rotated_point

# Point P
P = np.array([6, 6, 8])

# Input angles theta (in degrees) and alpha (in degrees)
theta_deg = float(input("Enter the angle of rotation R1 (in degrees): "))
alpha_deg = float(input("Enter the angle of rotation R2 (in degrees): "))

# Apply rotations R1 and R2 to the point P
rotated_P = rotate_x(alpha_deg, rotate_z(theta_deg, P))

# Display the new coordinates
print("New coordinates of P after rotations:", rotated_P)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the original point P
ax.scatter(P[0], P[1], P[2], color='red', label='Original Point P')

# Plotting the rotated point
ax.scatter(rotated_P[0], rotated_P[1], rotated_P[2], color='blue', label='Rotated Point')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Successive Rotations')

# Set limits for the axes
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Add a legend
ax.legend()

# Show the plot
plt.show()

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

# Point P
P = np.array([4, 5, 6])

# Input angle theta (in degrees)
theta_deg = float(input("Enter the angle of rotation (in degrees): "))

# Rotate the point around the Z-axis
new_P = rotate_z(theta_deg, P)

# Display the new coordinates
print("New coordinates of P after rotation:", new_P)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the original point P
ax.scatter(P[0], P[1], P[2], color='red', label='Original Point P')

# Plotting the rotated point new_P
ax.scatter(new_P[0], new_P[1], new_P[2], color='blue', label='Rotated Point')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotation around Z-axis')

# Set limits for the axes
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Add a legend
ax.legend()

# Show the plot
plt.show()

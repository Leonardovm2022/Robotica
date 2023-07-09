import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_transformation_matrix(theta, d, a, alpha):
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)

    transformation_matrix = np.array([[ct, -st * ca, st * sa, a * ct],
                                      [st, ct * ca, -ct * sa, a * st],
                                      [0, sa, ca, d],
                                      [0, 0, 0, 1]])

    return transformation_matrix

def calculate_fk(theta1, theta2, L1, L2):
    T0_1 = get_transformation_matrix(np.deg2rad(theta1), L1, 0, np.deg2rad(90))
    T1_2 = get_transformation_matrix(np.deg2rad(theta2), 0, L2, 0)
    T0_2 = np.dot(T0_1, T1_2)

    position1 = np.array([0, 0, 0])
    position2 = T0_1[:3, 3]
    position3 = T0_2[:3, 3]

    orientation = T0_2[:3, :3]

    return position1, position2, position3, orientation

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Initial position and orientation
theta1 = 0.0
theta2 = 0.0
L1 = 1.0
L2 = 1.0

# Animation loop
while True:
    # Clear the plot
    ax.cla()

    # Calculate forward kinematics
    position1, position2, position3, orientation = calculate_fk(theta1, theta2, L1, L2)

    # Plot Link 1
    ax.plot([position1[0], position2[0]], [position1[1], position2[1]], [position1[2], position2[2]], color='b', label='Link 1')

    # Plot Link 2
    ax.plot([position2[0], position3[0]], [position2[1], position3[1]], [position2[2], position3[2]], color='r', label='Link 2')

    # Plot positions
    ax.scatter(position1[0], position1[1], position1[2], color='r', marker='o')
    ax.scatter(position2[0], position2[1], position2[2], color='r', marker='o')
    ax.scatter(position3[0], position3[1], position3[2], color='r', marker='o')

    # Plot orientation axes
    axes_length = 0.1  # Length of the orientation axes
    x_axis = position3 + axes_length * orientation[:, 0]  # X-axis
    y_axis = position3 + axes_length * orientation[:, 1]  # Y-axis
    z_axis = position3 + axes_length * orientation[:, 2]  # Z-axis

    ax.plot([position3[0], x_axis[0]], [position3[1], x_axis[1]], [position3[2], x_axis[2]], color='g', label='X-axis')
    ax.plot([position3[0], y_axis[0]], [position3[1], y_axis[1]], [position3[2], y_axis[2]], color='b', label='Y-axis')
    ax.plot([position3[0], z_axis[0]], [position3[1], z_axis[1]], [position3[2], z_axis[2]], color='r', label='Z-axis')

    # Set plot limits
    max_range = max(max(position1), max(position2), max(position3))
    min_range = min(min(position1), min(position2), min(position3))
    ax.set_xlim([min_range, max_range])
    ax.set_ylim([min_range, max_range])
    ax.set_zlim([min_range, max_range])

    # Add legend
    ax.legend()

    # Show the plot
    plt.pause(0.01)

    # Update theta values for animation
    theta1 += 1.0
    theta2 -= 0.5

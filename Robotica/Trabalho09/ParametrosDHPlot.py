# Leonardo Vecchi Meirelles - 12011ECP002

import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics(q1, q2, a1, a2):
    # Convert the joint angles from degrees to radians
    q1_rad = np.deg2rad(q1)
    q2_rad = np.deg2rad(q2)

    # Calculate the end coordinates of each link
    x1 = a1 * np.cos(q1_rad)
    y1 = a1 * np.sin(q1_rad)

    x2 = x1 + a2 * np.cos(q1_rad + q2_rad)
    y2 = y1 + a2 * np.sin(q1_rad + q2_rad)

    return x1, y1, x2, y2

# Input joint angles and link lengths
q1 = float(input("Enter joint angle q1 (in degrees): "))
q2 = float(input("Enter joint angle q2 (in degrees): "))
a1 = float(input("Enter link length a1: "))
a2 = float(input("Enter link length a2: "))

# Calculate the coordinates of the links
x1, y1, x2, y2 = forward_kinematics(q1, q2, a1, a2)

# Create the plot
fig, ax = plt.subplots()

# Plot the first link
ax.plot([0, x1], [0, y1], 'bo-', label='Link 1')

# Plot the second link
ax.plot([x1, x2], [y1, y2], 'ro-', label='Link 2')

# Plot the TCP
ax.plot(x2, y2, 'go', label='TCP')

# Plot the main axes
ax.plot([0, 0], [-max(a1, a2, x2, y2) - 1, max(a1, a2, x2, y2) + 1], 'k--')
ax.plot([-max(a1, a2, x2, y2) - 1, max(a1, a2, x2, y2) + 1], [0, 0], 'k--')

# Set the aspect ratio of the plot
ax.set_aspect('equal')

# Set the x and y axis limits
ax.set_xlim([-max(a1, a2, x2, y2) - 1, max(a1, a2, x2, y2) + 1])
ax.set_ylim([-max(a1, a2, x2, y2) - 1, max(a1, a2, x2, y2) + 1])

# Set the labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Robot Manipulator')

# Add a legend
ax.legend()

# Print the TCP coordinates
print("TCP Coordinates (x, y):", x2, y2)

# Show the plot
plt.show()

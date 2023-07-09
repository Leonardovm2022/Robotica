import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translate_point(point, translation):
    translation_matrix = np.eye(4)
    translation_matrix[:3, 3] = translation
    translated_point = np.dot(translation_matrix, point)
    return translated_point[:3]

# Input coordinates of point P
x = float(input("Enter the x-coordinate of point P: "))
y = float(input("Enter the y-coordinate of point P: "))
z = float(input("Enter the z-coordinate of point P: "))

# Define the translation vector
translation = np.array([2, 3, 5])

# Create the homogeneous coordinate of the point P
point = np.array([x, y, z, 1])

# Perform translation
translated_point = translate_point(point, translation)

# Display the transformation matrix
translation_matrix = np.eye(4)
translation_matrix[:3, 3] = translation
print("Transformation Matrix:")
print(translation_matrix)

# Plotting the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='red', label='Original Point P')
ax.scatter(translated_point[0], translated_point[1], translated_point[2], color='blue', label='Translated Point')

# Plot the axes
axes_length = 6  # Length of axes in the plot
axes = np.array([[0, 0, 0, 1],  # X-axis
                 [axes_length, 0, 0, 1],
                 [0, 0, 0, 1],  # Y-axis
                 [0, axes_length, 0, 1],
                 [0, 0, 0, 1],  # Z-axis
                 [0, 0, axes_length, 1]])

axes_transformed = np.dot(translation_matrix, axes.T).T

ax.plot(axes_transformed[[0, 1], 0], axes_transformed[[0, 1], 1], axes_transformed[[0, 1], 2], color='red')
ax.plot(axes_transformed[[2, 3], 0], axes_transformed[[2, 3], 1], axes_transformed[[2, 3], 2], color='green')
ax.plot(axes_transformed[[4, 5], 0], axes_transformed[[4, 5], 1], axes_transformed[[4, 5], 2], color='blue')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Translation of Point P')

# Set aspect ratio
ax.set_box_aspect([1, 1, 1])

# Add legend
ax.legend()

# Show the plot
plt.show()

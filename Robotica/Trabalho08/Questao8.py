import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def translate(tx, ty, point):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])

    translated_point = np.dot(translation_matrix, point)
    return translated_point

def rotate_z(theta_deg, point):
    theta_rad = np.deg2rad(theta_deg)
    rotation_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad), 0],
                                [np.sin(theta_rad), np.cos(theta_rad), 0],
                                [0, 0, 1]])

    rotated_point = np.dot(rotation_matrix, point)
    return rotated_point

# Point P
P = np.array([4, 5, 7])

# Input translation values X and Y
X = float(input("Enter the translation value X: "))
Y = float(input("Enter the translation value Y: "))

# Input angle theta (in degrees)
theta = float(input("Enter the angle of rotation (in degrees): "))

# Perform the successive transformations T.R and R.T
transformed_point1 = rotate_z(theta, translate(X, Y, P))
transformed_point2 = translate(X, Y, rotate_z(theta, P))

# Display the results
print("Result of T.R transformation:", transformed_point1)
print("Result of R.T transformation:", transformed_point2)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the original point P
ax.scatter(P[0], P[1], P[2], color='red', label='Original Point P')

# Plotting the transformed points
ax.scatter(transformed_point1[0], transformed_point1[1], transformed_point1[2], color='blue', label='T.R Transform')
ax.scatter(transformed_point2[0], transformed_point2[1], transformed_point2[2], color='green', label='R.T Transform')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Successive Transformations')

# Set limits for the axes
ax.set_xlim([-30, 30])
ax.set_ylim([-30, 30])
ax.set_zlim([-30, 30])

# Add a legend
ax.legend()

# Show the plot
plt.show()

import numpy as np

def perform_transformation(matrix, point):
    homogeneous_point = np.append(point, 1)  # Convert point to homogeneous coordinates
    transformed_point = np.dot(matrix, homogeneous_point)  # Perform transformation
    return transformed_point[:3]  # Convert back to 3D coordinates

# User input for values of x0, y0, z0
x0 = float(input("Enter x0 value: "))
y0 = float(input("Enter y0 value: "))
z0 = float(input("Enter z0 value: "))

# User input for values of x1, y1, z1
x1 = float(input("Enter x1 value: "))
y1 = float(input("Enter y1 value: "))
z1 = float(input("Enter z1 value: "))

# Transformation matrices T0 and T1
T0 = np.array([[1, 0, 0, x0],
               [0, 1, 0, y0],
               [0, 0, 1, z0],
               [0, 0, 0, 1]])

T1 = np.array([[1, 0, 0, x1],
               [0, 1, 0, y1],
               [0, 0, 1, z1],
               [0, 0, 0, 1]])

# Point P
P = np.array([3, 4, 7])  # Point P

# Perform successive transformations T0.T1 and T1.T0
T0_T1 = np.dot(T0, T1)
T1_T0 = np.dot(T1, T0)

result_T0_T1 = perform_transformation(T0_T1, P)
result_T1_T0 = perform_transformation(T1_T0, P)

# Display the results
print("Results of successive transformations T0.T1 and T1.T0:")
print("T0.T1 * P =", result_T0_T1)
print("T1.T0 * P =", result_T1_T0)

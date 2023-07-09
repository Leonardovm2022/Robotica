import math

def calculate_joint_angles(x, y, phi, l1, l2):

    # Calculate theta1
    theta1 = math.atan2(y, x) + math.acos((x**2 + y**2 + l1**2 - l2**2) / (2 * l1 * math.sqrt(x**2 + y**2)))

    # Calculate theta2
    theta2 = math.acos((x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2))

    # Calculate theta3
    theta3 = phi - (theta1 + theta2)

    # Convert angles to degrees
    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    theta3_deg = math.degrees(theta3)

    return theta1_deg, theta2_deg, theta3_deg

# User input for (x, y) coordinates
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# User input for orientation angle phi
phi_deg = float(input("Enter the orientation angle in degrees: "))
phi = math.radians(phi_deg)

# User input for link lengths
l1 = float(input("Enter the length of the first link: "))
l2 = float(input("Enter the length of the second link: "))

theta1, theta2, theta3 = calculate_joint_angles(x, y, phi, l1, l2)
print("Theta1:", theta1)
print("Theta2:", theta2)
print("Theta3:", theta3)

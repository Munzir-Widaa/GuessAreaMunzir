# Get input from the user for length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate the actual area of the rectangle
actual_area = length * width
# Get the user's guess for the area
user_area = float(input("Enter the area of the rectangle: "))
# Print a message based on whether the user's guess is correct
print("You got the area right!" if user_area == actual_area else f"The actual area is: {actual_area}")
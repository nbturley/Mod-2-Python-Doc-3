# Exercise 2
# Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's 
# circumference or a houses square footage

def squareFoot(length, width):
    area = length * width
    return f"The area of your house is {area}"

def circumference(radius):
    from math import pi
    circum = (2 * pi * radius)
    return f"The circumference of your circle is {circum}"

# answer = True
# while answer:
#     action = input('Do you want to: circle, square, or quit? ')

#     if action.lower() == 'circle':
#         radius = input('What is the radius of your circle? ')
        
#         print(circumference(int(radius)))

#     elif action.lower() == 'square':
#         length = input('What is the length of your house? ')
#         width = input('What is the width of your house? ')

#         squareFoot(int(length), int(width))
#         print(squareFoot(int(length), int(width)))

#     elif action.lower() == 'quit':
#         break
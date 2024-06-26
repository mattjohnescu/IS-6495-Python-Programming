#Class 3, In class exercise 1

#1. 
# Creating a list of color names
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Printing the entire list
print("Colors", colors)

# Printing the length of the list
print("Length of colors:", len(colors))

# Printing the color at index 4
print("Color at index 4:", colors[4])

# Printing a range of colors from index 1 to 5
print("Colors from index 1 to 5:", colors[1:5])

# Printing a range of colors starting from index -3
print("Colors from index -3:", colors[-3:])

# Printing the colors list multiplied by 2
print("Colors list multiplied by 2:", colors * 2)


#2. 
#Changing the color name in element 5
colors[5] = 'indigo'
print("Colors, Change in element 5:", colors)

#Setting element 2 to equal element 4
colors[2] = colors[4]
print("Setting element 2 to equal element 4:", colors)

#Creating a new color list and setting three more color names
new_colors = ["magenta", "cyan", "lime"]

#Concatenating the two lists together
colors_combined = colors + new_colors
print("After concatenating new colors:", colors_combined)

#Setting element 5 of colors_combined to equal the colors variable
colors_combined[5] = colors
print("After setting element 5 to equal colors variable:", colors_combined)



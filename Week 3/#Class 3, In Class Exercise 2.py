#Class 3, In Class Exercise 2
#1 
#Creating the list shapes
shapes = ['square', 'circle']

#Using append to add a triangle
shapes.append('triangle')
print("After appending triangle:", shapes)

#Using insert to add a rectangle at index 1
shapes.insert(1, 'rectangle')
print("After inserting rectangle:", shapes)

#Removing the rectangle
shapes.remove('rectangle')
print("After removing rectangle:", shapes)

#Using del on element 2
del shapes[2]
print("After deleting element at index 2:", shapes)


#2
#Lists to be sorted
ages = [27, 60, 14, 35, 3, 76]
names = ['Quinn', 'John', 'Amber', 'Kim']
stats = [[3, 2], [1, 2], [1, 1], [3, 1]]

#Sorting in numerical order
ages.sort()
print("Ages sorted:", ages)

#Sorting in alphabetical order
names.sort()
print("Names sorted:", names)

#Sorting list of lists in numerical order
stats.sort()
print("Stats sorted:", stats) 



#3
#Given list
numbers = [6, 10, 3, 24, 79, 24]

#Printing the minimum and maximum values from the list
min_value = min(numbers)
max_value = max(numbers)

min_value, max_value




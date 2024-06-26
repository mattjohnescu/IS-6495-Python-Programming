#Week 7, Exercise 2
#1
#Define the simplest class with pass statement
class Simplest():
    pass

#Create an instance of Simplest
simp = Simplest()

#Check the types of both Simplest and its instance simp
simplest_type = type(Simplest)
simp_type = type(simp)

print("Type of Simplest:", simplest_type)
print("Type of simp:", simp_type)


#2
#making function
class Person:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def format_name(self):
        # Assuming the format "First Middle Last"
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
#Create an instance of the Person class
person_instance = Person("John", "Quincy", "Adams")

#Call the format_name() function and print the result
print(person_instance.format_name())


#3

import math

class Cylinder:
    def __init__(self):
        self.height = 0
        self.radius = 0

    def set_height_radius(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        # Volume formula: height * pi * radius^2
        return self.height * math.pi * (self.radius ** 2)

    def surface_area(self):
        # Surface area formula: 2*pi*radius*(radius + height)
        top_area = math.pi * (self.radius ** 2)
        return 2 * top_area + (2 * math.pi * self.radius * self.height)


mycyl = Cylinder()
mycyl.set_height_radius(2,3)
print(mycyl.volume())

print(mycyl.surface_area())





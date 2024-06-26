#Homework 7
#1
import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name  # Person's name.
        self.surname = surname  # Person's surname.
        self.birthdate = birthdate  # Person's birthdate.
        self.address = address  # Person's address.
        self.telephone = telephone  # Person's telephone.
        self.email = email  # Person's email.

    def age(self):
        today = datetime.date.today()  # Today's date.
        age = today.year - self.birthdate.year  # Initial age based on year difference.
        # Adjusting the age if the birthday hasn't occurred yet this year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age  # Calculated age.

# Creating an instance of Person
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # Birthdate in the format year, month, day.
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

# Printing the name, email, and age of the person
print(person.name)  # Accesses the 'name' attribute.
print(person.email)  # Accesses the 'email' attribute.
print(person.age())  # Calls the 'age' method.


#2
import datetime

class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self._age = None
        self._age_last_recalculated = None
        self.recalculate_age()
        
    def recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        self._age = age
        self._age_last_recalculated = today
        
    def age(self):
        if datetime.date.today() > self._age_last_recalculated:
            self.recalculate_age()
        return self._age

    
#3
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

#instance and test
square = Square(4)
print(square.area())

#different value and test again
square.side = 5
print(square.area())


#4
#instance
person_instance = Person("Jane", "Doe", datetime.date(1992, 3, 12), "Address", "Phone", "Email")

#dir and vars
print(dir(person_instance))
print(vars(person_instance))

# __str__ method and type
print(person_instance.__str__())
print(str(person_instance))
print(type(person_instance))
print(type(Person))

#Function to print custom attributes
def print_attributes(obj):
    for attr, value in vars(obj).items():
        print(f"{attr}: {value}")

print_attributes(person_instance)



#5 
class Reverser:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

# Test
reverser = Reverser()
print(reverser.reverse_words("Hello World"))


#6
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

#Test
circle = Circle(5)
print(circle.area())
print(circle.perimeter())


#7
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#Test
rectangle = Rectangle(4, 5)
print(rectangle.area())

#8 
import math

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #Calculate the distance between the two points
        #using the distance formula
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def slope(self):
        #Calculate the slope of the line
        #using the slope formula
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

#output:
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())  
print(li.slope())  

#9
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else: 
        result = 3 * number + 1
        print(result)
        return result

try:
    n = int(input("Give me a number: "))  
    while n != 1:
        n = collatz(n)
except ValueError:
    print("Please enter an integer.")
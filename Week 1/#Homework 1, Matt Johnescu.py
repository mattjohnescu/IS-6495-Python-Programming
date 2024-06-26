#Homework 1, Matt Johnescu

#Exercise 1: Basic Math Operations (2 points)
#Use the Python print function to perform basic calculations with four different math symbols. Provide four statements using addition, subtraction, multiplication, and division.
#Example: print(2+2)

print(2+2)
print(3-3)
print(4*4)
print(5/5)


#Exercise 2: Fruits in a Basket (2 points)
#Use the print function to display the names of four different fruits in one statement, such as "peaches," "grapes," "mangoes," and "strawberries."

print("apple")
print("banana")
print("star fruit")
print("pineapple")

#Exercise 3: Greeting Message (2 points)
#Create two variables called your_first_name and your_last_name, and assign your first and last names to them, respectively. Using the print function in Python, display the following message in one line:
#Nice to meet you, I am YourFirstName YourLastName.

your_first_name = "Matt"

your_last_name = "Johnescu"

print("Nice to meet you, I am", your_first_name, your_last_name,".")


#Exercise 4: Area of a Rectangle (2 points)

#Create two variables to represent the length and width of a rectangle. Assign them any numerical values. Calculate the area of the rectangle (Area = length * width) and store the result in a third variable. Use the print function to display the area.

length = 4

width = 5 

Area = length * width

print(Area)


#Exercise 5: Pay Calculation with Hours and Minutes (2 points)
#Create two variables to hold values for hourly wage and minutes worked for a project.
#Assign hourly_wage = 22 and minutes_worked = 390.
#Calculate the total hours worked (note that 1 hour = 60 minutes) and then calculate the total pay.
#Using the print function, display the pay results with a dollar sign before the value. (For example, $126)

hourly_wage = 22

minutes_worked = 390 

hours_worked = minutes_worked / 60

final_pay = hours_worked * hourly_wage

print("Final pay is $",final_pay)
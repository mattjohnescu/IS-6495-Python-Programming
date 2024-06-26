# Week 7, Exercise 1
#1
#Temp conversions

from ICE import fahrenheit_to_celsius, celsius_to_fahrenheit

# Test the conversion functions
print(f"32°F is {fahrenheit_to_celsius(32):.2f}°C")
print(f"0°C is {celsius_to_fahrenheit(0):.2f}°F")


#2 
from ICE import NullToBooleanConverter

#non-null variable
non_null_variable = "Hello, World!"
print(NullToBooleanConverter(non_null_variable))

#null variable
null_variable = None
print(NullToBooleanConverter(null_variable))


#3
import random
from ICE import getAnswer

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Pass the number into the getAnswer function and print the fortune
fortune = getAnswer(random_number)
print(f"Your fortune: {fortune}")


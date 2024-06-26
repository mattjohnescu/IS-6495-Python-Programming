#Class 2 code along 3

import random

num1 = random.randint(0,10)
num2 = random.randint(0,10)


answer = int(input(f"What is the sum of {num1} and {num2}?"))

num_sum = num1 + num2

if answer == num_sum:
    print("Correct")

while answer != num_sum:
    print("False")
    answer = int(input(f"What is the sum of {num1} and {num2}?"))

    if answer == num_sum:
        print("Correct")5
        



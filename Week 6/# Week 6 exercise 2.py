# Week 6 exercise 2
#Exercise 2
#1
def divide_numbers(num1, num2):
    try:
        #Attempt to divide the numbers
        result = num1 / num2
    except ZeroDivisionError:
        #Handle divide by zero errors
        print("invalid argument")
        return None
    else:
        #Return the result if division was successful
        return result

#Test the function with divide by zero example
test_result = divide_numbers(10, 0)
print("Result:", test_result)

#Test the function with valid arguments
valid_test_result = divide_numbers(10, 2)
print("Result:", valid_test_result)

#2
#Handle the exception in the code
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Error: Operation not supported between instances of str and int")

    
#3
#Handle the exception in the code
try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("All Done.")


#4
def ask_for_integer():
    while True:
        try:
            #Ask for an integer from the user
            value = int(input("Input an integer: "))
        except ValueError:
            #Handle non-integer inputs
            print("An error occurred! Please try again!")
        else:
            #If an integer was successfully inputted, print its square
            print("Thank you, your number squared is:", value ** 2)
            break  #Exit loop after successfully squaring the number



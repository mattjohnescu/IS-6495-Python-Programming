#Week 5, Exercise 2
#Function Arguments and Variables
#2.1 
def sum_of_numbers(num_list):
    return sum(num_list)

#list of numbers
numbers = [10, 20, 30, 40, 50]

#result
the_sum = sum_of_numbers(numbers)
print(the_sum)


#2.2
def raise_to_power(num1, num2):
    return num1 ** num2

#Using the function
result = raise_to_power(2, 3) 
print(result) 


#2.3
def price_with_tax(price):
    tax_rate = 0.07  
    total_price = price * (1 + tax_rate)  #Calculate total price including tax
    return total_price

#usage
total_price = price_with_tax(100)
print(total_price)


#2.4
def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3) / 3

#usage 
average_of_three(10,3,4)

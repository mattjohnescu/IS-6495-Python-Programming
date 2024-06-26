#Homework 2 Intro to Python
#2.1. 
def identify_coin(coin_value):
    #Adding coin values to coin names:
    coin_names = {1: "Penny", 5: "Nickle", 10: "Dime", 25: "Quarter", 50: "Half dollar"}
    
    #Determining coin type based on the entered value:
    coin_type = coin_names.get(coin_value, None)
    
    #Return the result
    if coin_type:
        return f"That is a {coin_type}!"
    else:
        return "That is not a valid coin!"

if __name__ == "__main__":
    #User Input code
    coin_value = int(input("Enter a Coin Value: "))
    
    #User output code
    result = identify_coin(coin_value)
    print(result)

#2.2
#User input Code
value_entered = int(input("Enter an Integer:"))

#Code checking multiples
if value_entered % 3 == 0 and value_entered % 4 == 0:
    print("The number is a multiple of both 3 and 4.")
elif value_entered % 3 == 0:
    print("The number is a multiple of 3.")
elif value_entered % 4 == 0:
    print("The number is a multiple of 4.")
else:
    print("The number is neither a multiple of 3 nor 4.")


#2.3.
#User Input Code: 
user_input = int(input("What is your age?"))

#Function giving different message depending on input age.
if user_input <= 0:
    print("Please enter a valid age greater than 0.")
elif user_input >= 65:
    print("You receive a 30 percent discount.")
elif user_input >= 18:
    print("You get a 15 percent discount.")
else:
    print("You are not eligible for a discount.")

#2.4
#User Input Code:
starting_number = int(input("Enter a starting number: "))
ending_number = int(input("Enter an ending number: "))
even_or_odd = input("Even or Odd?: ").lower()  #Helps to convert input to lower case

#Check and print numbers from User choice:
for number in range(starting_number, ending_number + 1):
    if even_or_odd == "even" and number % 2 == 0:
        print(number)
    elif even_or_odd == "odd" and number % 2 != 0:
        print(number)


#2.5
#User Input Code:
no_of_products = int(input("Enter the number of products: "))

#Starting total cost:
total_cost = 0  

#Loop to ask for the price of each product and add it to the total:
for product_number in range(1, no_of_products + 1):
    price = float(input(f"Enter price for product # {product_number}: "))
    total_cost += price  #Accumulate the total cost

#Print the total cost:
print(f"\nTotal cost: {total_cost}")


#2.6
while True:
    #User Input code
    book_price = float(input("What is the book price? "))

    #Calculate and print the discounted price
    discounted_price = book_price * 0.9  # Apply a 10% discount
    print(f"The discounted price is: {discounted_price}")

    #Ask if the user wants to enter another price
    another = input("Do you want to enter another price? (yes/no): ").lower()
    
    #Break the loop if the user does not want to enter another price
    if another != "yes":
        break


#2.7
#Initialize the total amount spent
total_spent = 0 
#Initialize the total saved from discounts
total_saved = 0  

while True:
    #User Input code
    book_price = float(input("What is the book price? "))

    #Calculate the discounted price and the amount saved
    discount_amount = book_price * 0.1  # 10% discount
    discounted_price = book_price - discount_amount
    
    #Update totals
    total_spent += discounted_price
    total_saved += discount_amount

    print(f"The discounted price is: {discounted_price}")
    print(f"You saved: {discount_amount} on this book.")

    #Ask if the user wants to enter another price
    another = input("Do you want to enter another price? (yes/no): ").lower()
    
    #Break the loop if the user does not want to enter another price
    if another != "yes":
        break

#After exiting the loop, print the totals
print(f"Total amount spent: {total_spent}")
print(f"Total saved from discounts: {total_saved}")


#2.8
#Set country and its capital
country = "France"
capital = "Paris"

#Continually ask the user for the capital until they get it right
while True:
    user_guess = input(f"What is the capital of {country}? ")
    if user_guess.strip().lower() == capital.lower():
        print("Correct!")
        break
    else:
        print("That's not correct, try again.")


#2.9
import random

#Generate 2 random numbers
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

#Enter while loop
while True:
    # Prompt user
    user_answer = int(input(f"What is {num1} + {num2} equal to? "))
    
    #Check answer
    if user_answer == num1 + num2:
        print("Correct!")
        break  #Exit the loop
    else:
        print("Incorrect, try again.")


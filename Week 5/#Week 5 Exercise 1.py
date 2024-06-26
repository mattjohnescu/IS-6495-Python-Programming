#Week 5 Exercise 1
#Basic Functions: 

#1.1
def greet_me():
    name = input("What is your name?")
    print("Hello,", name)
    
#Call Function:
greet_me()

#1.2
def dog_age_in_dog_years():
    age_input = input("What is your dog's age in human years? ")  #Ask for the dog's age in human years
    age_human_years = int(age_input)  #Convert input to int
    age_dog_years = age_human_years * 7  #Convert human years to dog years
    print(f"Your dog's age in dog years is: {age_dog_years}")
    

#Call function 
dog_age_in_dog_years()


#1.3
def get_purchase_quantity():
    quantity_input = input("Enter the number of items you wish to purchase: ")  #Ask for number of items
    quantity = int(quantity_input)  #Convert the input to an int
    print(f"You have chosen to purchase {quantity} item(s).")


#Call function 
get_purchase_quantity()
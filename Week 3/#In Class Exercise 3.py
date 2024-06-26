#In Class Exercise 3
#1
#Prompt the user, ask how many numbers to add
quantity = int(input("How many numbers do you want to add? "))

#Initialize a total variable to zero
total = 0

#Enter for loop
for i in range(quantity):
    #Prompt user: Enter a number to add
    number = int(input("Enter a number to add: "))
    #Add number from input to the total
    total += number
#End for loop
#Print the total
print("the total is", total)


#2
#Prompting user for a word or phrase
user_input = input("Enter a word or sentence: ")
total = 0

#Entering 'for' loop to count vowels
for letter in user_input:
    # Checking if the letter is a vowel using the 'or' operator with proper comparisons
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        total += 1

#Printing total results
print(f"The total number of vowels is:",total)



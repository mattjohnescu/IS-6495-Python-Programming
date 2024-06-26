# Week 6 Exercise 1
#Exercise 1 
#1
def format_full_name(first_name, last_name, middle_initial):
    #Capitalize the first letter of each name
    first_name_title = first_name.title()
    last_name_title = last_name.title()
    middle_initial_title = middle_initial.upper()  # Middle initials capitalized

    #Format and return the full name using .format()
    return "{0} {1}. {2}".format(first_name_title, middle_initial_title, last_name_title)

#Example usage
formatted_name = format_full_name("john", "doe", "c")
formatted_name

#2
#Print the phrase with an escape character
print("Welcome to O\'Neil\'s Boat Rentals!")

#Initialize the string variable
sentence = "Hello there! How are you? I\'m doing fine."

#Print the sentence with newline characters to format the output as required
print("\n" + sentence.replace("? ", "?\n"))

#3
#Initialize the string variable
my_string = "hello python"

#Print the string in all uppercase
print(my_string.upper())

#4
#Example first and last name
first_name = "John"
last_name = "Doe"

#Combine the names with the * symbol and ensure the total length is max 25 characters
full_name_with_stars = "*{0} {1}*".format(first_name, last_name).center(25, '*')

#Print name
print(full_name_with_stars)   



#5 
#Define name
full_name = "Matt"

#Define the symbol to use
symbol = "*"

#calculate the maximum name length, subtracting the length of the symbols from the total allowed length.
max_name_length = 25 - 2 * len(symbol)  #Subtracting the length of two symbols from the total length

#Ensure the name is trimmed to the maximum allowed length before adding symbols
trimmed_name = full_name[:max_name_length]

#Create the final string
final_string = f"{symbol}{trimmed_name}{symbol}"

final_string
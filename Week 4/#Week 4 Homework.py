#Week 4 Homework
#1
#dictionary of items
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments': 3}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, amount in inventory.items(): 
        print(f"{amount} {item}")
        item_total += amount 
    #Print the total number of items
    print("Total number of items:", item_total)

#function with the inventory
display_inventory(stuff)

#2
#list of characters
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]

def list_to_string(char_list):
    #Join all items in a list into a string, with ', ' as separator except for the last item
    if len(char_list) == 1:
        #Only one item in the list, return it as string
        return char_list[0]
    else:
        #Join all items using ', ' but for the last item use 'and '
        return ', '.join(char_list[:-1]) + ' and ' + char_list[-1] + '.'

#Convert the list to a string
characters_string = list_to_string(characters)
characters_string

#3
#Dictionary of technical terms
tech_terms = {
    'dict': 'stores a key/value pair',
    'list': 'stores a value at each index',
    'map': 'see dict',
    'set': 'stores unordered unique elements',
    'exit': 'type "exit" to end the program'
}

#Function to lookup definitions
def lookup_definitions(terms):
    while True:
        user_input = input("Enter a term ('exit' to end): ").strip().lower()  #input from user
        if user_input == 'exit':
            print("Exiting the program.")
            break  #Exit the loop if user types 'exit'
        elif user_input in terms:
            print(f"{user_input} = {terms[user_input]}")  #Print the definition if the term is in the dictionary
        else:
            print("Term not found. Please try another.")  #Tell user if the term is not found

#Call the function to start the lookup
lookup_definitions(tech_terms)

#4
set("Mississippi")

#5
# Given nested list
list1 = [1, 2, [3, 4, "hello"]]

#Reassign "hello" to "goodbye"
list1[2][2] = "goodbye"

list1  #Return the list to show change

#6a
d = {'simple_key':"hello"}
hello_6a = d['simple_key'] 

#6b
d = {"k1":{"k2":"hello"}}
hello_6b = d['k1']['k2']  
# Week 6 Exercise 3 

#Exercise 3
#1
def verify_integer_input():
    while True:
        try:
            #Request input from user
            user_input = input("Please enter a number: ")
            #Attempt to convert the input to an integer
            number = int(user_input)
        except ValueError:
            #If conversion fails, report error and prompt again
            print("That's not a valid number. Please try again.")
        else:
            #If conversion succeeds then confirm valid input and exit the loop
            print("Thank you for entering a valid number:", number)
            break  #Exit the loop


#2
#Define the file name
file_name = "/mnt/data/example_file.txt"

#Open the file with write mode ('w')
with open(file_name, 'w') as file:
    #Write a few lines of text to the file
    file.write("This is the first line of text.\n")
    file.write("Here is another line of text.\n")
    file.write("The file will be overwritten each time this program runs.\n")



#3
def print_file_contents():
    #Ask the user for a file name
    file_name = input("Please enter a file name: ")

    try:
        #Attempt to open file
        with open(file_name, 'r') as file:
            #Print each line
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        #Handle case where the file does not exist
        print(f"The file {file_name} was not found.")



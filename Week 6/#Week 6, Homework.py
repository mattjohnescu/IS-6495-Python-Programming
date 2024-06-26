#Week 6, Homework
#1. 
#Try to open and read the file
try:
    #Open the file for reading
    with open("most_popular_words_in_english.txt", "r") as file:
        #Read the entire content of the file
        content = file.read()
        #Print the content
        print(content)
        
        #Split the content by line breaks to get a list of words
        popular_words = content.split('\n')
        
        #Ask the user to input a word
        user_word = input("Please type in a word in English: ").strip().lower()
        
        #Check if the user's word is in the list of popular words
        if user_word in popular_words:
            print(f"'{user_word}' is one of the most 100 popular English words.")
        else:
            print(f"'{user_word}' is not one of the most 100 popular English words.")

#Handle the case where an error occurs
except Exception as e:
    print("Something went wrong!", str(e))


#2. 
#Ask the user for a username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

#Open the file "security.txt" in write mode
try:
    with open("security.txt", "w") as file:
        #Write the username and password to the file on separate lines
        file.write(username + '\n')
        file.write(password)
    print("Username and password have been securely stored.")
except Exception as e:
    print("An error occurred while trying to write the file:", str(e))


#3. 
#Function to read the stored username and password
def read_credentials():
    try:
        with open("security.txt", "r") as file:
            #Read the username and password from the file
            stored_username = file.readline().strip()  #Removes the newline character
            stored_password = file.readline().strip()
        return stored_username, stored_password
    except FileNotFoundError:
        print("Security file not found. Please ensure 'security.txt' exists.")
        exit()  #Exit the program
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

#Read credentials
stored_username, stored_password = read_credentials()

#Prompt the user
user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

#Check if the provided credentials match the stored credentials
if user_username == stored_username and user_password == stored_password:
    print("Access granted. Welcome!")
else:
    print("Error: The provided username or password is incorrect. Access denied.")


#4. 
#Open the file
try:
    with open("testscores.txt", "r") as file:
        lines = file.readlines()  #Read all lines in file

    #Initialize variables to store the student's name and total score, and a counter for the number of scores
    student_name = None
    total_score = 0
    score_count = 0

    #Use a for loop
    for line in lines:
        if student_name is None:
            #The first line is the student's name
            student_name = line.strip()
        elif line.strip().isnumeric():  #Ensure the line contains a number with is numeric
            #Add the score to the total and increment the score count
            total_score += int(line.strip())
            score_count += 1

    #Calculate the average score
    if score_count > 0:
        average_score = total_score / score_count
        #Print out the student's name and their average score
        print(f"{student_name}'s average score: {average_score:.2f}")
    else:
        print("No scores found.")

except FileNotFoundError:
    print("The file 'testscores.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


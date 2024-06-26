#Week 5 Homework
# Exercise 1
def topOrBottom():
#Prints the top or bottom line of the pattern.
    print("#####")

def hollowSpace():
#Prints the hollow space with borders of the pattern.
    print("#     #")

def diamond():
#Prints the diamond shape in the middle of the pattern.
    print(" #   #")
    print("  # #")
    print("   #")
    print("  # #")
    print(" #   #")

def printPattern():
#Assembles the full pattern using the functions
    topOrBottom()    #Top line
    hollowSpace()    #Hollow space
    diamond()        #Diamond shape
    hollowSpace()    #Hollow space
    topOrBottom()    #Bottom line

#print the pattern
printPattern()



#Exercise 2
def feet_to_inches(feet):
    #Converts Feet to inches
    inches = feet * 12
    print(f"... {inches} inches")

def feet_to_meters(feet):
    #Converts feet to meters
    meters = feet * 0.3048
    print(f"... {meters} meters")

def generate_output():
    #Generates output from conversion functions
    for feet in range(10):  # Looping from 0 to 9 feet
        print(f"{feet} ft:")
        feet_to_inches(feet)
        feet_to_meters(feet)

#Run program
generate_output()


#Exercise 3
import random

def roll_two_dice(max_sides):
#Rolls two dice with sides ranging from 1 to max_sides and returns the results in ascending order
    roll1 = random.randint(1, max_sides)
    roll2 = random.randint(1, max_sides)
    return sorted([roll1, roll2])

#Program to roll 5 sets of dice with different sides
for sides in range(6, 11):  #From 6-sided to 10-sided dice
    roll_result = roll_two_dice(sides)
    print(f"{sides} sided dice roll: {roll_result[0]} & {roll_result[1]}")

    
#Exercise 4
#Guess the number game.
import random

#random.randint() function to generate a random number between 1 and 20.
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())  #Convert input to an integer
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        #This condition is the correct guess!
        break

if guess == secretNumber:
    print(f'Good job! You guessed my number in {guessesTaken} guesses!')
else:
    print(f'Nope. The number I was thinking of was {secretNumber}.')

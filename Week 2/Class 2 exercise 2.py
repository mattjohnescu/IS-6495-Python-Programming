#1
password = "Utes123"
x = input("Enter your password")


if (x == password):
    print("Access Granted")
else:
    print("Acces Denied")


#2

voting_age = "18"
x = input("What is your age?")
if (x >= voting_age):
    print("You can vote")
else:
    year_left = voting_age - x
    print("You can vote in", year_left, "years.")


#3

temp = int(input("What's the temperature outside?"))

if (temp < 40): 
    print("Wear a warm coat")
elif (temp < 70):
    print("wear a light jacket")
elif (temp < 100):
    print("wear something cool")
elif (temp > 100):
    ac = input("Do you have air conditioning at home?")
    if ac == "yes":
        print("Stay at home")
    if ac == "no":
        print("Bummer, try a swimming pool.")














#code along 1

"""
Multi-line comments using the triple quote

"""
#3 strings
a = "100" 
b = "50.75"
c = "-3.2"

d = int(a)
e = float(b)
f = float(c)

answer = a+b+c
print(answer)

answer = d+e+f
print(answer)


user_age = input("What is your age? ")
user_name = input("What is your name? ")
print("Welcome to my program", user_name)
print("You are", user_age, "years old.")

#money sing but it has a space 
print("$", answer)
#printing money sign without space
print("$" + str(answer))
#formatting dollar sign - new method 
print(f"${answer}")



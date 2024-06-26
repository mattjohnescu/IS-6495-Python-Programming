#Week 5 Code Along 2
def format_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(format_name("Matt", "Johescu"))


first = input("What is your first name?")
last = input("What is your last name")
print("Hello", format_name(first, last))



#Function adding numbers and finding average
def average(*args):
    pooop = sum(args)
    avg = format(pooop / len(args), ".2f")
    print(avg)

average(4,12,3,8,7,5,4,3,3,2,2,3,200000000000000000000000000000000000)

def func(num1, num2 = 2):
    if num1 < 0:
        return
    else:
        return num1 + num2
    
print(func(1,4))


# *args
# **kw args

def multiply_by(a, b=2):
    return a * b

print(multiply_by(5))
print(multiply_by(5, 5))






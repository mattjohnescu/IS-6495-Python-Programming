

# = assigning 
# == somthing is equal to 
# != is NOT equals
# and - Represents two tru values 
# or - Represents one value or the other 
# and not - represents one value and not another value 

# Week 2, Code along 2
a = True 
b = False

print(a == b)
print( a != b)
print(a != b)
print(a and b)
print(a or b)
print(not a)


print("break from first trail")
print (True)
print(1 == 1)
print (1 == 2)
print(1 != 1)
print(1 < 2)
print(1 > 2 and 2 < 5)
print(1 > 2 or 2 < 5)
print(not 1 > 2 and 2 < 5)


# part 2 
#One-way condiiton
x = 5 
if x > 0:
    print("x is positive")
    
print("This line will always run")

#2-way condiiton 

x = -1 
if x > 0:
    print("positive")
else:
    print("negative")

print("this will always print")

#multi-way condition
x = -1 
if x > 0:
    print("positive")
elif x == 0:
    print("x is zero")
else:
    print("negative")



x = int(input("Enter a number: "))
#nested condiitons: 
if x > 0:
    print("positive")

    if x % 2 == 0:
        print("x is even")  
    else:
        print("x is odd")
else: 
    print("x is not positive")

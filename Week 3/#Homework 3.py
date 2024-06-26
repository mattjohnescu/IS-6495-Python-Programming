#Homework 3

#1. 
grades = [90, 100, 70, 45, 76, 84, 93, 21, 36, 99, 100]

#Counters for each grade category
count_A = count_B = count_C = count_D = count_F = 0

#Gach grade in the list
for grade in grades:
    if 90 <= grade <= 100:
        count_A += 1
    elif 80 <= grade < 90:
        count_B += 1
    elif 70 <= grade < 80:
        count_C += 1
    elif 60 <= grade < 70:
        count_D += 1
    else:
        count_F += 1

# Print the counts for each grade category
print(f"Count of A's: {count_A}")
print(f"Count of B's: {count_B}")
print(f"Count of C's: {count_C}")
print(f"Count of D's: {count_D}")
print(f"Count of F's: {count_F}")


#2. 
grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]

#Apply the curve to each score
curved_grades = []
for score in grades:
    if score >= 90:
        curved_grades.append(score)  #No curve needed
    elif 80 <= score < 90:
        curved_grades.append(score + 2)  #Add 2 points
    elif 70 <= score < 80:
        curved_grades.append(score + 5)  #Add 5 points
    else:
        curved_grades.append(score + 8)  #Add 8 points

#Print out the new grades
print("Original grades:", grades)
print("Curved grades:", curved_grades)


#3. 
#Initialize an empty list to store sales
weekly_sales = []

#Days of the week for reference
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Loop through each day of the week
for i in range(7):
    #Prompt the user for sales input
    sales = input(f"Enter sales for {days_of_week[i]}: ")
    #Append the sales input (converted to an integer) to the weekly_sales list
    weekly_sales.append(int(sales))

#Print out the sales for the week
print("\nSales for the week:", weekly_sales)


#4. 
#Initial list
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#Extract the first 3 elements
first_three = my_list[:3]

#Extract the characters b, c, and d
bcd = my_list[1:4]

#Extract the last 4 characters
last_four = my_list[-4:]

#Print the results
print("First 3 elements:", first_three)
print("Characters b, c, and d:", bcd)
print("Last 4 characters:", last_four)


#5. 
#List of products in inventory
products = ["apple", "pear", "peach", "banana"]

#Prompt the user to type in the name of a product
product_name = input("Type in the name of a product to check if it is in our inventory: ")

#Convert the user input to lowercase and check if it exists in the inventory
if product_name.lower() in [product.lower() for product in products]:
    print("The product is in our inventory.")
else:
    print("The product is not found.")


#6. 
#Define the two lists
a = [1, 2, 3, 4, 5]
b = [2, 3, 10, 11, 12, 1]

#Find common elements using list comprehension
common_elements = [element for element in a if element in b]

#Print the result
print(common_elements)


#7. 2
#Initialize an empty list to store first names
first_names = []

while True:
    #Prompt the user to enter a first name
    name = input("Enter a first name (type 'end' to stop): ")
    
    #Check if the input is "end" to break the loop
    if name.lower() == "end":
        break
    
    #Add the name to the list if it's not already present (to prevent duplicates)
    if name not in first_names:
        first_names.append(name)
    else:
        print("This name has already been entered. Please enter a different name.")

#Print out the list of entered first names
print("First names entered:", first_names)


#8. 
#Initial inventory list
products = ["apple", "pear", "peach", "banana"]

while products:  #Continue as long as there are products in the list
    #Prompt the user for a product name
    product_name = input("Enter a product name (type 'end' to stop): ")
    
    #Check if the user wants to end the program
    if product_name.lower() == "end":
        break
    
    #Check if the product is in the inventory list
    if product_name in products:
        # Remove the product from the list
        products.remove(product_name)
        print("Product removed. Current list of products:", products)
    else:
        #Inform the user that the product is not in the inventory
        print("We do not currently carry the product in question.")
    
    #If the list becomes empty, end the program
    if not products:
        print("All products have been removed. Ending program.")
        break


#9. 
#Lists of products and their corresponding prices
products = ['peanut butter', 'jelly', 'bread']
prices = [3.99, 2.99, 1.99]

#Prompt the user to enter a product name
product_name = input("Enter a product: ")

#Check if the entered product is in the products list
if product_name in products:
    #Find the index of the product
    index = products.index(product_name)
    #Retrieve the corresponding price using the index
    price = prices[index]
    #Display the price to the user
    print(f"This product costs {price}")
else:
    #Inform the user if the product is not found
    print("Product not found.")


#10.
#Ask the teacher for the number of students and assignments
num_students = int(input("How many students in the class? "))
num_assignments = int(input("How many assignments in the class? "))

#Iterate over each student
for student in range(1, num_students + 1):
    print(f"\nStudent #{student}")
    total_score = 0  # Initialize total score for each student
    
    #Iterate over each assignment for the current student
    for assignment in range(1, num_assignments + 1):
        score = float(input(f"Assignment #{assignment}: "))
        total_score += score  #Add score to total
    
    #Calculate and print the average score for the current student
    average_score = total_score / num_assignments
    print(f"Student #{student} earned a {average_score:.2f}")




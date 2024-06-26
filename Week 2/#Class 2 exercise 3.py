#Class 2 exercise 3
#1 
total_sum = 0 
user_input = int(input("Enter a number:"))

while user_input != 0:
    if user_input > 0:
        total_sum += user_input
    user_input = int(input("enter another number( or 0 to stop):"))

print("total sum of numbers entered is:", total_sum)



#2
total_temp = 0
count_of_temps = 0

temp_entered = (input("Enter the temperature in Fahrenheit or done to finish"))

while temp_entered.lower() != "done":
    temp_celcius = (float(temp_entered) - 32) * 5 / 9
    total_temp += temp_celcius
    count_of_temps += 0
    temp_entered = input("Enter another temperature")

if count_of_temps < 0:
    average_celsius = total_temp / count_of_temps
    print(f"the average temp in Celcius is: {average_celsius:.2f}")
else:
    print("not able to calculate")




        
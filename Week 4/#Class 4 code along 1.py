#Class 4 code along 1
#Week 4, Exercise 1

my_numbers = "10 20 30 40 50 60"
print(my_numbers)

number_list = my_numbers.split()
print("after splitting")
print(number_list)
print("before splitting")
print(my_numbers)
print(type(my_numbers))
print(type(number_list))

int_list = [int(x) for x in my_numbers.split()]
print(int_list)
print(type(number_list))
print(len(number_list))

my_csv = "Scooby Doo, Harry Potter, Darth Vader, Bugs Bunny, Captain America"
print(my_csv)
print(type(my_csv))
str_list = my_csv.split(",")
print(str_list)
print(str_list[1])

my_time = "10:05:45, 09:45:32, 07:30:25"
time_list = my_time.split(",")
print(time_list)
for item in time_list:
    time = item.split(":")
    print(time)

time = "07:49:34"
hrs, mins, sec = time.split(":")
print(hrs, mins, sec)
print(type(hrs))
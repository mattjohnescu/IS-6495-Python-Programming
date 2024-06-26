#Class 3 Code Along 1

empty_list = []

#making list
my_list = [45, 3.2, "Marvel", 17, -4]

#printing list with index 2 
print(my_list[2])

#printing whole list 
print(my_list)

#making new list
second_list = [100,101]
print("Second List", second_list)

second_list = second_list* 2
print(second_list)

big_list = my_list + second_list
print("Big List", second_list)

#chracters list
characters = ["Thor", "Spider_man", "Super Man", "Adam", "Ironman", "Captain AMerica"]
print(characters)
print(len(characters))
#partitioing data
print(characters[2])
#characters 1 and 2
print(characters[1:3])
print(characters[1:5])
#going backwards in data
print(characters[-3])
#prints characters twice
print(characters * 2)
#every third character
print(characters[::3])
#index of list and string
print(characters[2][-1])


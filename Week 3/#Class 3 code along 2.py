#Class 3 code along 2
my_list = ["Christine", "Jack", "Renae", "Jeff"]
my_list.append("Jeff")
print(my_list)
del my_list[1]
print(my_list)


#pop example
pop_list = [4,3,5]
item = pop_list.pop(1)
print(pop_list)
print(item)

#reverse function 
pop_list.reverse()#permanently modifies list
print(pop_list)

#printing the location of a variable 
location = my_list.index("Jeff")
print(location)


#Prices list
prices = [3.99,2.99,1.99,4.99,0.99,0.99]
biggest_num = max(prices)
smallest_num = min(prices)
print(smallest_num, "up to", biggest_num)

#inserting something into the list 
prices.insert(1,6.99)
print(prices)

#remove function 
prices.remove(0.99)
print(prices)

#sort function
prices.sort()
print(prices)

#reverse function
prices.sort(reverse=True)
print(prices)
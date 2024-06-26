#Week 4, Exercise 2
#1.1
#Making a birthday dictionary
birthday_dict = {
    "Alice": "1992-04-12",
    "Bob": "1985-11-23",
    "Carol": "1978-02-05",
    "Dave": "1990-07-14"
}
#Print each birth date by using the key to access each entry
for name in birthday_dict:
    print(f"{name}'s birthday is {birthday_dict[name]}")
    
    
#1.2
#Updating last entry
birthday_dict["Dave"] = "1980-06-06"

#Print the updated dictionary to confirm the change
for name in birthday_dict:
    print(f"{name}'s updated birthday is {birthday_dict[name]}")
    
#1.3
# Creating a dictionary of seasons
seasons_dict = {
    "Fall": ["September", "October", "November"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}

# Print the value of "Fall"
print("Months in Fall:", seasons_dict["Fall"])


#1.4
#Creating a second dictionary with only winter
winter_dict = {
    "Winter": ["December", "January", "February"]
}

#Using dictionary.update 
seasons_dict.update(winter_dict)

#Print the updated seasons dictionary
print("Updated seasons dictionary:", seasons_dict)


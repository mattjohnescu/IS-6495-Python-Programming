#4.1
#First string
string_with_spaces = '10 67 123 46 20 18 36 250'
list_of_numbers_spaces = string_with_spaces.split()
print("List from space-separated string:", list_of_numbers_spaces)

#Second string
string_with_commas = '10,67,123,46,20,18,36,250'
list_of_numbers_commas = string_with_commas.split(',')
print("List from comma-separated string:", list_of_numbers_commas)


#4.2
#String with commas as separators
string_with_numbers = '90,67,87,102,77,80'

#Split the string and create list of numbers
list_of_numbers = string_with_numbers.split(',')

#Convert each string and sum them
sum_of_numbers = sum([int(number) for number in list_of_numbers])

#Print the sum
print("Sum of the numbers:", sum_of_numbers)


#4.3
#Given list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Use slicing to get the first 4 numbers
first_four_numbers = numbers_list[:4]

#Print the results
print("First 4 numbers:", first_four_numbers)

#4.4
#Given list of letters
letters_list = ['a', 'b', 'z', 'd', 'e', 'f', 'x']

#Use slicing to get every other entry, starting at the beginning
every_other_entry = letters_list[::2]

#Print
print("Every other entry:", every_other_entry)
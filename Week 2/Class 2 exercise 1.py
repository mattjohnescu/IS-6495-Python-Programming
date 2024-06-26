#question 1
fruit_cost = input("What is the cost of fruit? ")
Vegetables_cost = input("What is the cost of vegetables? ")
meat_cost = input("What is the cost of meat? ")
dairy_cost = input("What is the cost of dairy products? ")

fruit_cost = float(fruit_cost)
Vegetables_cost = float(Vegetables_cost)
meat_cost = float(meat_cost)
dairy_cost = float(dairy_cost)

total_sum = fruit_cost + Vegetables_cost + meat_cost + dairy_cost
print(f"${total_sum:.2f}")

#2
# Prompt the user for the amount in US dollars
price_per_book = float(input("Enter price of book in euros"))
number_of_books = float(input("how many books do you have?"))
exchange_rate_usd = (price_per_book*1.8)*number_of_books

print(f"{exchange_rate_usd:.2f}$ is how much your books will cost in US Dollars")


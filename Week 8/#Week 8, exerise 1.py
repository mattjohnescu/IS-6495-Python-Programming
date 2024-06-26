#Week 8, exerise 1

#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} cuisine.")


    def open_restaurant(self):
        print(f"{self.name} is open for business.")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors



    def get_flavors(self):
        flavors_str = ', '.join(self.flavors)
        print(f"Flavors available: {flavors_str}")

#Usage 
ice_cream = IceCreamStand("Matts Ice Cream Shop", "Ice Cream", ["Vanilla", "Chocolate", "Rocky Road"])
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.get_flavors()


#2
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email


    def describe_user(self):
        print(f"User Summary:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}")


    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


class Admin(User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges



    def show_privileges(self):
        print(f"{self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")

#Creating Users
user1 = User('Matt', 'Johnescu', 23, 'matt@example.com')
user2 = User('Jane', 'George', 32, 'jane@example.com')

#Describe and greet users
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

#Create Admin
admin = Admin('Jeff', 'Whitman', 30, 'Jeff@example.com', ['can add post', 'can delete post', 'can ban user', 'can twerk'])
admin.describe_user()
admin.greet_user()
admin.show_privileges()



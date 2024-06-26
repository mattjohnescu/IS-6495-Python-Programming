# Week 7, Exercise 3

#1
class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1)
        print(self.num2)

#Creating an instance of NumberSet with num1=6 and num2=10
t = NumberSet(6, 10)

#Displaying the created instance
t.num1, t.num2




#2
class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs

#Creating an instance of animal for a spider with 4 arms and 4 legs
spider = Animal(4, 4)

#calling limbs method on the spider instance
spidlimbs = spider.limbs()

spidlimbs


#3
class Cereal:
    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"

#instances
c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

#Printing the instances
print(c1)
print(c2)



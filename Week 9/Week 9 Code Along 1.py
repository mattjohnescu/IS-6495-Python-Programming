class Numbers:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add(self):
        return self._x + self._y

    def multiply(self):
        return self._x * self._y

    @property
    def value(self):
        return self._x, self._y

    @value.setter
    def value(self, xy_tuple):
        self._x, self._y = xy_tuple

# Creating an instance of Numbers
num = Numbers(4, 5)
print(num.value)
print(num.add())
print(num.multiply())

# Changing the value using the setter
num.value = (6, 8)
print(num.value)
print(num.add())
print(num.multiply())




num = numbers(6,5)
num.__x = 55

print(num.__x)



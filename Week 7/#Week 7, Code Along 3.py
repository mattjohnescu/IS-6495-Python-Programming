#Week 7, Code Along 3
class student:
    first_name = ""
    last_name = ""
    is_graduated = ""

    def __init__(self, first_name, last_name):  # Adjusted to accept both first_name and last_name
        try:
            self.first_name = first_name  # Corrected from fname to first_name
            self.last_name = last_name  # Corrected from lname to last_name
            self.say_hi()
        except Exception as ex:
            print(ex)

    def say_hi(self):  # Indentation added to include this method in the student class
        print("Hello", self.first_name, self.last_name)

    def format_name(self):  # Corrected the syntax for method definition
        return f"{self.first_name} {self.last_name}"  # Adjusted the return statement


student = student("Matt", "Johnescu")  # This will now correctly create an instance

class py_solution:  # Added missing colon

    def reverse_word(self, s):  # Correct method name
        return ' '.join(reversed(s.split()))

c = py_solution()
print(c.reverse_word("Hello Class Welcome to Week 7"))  # Corrected method name to match definition



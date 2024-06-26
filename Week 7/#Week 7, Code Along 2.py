#Week 7, Code Along 2

class First_Class:

    def hello(sel, x):
        print("Hello 00P", x)

    def hello_class(self, x):
        print("Hello Class", x)




fc = First_Class()
fc.hello("John")
fc.hello_class("Hello World!")

fc1 = First_Class()
fc1.hello("batman")
fc1.hello_class("Someone Else")

fc2 = First_Class()
fc2.hello("poopman")
fc2.hello_class("A differnt person")


class student:

    first_name = ""
    last_name = ""
    is_graduated = False

student_list = []
for item in range(0,16):
    student = student()
    print(student.is_graduated)
    student_list.append(student)


for student in student_list:
    student.is_graduated = True

for student in student_list:
    print(student.is_graduated)





#Java Convention
#CamelCase

#MS_Convention
#PascalCase

#Python
# snake_case


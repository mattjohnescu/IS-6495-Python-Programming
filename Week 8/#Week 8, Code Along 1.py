#Week 8, Code Along 1
class Person:
    _uNID = ""
    _address = ""
    _DOB = ""
    _email = ""
    _first_name = ""
    _last_name = ""

    def __init__(self, first_name, last_name, uNID):
        self._first_name = first_name
        self._last_name = last_name
        self._uNID = uNID

    def get_names(self):
        return f"{self._first_name} {self._last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, uNID):
        super().__init__(first_name, last_name, uNID)
        self._courses = []

    def get_schedules(self):
        return self._courses

    def add_class(self, class_name):
        self._courses.append(class_name)

class Athlete(Student):
    _sport = ""
    
    def __init__(self, first_name, last_name, uNID, sport):
        super().__init__(first_name, last_name, uNID)
        self._sport = sport

class Staff(Person):
    def __init__(self, first_name, last_name, uNID, salary, dept):
        super().__init__(first_name, last_name, uNID)
        self._salary = salary
        self._dept = dept
        self._courses_taught = []

    def assign_teaching(self, course):
        self._courses_taught.append(course)

    def get_schedule(self):
        return self._courses_taught

p = Person("Matt", "Johnescu", "u1255890")
s = Student("Shaun", "White", "u12222223")
s.add_class("Python")
s.add_class("Cyber Security")
s.add_class("Networking")
s.add_class("Economics")

athlete = Athlete("Cam", "Rising", "0000000", "Football")
athlete.add_class("English")

teacher = Staff("John", "Degry", "u11111111", 10000000, "IS")
teacher.assign_teaching("Python")
teacher.assign_teaching("Power Apps")

print(s.get_schedules())
print(athlete.get_names())
print(athlete.get_schedules())
print(teacher.get_schedule())
print(teacher.get_names())
print(p.get_names())


class GamePiece():
    _name = ""
    _health = 0 
    _defence = 0

class Vivica(GamePiece):
    pass


class Baldur(GamePiece):
    pass


    










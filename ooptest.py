class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def hello(self):
        print("I'm a person!")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subject = str
        self.salary = int

    def set_subject(self):
        return self.subject

    def set_salary(self):
        return self.salary

    def get_subject(self):
        return self.subject

    def get_salary(self):
        return self.salary

    def hello(self):
        print("I'm a teacher!")


class Student(Person):
    def __init__(self):
        super.__init__()
        self.grades = []
        self.avaragegrade = int

    def set_grades(self):
        return self.grades

    def set_avaragegrade(self):
        return self.avaragegrade

    def get_grades(self):
        return self.grades

    def get_avaragegrade(self):
        return self.avaragegrade


Jack_p1 = Person("Jack", 26)

Will = Teacher("Will", 44)

Will.hello()
Jack_p1.hello()



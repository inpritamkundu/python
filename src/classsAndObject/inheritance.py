# simple inheritance


# base class
class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getdata(self):
        self.name = input('enter name')
        self.age = input('enter age')

    def putdata(self):
        print(self.name, self.age)


# Derived class or sub class
class scienceStudent(student):
    def science(self):
        print('this is a science method')


obstudent = scienceStudent("amar", "12")
obstudent.getdata()  # Accessible
obstudent.putdata()  # Accessible
obstudent.science()

# Multiple inheritance
# class c(a,b)  where a,b are base class


# Multilevel inheritance
# class b(a):  a-base class, b-derived class
# class c(b):  b-base class, c-derived class

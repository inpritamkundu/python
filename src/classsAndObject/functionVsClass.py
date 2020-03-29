# In this we will compare class and function

# function


# def getdata():
#     name = input('enter name')
#     age = input('enter age')
#     return (name, age)


# def putdata(name, age):
#     print(name)
#     print(age)


# name, age = getdata()
# putdata(name, age)


# Using Class and Object
class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getdata(self):
        self.name = input('enter name')
        self.age = input('enter age')

    def putdata(self):
        print(self.name, self.age)


obstudent = student("", "")
obstudent.getdata()
obstudent.putdata()

# It is used to make an object of the class.
# if we do not use instance and we directly assign values then the values will be assigned to every object of that class
# instance attribute we use with a constructor with special name
# Constructor is a method which executes when we create an object of the class


class teddy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


obteddy = teddy("amar", "red")
print(obteddy.name)

# Methods in class could be denoted as functions

# Example 1


class teddy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def changeColor(self):
        self.color = input('enter the new color')

    def changeName(self):
        self.name = input('enter the new name')


obteddy = teddy("ashish", "yellow")

print(obteddy.name, obteddy.color)
obteddy.changeColor()
obteddy.changeName()
print(obteddy.name, obteddy.color)

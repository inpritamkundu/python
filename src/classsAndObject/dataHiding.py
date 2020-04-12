# Data hiding in python


class A:

    __quantity = 0

    def add(self, increment):
        self.__quantity = self.__quantity+increment
        print(self.__quantity)


obA = A()
obA.add(10)

# if i try to access quantity directly

# print(obA.___quantity)

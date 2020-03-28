# to generate even numbers


# y = []

def even(x):

    for i in range(x):
        if i % 2 == 0:
            yield i
            # y.append(i)


x = list(even(10))
print(x)
# print(y)

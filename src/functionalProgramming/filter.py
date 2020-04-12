# it makes easy to filter data from iterables

# list

# l = [1, 2, 3, 4, 5, 45, 65, 6, 64]

# result = list(filter(lambda x: x % 2 == 0, l))
# print(result)


# dictionary
d = {'1': 20, '2': 31, '3': 40}

# x[0] : keys of dictionary, x[1] : values of dictionary
result = dict(filter(lambda x: x[1] % 2 == 0, d.items()))
print(result)

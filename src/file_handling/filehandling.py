import os

# To find the current path and add file name to the path
path = os.path.join(os.sys.path[0], "test.txt")
print(path)

# To write in a file

# file = open(path, 'w')
# file.write("This will hello")
# file.close()


# To read from a file

# file = open(path, 'r')
# content = file.read()
# print(content)
# file.close()


# To read a first line

# file = open(path, 'r')
# content = file.readline()
# content1 = file.readline()
# print(content)
# print(content1)
# file.close()


# to append file or add lines to the existing file

# file = open(path, 'a')
# content = file.write(" \n this is added")
# print(content)
# file.close()


# To read and differentiate each line

# file = open(path, 'r')
# d = []
# c = ""
# for i in file:
#     d.append(i)
# print(d)

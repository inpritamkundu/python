
# Checking pattern in a string

import re
string = "eggs are my first love"
pattern = r"eggs"
if re.match(pattern, string):
    print("match found")
else:
    print("match not found")


# Search & find
if re.search(pattern, string):
    # It only search the string in the main string
    print(re.search(pattern, string))
else:
    print("match not found")


# Find all
if re.findall(pattern, string):
    # It returns a list of number of times the element is found
    print(re.findall(pattern, string))
else:
    print("match not found")


# find and replace
string = re.sub(pattern, "eggseggs", string)
print(string)

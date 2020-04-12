# dot is used as a space where we can replace the value

import re

# pattern = r"da..y"  # It signifies that the word must get initialize with da and end with y

# if(re.match(pattern, "daddy")):
#     print("match found")
# else:
#     print("match not found")


# ^- caret -> Signifies the starting of the string , $-dollar -> Signifies the ending of the string


# pattern = r"^da.y$"  # It signifies that the word must get initialize with da and end with y

# if(re.match(pattern, "dady")):
#     print("match found")
# else:
#     print("match not found")


# *-star -> for taking repeating string or group which we have writen before star
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
    print("YES! We have a match!")
else:
    print("No match")

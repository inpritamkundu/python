import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient(
    "mongodb://onsi:onsi_12345@ds017070.mlab.com:17070/teckat")
mydb = myclient["teckat"]
mycol = mydb["training_enrollments"]
# print(mycol)

# Find one
# x = mycol.find_one()
# print(x)


# Find all

for x in mycol.find():
    print(x)

# ids = '5e91a23fb0023647150d8c9c'
# # find using query
# myquery = {"_id":  ObjectId(ids)}

# mydoc = mycol.find(myquery)

# for x in mydoc:
#     print(x)

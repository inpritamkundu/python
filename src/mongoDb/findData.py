import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["teckat"]
mycol = mydb["users"]

# Find one
# x = mycol.find_one()
# print(x)


# Find all

# for x in mycol.find():
#     print(x)

ids = '5e91a23fb0023647150d8c9c'
# find using query
myquery = {"_id":  ObjectId(ids)}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["teckat"]
mycol = mydb["users"]
# print(mycol)

# Find one
# x = mycol.find_one()
# print(x)


# Find all

# for x in mycol.find():
#     print(x)

ids = '5e91b536f8aa2f6e3f6198d8'
name = 'puja'
# find using query
myquery = {"_id":  ObjectId(ids),
           "name": name
           }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

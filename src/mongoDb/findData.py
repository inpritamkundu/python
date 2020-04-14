import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["teckat"]
mycol = mydb["users"]
# print(mycol)

# Find one
# x = mycol.find_one()
# print(x)

# find key exists or not
# x = mycol.find_one(
#     {'name': {"$exists": True}, '_id': ObjectId("5e91a0c937cbea16469ee447")})
# if(x):
#     if 'name' in x.keys():
#         print(x.keys())
# else:
#     print("no key found")


# Find all

# for x in mycol.find():
#     print(x)

ids = '5e91a0c937cbea16469ee447'
# find using query
myquery = {"_id":  ObjectId(ids),
           }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

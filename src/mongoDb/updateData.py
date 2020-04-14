import pymongo
from bson.objectid import ObjectId
import time
from datetime import datetime
# Connecting to mongoDb

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

print(myclient)

# Creating Database
mydb = myclient["teckat"]
print(mydb)


# Printing database List
# print(myclient.list_database_names())


# Creating Collection
mycol = mydb["users"]
print(mycol)

# To erase all data and set new data
# mycol.update_one({'name': 'puja'}, {'$set': {'address': 'bokaro'}})


dattimes = datetime.fromtimestamp(1253372036000.50/1000.0)

print(dattimes)

# To update a specific key of dictionary
doc = mycol.find_one_and_update(
    {"_id": ObjectId("5e91a0c937cbea16469ee447")},
    {"$set":
        {"date": dattimes}
     }, upsert=True
)

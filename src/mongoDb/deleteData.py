import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["teckat"]
mycol = mydb["users"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

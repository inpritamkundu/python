import pymongo

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

# Inserting one document in collection
# mydict = {"name": "John", "address": "Highway 37"}

# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# insert many documents in collection
mydict = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mydict)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)


# Printing collection List
# print(mydb.list_collection_names())

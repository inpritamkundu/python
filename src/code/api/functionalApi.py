from flask import Flask, request, jsonify
import pymongo
from bson.objectid import ObjectId


# Connecting to mongoDb

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# Creating/connecting Database
teckatdb = myclient["teckat"]

# Creating/connecting Collection
colusers = teckatdb["users"]


# Create app object

app = Flask(__name__)

# If we type this url then hello function is going to execute


@app.route('/users', methods=['POST', 'GET'])
# reads or writes in db as per method
def dataEntry():
    if(request.method == 'POST'):

        data = request.get_json()
        name = data['name']
        address = data['address']

        query = {
            "name": name,
            "address": address
        }
        colusers.insert_one(query)
        return '''
      name : {}
      address : {}
      status : "Data submitted successfully"
      '''.format(name, address)

    elif(request.method == 'GET'):
        data = []
        for value in colusers.find():
            # print(value['_id'])
            data.append(
                {'_id': str(value['_id']), 'name': value['name'], 'address': value['address']})
        print(data)
        return jsonify(data)


# To find wrt id, name, address
@app.route('/user', methods=['GET'])
def findEntry():
    _id = request.args.get('_id')
    name = request.args.get('name')
    address = request.args.get('address')

    if(_id):
        query = {'_id': ObjectId(_id)}
        data = checkQuery(query)
        return jsonify(data)
    elif(name):
        query = {'name': name}
        data = checkQuery(query)
        return jsonify(data)
    elif(address):
        query = {'address': address}
        data = checkQuery(query)
        return jsonify(data)
    else:
        return "Wrong format"


def checkQuery(query):

    data = []
    for value in colusers.find(query):
        # print(value['_id'])
        data.append(
            {'_id': str(value['_id']), 'name': value['name'], 'address': value['address']})
    if (len(data) > 0):
        return data
    else:
        return "No Data Found"


if __name__ == "__main__":
    app.run()

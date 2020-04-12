''' This will generate certificate 
data get from server -> Header gives auth token, body gives course id
flow -> check token authenticity, if status true then check for status of training enrollment through userid and course id,
        if enrolled then check if time gap is more than 15 days from current time, if true then generate pdf update
        certificate generation time and status.
 '''


import pymongo
from bson.objectid import ObjectId
from functions import auth        # authentication module
from flask import Flask, request


# connect to mongo db
myclient = pymongo.MongoClient(
    "mongodb://onsi:onsi_12345@ds017070.mlab.com:17070/teckat")
mydb = myclient["teckat"]
trainingCollection = mydb["training_enrollments"]


# Api call

# Create app object
app = Flask(__name__)


@app.route('/generateCertificate', methods=['GET'])
def generateCerti():
    # collect body data
    courseId = request.args['course_id']

    # check auth token from header
    token = request.headers.get('Authorization')
    l = token.split()

    # send token for authentication
    data = auth.authenticate(l[1])

    # Check status of authorization
    if(data['status']):
        userId = data['user']['_id']
        print(type(userId), type(courseId))

        # Find status of enrollment
        # Check query for enrollment status
        enrollmentCheckQuery = {
            "_id":  ObjectId(userId),
            "course_id": ObjectId(courseId)
        }
        # Find enrollment data for the check query
        enrollmentData = trainingCollection.find(enrollmentCheckQuery)

        for x in enrollmentData:
            print(x)
        return "authorized"
        # Check if enrollment data exist
        # if(enrollmentData['status'] == 'ENROLLED'):
        #     return "Authorized to access data"
        # else:
        #     return "User has not enrolled yet"

    else:
        return "Not authorized to access data"


if __name__ == "__main__":
    app.run(debug=True)


# ids = '5e91a23fb0023647150d8c9c'
# # find using query
# myquery = {"_id":  ObjectId(ids)}

# mydoc = mycol.find(myquery)

# for x in mydoc:
#     print(x)

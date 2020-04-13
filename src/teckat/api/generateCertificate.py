''' This will generate certificate
data get from server -> Header gives auth token, body gives course id
flow -> check token authenticity, if status true then check for status of training enrollment through userid and course id,
        if enrolled then check if certificate_id key is present or not,if not present then check if time gap is more than 
        15 days from current time, if true then generate pdf update certificate generation time and status, else send certificate
        out of date. If certificate_id is present then get all the previous details and print the certificate.

data->
user enrolled -> createdAt from enrollment collection
certificate no. -> training_certificate's _id from enrollment collection
certificate date -> generated date from certificate collection
 '''


from datetime import datetime
import pymongo
from bson.objectid import ObjectId
from functions import auth        # authentication module
from flask import Flask, request
import time
from functions import generateCertificatePdf as pdf


# connect to mongo db
myclient = pymongo.MongoClient(
    "mongodb://onsi:onsi_12345@ds017070.mlab.com:17070/teckat?retryWrites=false")
mydb = myclient["teckat"]
trainingEnrollmentCollection = mydb["training_enrollments"]
trainingCourseCollection = mydb["training_courses"]
trainingCertificateCollection = mydb["training_certificate"]
# Api call

# Create app object
app = Flask(__name__)


@app.route('/generateCertificate', methods=['GET'])
def generateCerti():
    # collect body data
    courseId = request.args['course_id']

    # getting course details
    courseCheckQuery = {
        "_id": ObjectId(courseId)
    }
    courseData = trainingCourseCollection.find_one(
        courseCheckQuery)

    # check auth token from header
    token = request.headers.get('Authorization')
    l = token.split()

    # send token for authentication
    data = auth.authenticate(l[1])

    # Check status of authorization
    if(data['status']):

        userId = data['user']['_id']    # uncomment on production

        # userId = '5dd6c42cf570820d94ae8cca'   # comment on production

        # Find status of enrollment
        # Check query for enrollment status
        enrollmentCheckQuery = {
            "user_id":  ObjectId(userId),
            "course_id": ObjectId(courseId)
        }

        # Find enrollment data for the check query
        enrollmentData = trainingEnrollmentCollection.find_one(
            enrollmentCheckQuery)

        # Check if enrollment data exist
        if(enrollmentData['status'] == 'ENROLLED'):

            # Check certificate is previously generated or not
            if 'certificate_id' in enrollmentData.keys():
                certificateGenerateStatus = True
            else:
                certificateGenerateStatus = False

            if(not certificateGenerateStatus):

                # Checking time gap between current time and created time is greater than 15
                createdAt = str(enrollmentData['createdAt'])
                dt_obj = datetime.strptime(createdAt,
                                           '%Y-%m-%d %H:%M:%S.%f')
                createdAtMillisec = dt_obj.timestamp() * 1000   # Created at in milliseconds

                # current time in milliseconds
                currentTimeMillisec = int(round(time.time() * 1000))

                # checking time difference in current time and created time
                timeGap = currentTimeMillisec-createdAtMillisec

                if(timeGap >= 1300795200):

                    # inserting data to training certificate collection
                    certificateData = trainingCertificateCollection.insert_one(
                        {'generatedAt': currentTimeMillisec})
                    certificateId = str(certificateData.inserted_id)

                    # Insert certificate id to enrollment collection
                    doc = trainingEnrollmentCollection.find_one_and_update(
                        {"_id": ObjectId(str(enrollmentData['_id']))},
                        {"$set":
                         {"certificate_id": certificateId}
                         }, upsert=True)

                    # fetching data and sending for pdf generation
                    certificateNum = str(enrollmentData['_id'])

                    userName = data['user']['firstName'] + \
                        " "+data['user']['lastName']

                    courseName = courseData['title']

                    # send date[0] for date
                    date = str(datetime.fromtimestamp(
                        currentTimeMillisec/1000.0)).split()

                    fileName = certificateId

                    pdfPath = pdf.generateCerti(certificateNum, userName,
                                                courseName, date[0], fileName)

                    return pdfPath
                else:
                    return "certificate out of date"

            else:

                # Getting certificate data that is already present
                certificateId = str(enrollmentData['certificate_id'])

                certificateData = trainingCertificateCollection.find_one(
                    {'_id': ObjectId(certificateId)})

                # fetching data and sending for pdf generation
                certificateNum = str(enrollmentData['_id'])
                userName = data['user']['firstName'] + \
                    " "+data['user']['lastName']
                courseName = courseData['title']

                # send date[0] for date
                date = str(datetime.fromtimestamp(
                    certificateData['generatedAt']/1000.0)).split()

                fileName = certificateId

                pdfPath = pdf.generateCerti(certificateNum, userName,
                                            courseName, date[0], fileName)
                return pdfPath

        else:
            return "User has not enrolled yet"

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

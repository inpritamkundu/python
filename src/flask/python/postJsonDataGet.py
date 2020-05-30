# import flask
from flask import Flask, request, jsonify

# Create app object

app = Flask(__name__)

# Create url

# If we type this url then hello function is going to execute
@app.route('/value', methods=['POST'])
def hello():
    data = request.get_json()
    email = data['email']
    course_id = data['course_id']
    return jsonify({
        "email": email,
        "course_id": course_id
    })


if __name__ == "__main__":
    app.run(debug=True)

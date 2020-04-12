from functions import auth
from flask import Flask, request

# Create app object
app = Flask(__name__)


@app.route('/users/login', methods=['POST'])
def token():
    token = request.headers.get('Authorization')
    l = token.split()
    data = auth.authenticate(l[1])
    return data


if __name__ == "__main__":
    app.run(debug=True)

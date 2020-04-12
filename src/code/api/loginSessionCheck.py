from flask import Flask, request
import jwt
# Create app object

app = Flask(__name__)


@app.route('/users/login', methods=['POST'])
def token():
    token = request.headers.get('Authorization')
    l = token.split()
    authToken = l[1].encode('utf-8')
    # print(authToken)
    decoded_jwt = jwt.decode(authToken, 'organizationId', algorithms='HS256')
    print(decoded_jwt)
    return decoded_jwt


if __name__ == "__main__":
    app.run(debug=True)

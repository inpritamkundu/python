# import flask
from flask import Flask, request

# Create app object

app = Flask(__name__)

# Create url

# If we type this url then hello function is going to execute
@app.route('/value', methods=['GET'])
def hello():
    data = request.args.get('value')
    return ''' value is {}'''.format(data)


if __name__ == "__main__":
    app.run()

# import flask
from flask import Flask

# Create app object

app = Flask(__name__)

# Create url

# If we type this url then hello function is going to execute
@app.route('/')
def hello():
    return 'hello world'


# If we type this url then task function is going to execute, this is known as routing
@app.route('/task/')
def task():
    return 'This is task function'


if __name__ == "__main__":
    app.run()

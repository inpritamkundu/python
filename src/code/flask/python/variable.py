# import flask
from flask import Flask

# Create app object

app = Flask(__name__)

# Create url

# If we type this url then hello function is going to execute
@app.route('/guest/<name>')
def hello(name):
    return 'hello %s' % name


if __name__ == "__main__":
    app.run()

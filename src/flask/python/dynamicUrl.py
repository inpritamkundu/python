# import flask
from flask import Flask, redirect, url_for

# Create app object

app = Flask(__name__)

# Create url

# If we type this url then hello function is going to execute
@app.route('/admin/')
def adminName():
    return 'hello admin'


# If we type this url then task function is going to execute, this is known as routing
@app.route('/guest/<name>')
def guestName(name):
    return 'hello %s' % name


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('adminName'))
    else:
        return redirect(url_for('guestName', name=name))


if __name__ == "__main__":
    app.run()

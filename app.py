# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def welcome():
#     return "Hello World"

# @app.route("/home")
# def home():
#     return "this is home page"

# import user_controller

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)  # Runs on all interfaces on port 5000


from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is home page"

# Import the user_controller at the end to ensure all routes are registered
from controller.user_controller import *

from controller.product_controller import *

# from controller import product_controller, user_controller # this is not working 
# from controller import * # it is also not working in my system

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



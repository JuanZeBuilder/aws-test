from flask import Flask

application = Flask(__name__)

@application.route("/")
# print a nice greeting.
def say_hello():
    return "Hello World!"


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()

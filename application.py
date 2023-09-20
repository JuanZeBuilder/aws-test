from flask import Flask

application = Flask(__name__)

@application.route("/")
# print a nice greeting.
def say_hello():
    return "Hello World!"

@application.route("/bye")
# print a nice greeting.
def byebye():
    return "Byebye World!"

# run the app.
if __name__ == "__main__":
    application.run()

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Synenta Tech Leaders!\n\nLet's build a new, better Syngenta IS experience!"

if __name__ == "__main__":
    application.run()

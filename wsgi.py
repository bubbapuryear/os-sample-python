from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return """<html>
    <head><body>
    <p>Hello Synenta Tech Leaders!</p>
    <p>Let's build a new, better Syngenta IS experience!</p>
    </body></head></html>"""

if __name__ == "__main__":
    application.run()

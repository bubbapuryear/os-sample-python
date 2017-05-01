from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return """<html>
    <head><body>
    <p>Hello World!</p>
    </body></head></html>"""

if __name__ == "__main__":
    application.run()

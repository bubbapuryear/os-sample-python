from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return """<html>
    <head><body>
    <p>Hello Syngenta!</p>
    <p>Let's build a better IS environment. Maybe something like what's in the Phoenix Project</p>
    </body></head></html>"""

if __name__ == "__main__":
    application.run()

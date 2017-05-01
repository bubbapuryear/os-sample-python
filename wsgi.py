from flask import Flask
application = Flask(__name__)

ping_count = 1

@application.route("/")
def hello():
    ping_count = ping_count + 1
    return """<html>
    <head><body>
    <p>Hello Synenta Tech Leaders!</p>
    <p>Let's build a new, better Syngenta IS experience!</p>
    <p>%02d hits</p>
    </body></head></html>""" % (ping_count)

if __name__ == "__main__":
    application.run()

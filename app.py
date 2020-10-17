from flask import Flask

app = Flask(__name__)


@app.route("/rohan", methods=["GET", "POST"])
def rohan():
    return "<h1> hello rohan </h1>"

@app.route("/", methods=["GET", "POST"])
def index():
    return "<h1> hello world </h1>"



app.run(debug=True)




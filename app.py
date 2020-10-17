from flask import Flask

app = Flask(__name__)


@app.route("/rohan", methods=["GET", "POST"])
def index():
    return "<h1> hello </h1>"

app.run(debug=True)



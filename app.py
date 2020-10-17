from flask import Flask, request
import authenticate

app = Flask(__name__)
bot = authenticate.verify_bot_access()

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return authenticate.verify_token(request)
    else:
        bot.send_text_message(user_id, "Hello This is The Bot")


@app.route("/", methods=["GET", "POST"])
def index():
    return "<h1> hello this is Capitta Made By Rohan </h1>"


if __name__ == "__main__":
    app.run(debug=True)




from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def game():
    return render_template("index.html ")


@app.route("/game")
def game():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)

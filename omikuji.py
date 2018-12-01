import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/omikuji")
def omikuji():
    omikuji_list = ["大吉", "吉", "凶"]

    omikujikekka = random.choice(omikuji_list)

    return render_template("omikuji.html", omikujikekka=omikujikekka)


if __name__ == "__main__":
    app.run(debug=True)

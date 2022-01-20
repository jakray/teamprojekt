from flask import Flask, render_template, request, flash
from modelv4 import *


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
        flash("Clickbaitsatz übergeben")
        return render_template("index.html")

@app.route("/sentence", methods=['POST', 'GET'])
def greeter():
         satz =  str(request.form['sentence_input'])
         print(satz)
         ruckgabe = handler(satz)
         ruckgabe = round(ruckgabe*10000)
         ruckgabe = ruckgabe / 100
         ruckgabe = str(ruckgabe)
         flash("Der Übergebene Satz ist zu" + ruckgabe + "% Clickbait.")
         return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

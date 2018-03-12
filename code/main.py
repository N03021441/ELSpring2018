from flask import Flask, render_template, request
from datetime import datetime
import sqlite3


app = Flask(__name__)



@app.route("/")
def hello():
   return render_template("main.html")


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=81, debug=True)

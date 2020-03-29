# app.py
from flask import Flask           # import flask
import requests
app = Flask(__name__)             # create an app instance

@app.route("/<sam>")                   # at the end point /
def hello(sam):                      # call method hello
    r = requests.get('https://corona.lmao.ninja/countries/'+sam)
    return r.text
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#app intialisation
app = Flask(__name__)

#config files for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "<h1>Hello</h1>"

if __name__=='__main__':
    app.run(debug=True)
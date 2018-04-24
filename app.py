
from flask import Flask, jsonify, abort, request, json
from werkzeug import secure_filename
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zmlunszmacjepr:a3a78375484ba71e5cf8e6ebd967c395372d7d1ce4909f168f077e5dd4221235@ec2-23-23-247-222.compute-1.amazonaws.com:5432/dagavtnqopulb2'
db = SQLAlchemy(app)

from models import *

db.drop_all()
db.create_all()


@app.route('/')
def index():
    return "welcome to adaptyou analyti server API"


@app.route('/api/test')
def check():
    return jsonify({'active': 'true'})


@app.route('/api/save', methods=['POST'])
def save():
    userData = request.json
    userdata = UserData(username=userData['username'], component=userData['component'], url=userData['url'], mouseover=userData['mouseover'], clicks=userData['clicks'])
    db.session.add(userdata)
    try:
        db.session.commit()
    except:
        return "already added"
    else:
        return "pass"


@app.route('/api/saved')
def getAll():
    allData = UserData.query.all()
    formatted = {}
    
    for userdata in allData:
        data ={}
        data["username"]= userdata.username 
        data["component"]= userdata.component
        data["url"]= userdata.url 
        data["clicks"]= userdata.clicks 
        data["mouseover"]=userdata.mouseover
        
        formatted[len(formatted)]=data

    return jsonify(formatted)


if __name__ == "__main__":
    app.run()

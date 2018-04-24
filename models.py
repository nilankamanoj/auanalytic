from app import db

class UserData(db.Model):
    username = db.Column(db.String(80), nullable=False, primary_key=True)
    component = db.Column(db.String(80), nullable=False, primary_key=True)
    url = db.Column(db.String(256), nullable=False, primary_key=True)
    mouseover = db.Column(db.BigInteger)
    clicks = db.Column(db.BigInteger)
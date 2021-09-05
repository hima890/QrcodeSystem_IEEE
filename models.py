from enum import unique
from theFormForaccepted import db
from datetime import datetime
from config import Config


class theAccepted(db.Model):
    __tabel__ = "theAccepted"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    hashLink = db.Column(db.String(200), nullable=False)
    imageNumber = db.Column(db.String(200), nullable=False)
    the_link_use = db.Column(db.Integer(), nullable=False, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now())
    

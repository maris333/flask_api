from src import db
from datetime import datetime


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=False)

    def __init__(self, content, author, date=None):
        self.author = author
        self.content = content
        self.date = date

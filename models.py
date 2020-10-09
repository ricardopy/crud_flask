from app import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

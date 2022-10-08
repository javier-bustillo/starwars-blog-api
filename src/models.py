from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    heigth = db.Column(db.Integer(4), nullable=True)
    mass = db.Column(db.Integer(4), nullable=True)
    hair_color = db, Column(db.String(10), nullable=True)
    skin_color = db, Column(db.String(10), nullable=True)
    eye_color = db, Column(db.String(10), nullable=True)
    birth_year = db, Column(db.String(10), nullable=False)
    gender = db, Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

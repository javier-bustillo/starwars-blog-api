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
    hair_color = db.Column(db.String(10), nullable=True)
    skin_color = db.Column(db.String(10), nullable=True)
    eye_color = db.Column(db.String(10), nullable=True)
    birth_year = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    planet_id = db.Column(db.Integer(), db.ForeignKey("Planet.id"))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rotation_period = db.Column(db.Integer(3), nullable=False)
    orbital_period = db.Column(db.Integer(4), nullable=False)
    diameter = db.Column(db.Integer(5), nullable=False)
    climate = db.Column(db.String(10), nullable=False)
    gravity = db.Column(db.String(10), nullable=False)
    terrain = db.Column(db.String(100), nullable=False)
    surface_water = db.Column(db.Integer(4), nullable=False)
    population = db.Column(db.Integer(10), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

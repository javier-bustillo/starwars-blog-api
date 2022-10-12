from flask_sqlalchemy import SQLAlchemy
# from eralchemy import render_er

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    heigth = db.Column(db.Integer, unique=False, nullable=True)
    mass = db.Column(db.Integer, unique=False, nullable=True)
    hair_color = db.Column(db.String(25), unique=False, nullable=True)
    skin_color = db.Column(db.String(25), unique=False, nullable=True)
    eye_color = db.Column(db.String(25), unique=False, nullable=True)
    birth_year = db.Column(db.String(15), unique=False, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "heigth": self.heigth,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender

        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Integer, unique=False, nullable=True)
    diameter = db.Column(db.Integer, unique=False, nullable=True)
    climate = db.Column(db.String(25), unique=False, nullable=True)
    gravity = db.Column(db.String(25), unique=False, nullable=True)
    terrain = db.Column(db.String(100), unique=False, nullable=True)
    surface_water = db.Column(db.Integer, unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population

        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,

        }


# Draw from SQLAlchemy db
# render_er(Base, 'diagram.png')

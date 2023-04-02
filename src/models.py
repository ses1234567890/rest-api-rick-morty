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
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    alive = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "alive": self.alive,
        }

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(120), unique=True, nullable=False)
    dimensions = db.Column(db.String(80), unique=False, nullable=False)
    residents = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.tipo,
            "dimensions": self.dimensions,
            "alive": self.residents,
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "character": self.character_id,
            "location": self.location_id,
        }

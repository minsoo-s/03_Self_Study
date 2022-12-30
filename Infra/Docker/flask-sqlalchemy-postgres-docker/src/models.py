import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
# sqlalchemy -> python에서 사용가능한 ORM(Object-relational maping)

class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100))
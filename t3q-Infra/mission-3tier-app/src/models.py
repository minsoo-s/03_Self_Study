import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
# sqlalchemy -> python에서 사용가능한 ORM(Object-relational maping)

# ORM방식 DB테이블 생성
class wordtable(db.Model):
    __tablename__ = 'wordtable'
    # Primary key 지정
    id = db.Column(db.Integer, primary_key=True)
    # 테이블 요소
    word = db.Column(db.String(100))
    area = db.Column(db.String(100))
    mean = db.Column(db.String(100))


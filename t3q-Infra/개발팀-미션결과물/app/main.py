## 모듈 삽입
from flask import Flask, request, redirect, jsonify, Response
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
from keras.models import load_model
import numpy as np

## SQLAlchemy <> Postgresql 연결(DB 엔진 및 세션 로드)
db = create_engine("postgresql://root:root@kympsql-service.default.svc.cluster.local:5432/mydb")
base = declarative_base()

Session = sessionmaker(db)
session = Session()


## ORM방식으로 DB의 테이블 정의
class TestTable(base):
    __tablename__ = 'Coffee_info'
    ## primary key 지정
    idx = Column(Integer, primary_key=True)
    aroma = Column(Float)
    flavor = Column(Float)
    acidity = Column(Float)
    balance = Column(Float)

base.metadata.create_all(db)

## Flask 객체 생성
app = Flask(__name__)
CORS(app)

@app.route('/datasend', methods=['POST'])
def datasend():
    ## SQLAlchemy <> Postgresql 연결(DB 엔진 및 세션 로드)
    db = create_engine("postgresql://root:root@kympsql-service.default.svc.cluster.local:5432/mydb")

    Session = sessionmaker(db)
    session = Session()
    
    req = request.get_json()
    ## 데이터 요청
    aroma = req['aroma']
    flavor = req['flavor']
    acidity = req['acidity']
    balance = req['balance']
    
    ## 모델 불러오기
    model = load_model('./model/my_model.h5')
    arr = np.array([[float(aroma), float(flavor), float(acidity), float(balance)]])
    pred = model.predict(arr)
    
    ## DB로 데이터 전송
    session.add(TestTable(aroma=aroma, flavor=flavor,
                acidity=acidity, balance=balance))
    session.commit()
    result = jsonify({'score':str(pred[0][0])})
    
    # result.headers.add('Access-Control-Allow-Origin', '*')
    return result

@app.route('/data')
def data(): # 플러시, 로깅
    db = create_engine("postgresql://root:root@kympsql-service.default.svc.cluster.local:5432/mydb")

    Session = sessionmaker(db)
    session = Session()
    
    q = session.query(TestTable).all()
    temp = dict()
    temp['info'] = list()
    for i in q:
        temp['info'].append({'idx': i.idx, 'aroma': i.aroma, 'flavor': i.flavor,
                             'acidity': i.acidity, 'balance': i.balance})
    result = jsonify(temp)
    # result.headers.add('Access-Control-Allow-Origin', 'http://172.16.16.132:30808')
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

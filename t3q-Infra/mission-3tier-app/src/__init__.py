from flask import Flask

from .models import db
from . import config
import os

# 플라스크 공식 홈페이지에서 애플리케이션 팩토리 사용을 권하기도 하고,
# app 객체를 전역으로 사용하면 프로젝트 규모가 커질수록 문제가 발생할 확률이 높아진다고 하여 사용
def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app
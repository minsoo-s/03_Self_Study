# 서버 환경 : .env
import os

user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
host = os.getenv('PG_HOST')
database = os.getenv('PG_DB')
port = os.getenv('PG_PORT')

# 사용자 이름 및 암호를 사용하여 로컬 컴퓨터에서 기본 데이터베이스에 연결
# psycopg2: PostgreSQL DB 어댑터
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
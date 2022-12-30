FROM python:3.8.5

WORKDIR /test
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./app.py

# docker iamge
# docker build -t my-api . <- api 폴더로 이동 후 실행

# docker 실행
# docker run --name api -p 5000:5000 my-api
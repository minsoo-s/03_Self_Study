######## API ##########################################

# Module
# $ pip install -U Flask-SQLAlchemy
import json
from flask import request
from . import create_app, database
from .models import wordtable
from flask import redirect, url_for

# Flask 객체 생성 
app = create_app()

# CRUD
## get
@app.route('/result', methods=['GET'])
def read():
    wordbooks = database.get_all(wordtable)
    all_wordtable = []
    for words in wordbooks:
        new_wordbook = {
            "id": words.id,
            "word": words.word,
            "area": words.area,
            "mean": words.mean1
        }

        all_wordtable.append(new_wordbook)
    return json.dumps(all_wordtable), 200

## POST METHOD
@app.route('/add', methods = ['POST'])
def add():

    # 데이터 요청
    word = request.form['word']
    area = request.form['area']
    mean = request.form['mean']

    database.add_instance(wordtable, word=word, area=area, mean=mean)
    return redirect('result') # 1. 주소이동 redirect('url명') 2. 함수로 이동 redirect(url_for('함수명'))






########### 최소단위 flask app ####################

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

############ 라우팅 ################################

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'

############# 라우팅 변수 규칙 #####################

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


############### url 후행 슬래쉬 ######################
# url 후행 슬래쉬 없으면, 좀 더 고유한 url

# @app.route('/projects/') # 후행슬래쉬 있든없든 모두 동작
# def projects():
#     return 'The project page'

# @app.route('/about') # 후행슬래쉬 없을 때만 동작
# def about():
#     return 'The about page'

################ URL Building : url_for() ################
# from flask import url_for

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# # url 확인방법 - print문으로 각 함수에 해당하는 url 표시
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

################ HTTP method #################################
# 방법1 ---------------------------------
# from flask import request

# def do_the_login():
#     return "do the login"

# def show_the_login_form():
#     return "id , pw"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# 방법 2------------------------------------
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

###################### Static Files(정적 파일)###################
# that’s usually where the CSS and JavaScript files are coming from


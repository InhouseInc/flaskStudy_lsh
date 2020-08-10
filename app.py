from flask import Flask, url_for, request, render_template, Markup
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hellow World'

# URI파라미터로 프로필 표현a
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

# URI파라미터로 프로필 표현
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# Flask의 URL 규칙은 Werkzeug의 라우팅 모듈
# /user와 /user/는 다른 url로 인식.
# 첫번째의 경우 유저가 /user로 접근하는건 인식하나 /user/는 인식하지 못함.
# 두번째의 경우 /user나 /user/ 모두 인식함.
# 헷갈리는 경우 url_for() 같이 내가 작성한 어플리케이션의 도메인을 얻는 함수가 있음.

# with app.test_request_context():
#     print url_for('index')

# Http 요청 처리
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

# 템플릿 처리
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 디버그 모드 실행(자동 리로드)
if __name__ == '__main__':
    app.run(debug=True)

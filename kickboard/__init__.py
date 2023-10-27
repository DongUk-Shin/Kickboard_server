from flask import Flask, flash, redirect, render_template, request, url_for, session, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import config

#객체 생성
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'abcde'

db.init_app(app)
migrate.init_app(app, db)

from .models import information


@app.route('/')
def default():
    return redirect('/main')

@app.route('/main')
def main():
    session_id = session.get('session_user')
    return render_template("main.html", session_id=session_id)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        """
        json_data = request.get_json()
        user_id = json_data['user_id']
        password = json_data['password']
        name = json_data['name']
        birth = json_data['birth']
        call = json_data['call']
        """
        user_id = request.form['user_id']
        password = request.form['password']
        name = request.form['name']
        birth = request.form['birth']
        call = request.form['call']

        hashed_password = generate_password_hash(password)  # 비밀번호 해싱
        user = information(user_id=user_id, password=hashed_password, name=name, birth=birth, call=call)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main'))

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        user_id_input = request.form['user_id_input']
        password_input = request.form['password_input']
        user = information.query.filter_by(user_id=user_id_input).first()
        
        if user and check_password_hash(user.password, password_input):
            session.clear()
            session['session_user'] = user.user_id #세션에 id 저장
            return redirect(url_for('main'))
        
    return render_template('signin.html')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main'))

#DB 표시
@app.route('/dataview/')
def dataview():
    data = information.query.all()
    return render_template('dataview.html', data=data)
    
"""
#POST 요청으로 json 받아서 user 객체 생성
@app.route('/jsontest/', methods=['POST'])
def jsontest():
    if request.method == 'POST':
        data = request.get_json()

        user_id = data.get('user_id')
        password = data.get('password')
        name = data.get('name')
        birth = data.get('birth')
        call = data.get('call')

        hashed_password = generate_password_hash(password)
        user = information(user_id=user_id, password=hashed_password, name=name, birth=birth, call=call)
        db.session.add(user)
        db.session.commit()
        return "성공"


@app.route('/jsontest1/', methods=['GET'])
def jsontest1():
    if request.method == 'GET':
        data = request.get_json()


        user_info_json = jsonify(
            user_id=user.user_id,
            password=user.password,
            name=user.name,
            birth=user.birth,
            call=user.call
        )
        
        return user_info_json
    
"""

if __name__ == '__main__':
    #app.run(host="220.69.208.119", port=8000, debug=True)
    app.run(port=8000, debug=True)

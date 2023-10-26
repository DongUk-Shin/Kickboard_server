from flask import Flask, flash, redirect, render_template, request, url_for, session
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


if __name__ == '__main__':
    #app.run(host="220.69.208.119", port=8000, debug=True)
    app.run(port=8000, debug=True)

from flask import Blueprint
from flask import redirect, render_template, request, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from kickboard import db
from kickboard.models import information

bp = Blueprint('html_views', __name__, url_prefix='/')

#HTML에서 사용하는 테스트 페이지 

@bp.route('/')
def default():
    return redirect('/main')

@bp.route('/main')
def main():
    session_id = session.get('session_user')
    return render_template("main.html", session_id=session_id)

@bp.route('/signup', methods=['GET', 'POST'])
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

@bp.route('/signin', methods=['GET', 'POST'])
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

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main'))

#DB 표시
@bp.route('/dataview/')
def dataview():
    data = information.query.all()
    return render_template('dataview.html', data=data)
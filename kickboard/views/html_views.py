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

        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone_number = request.form['phone_number']

        hashed_password = generate_password_hash(password)  # 비밀번호 해싱
        user = information(email=email, password=hashed_password, name=name, phone_number=phone_number)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('html_views.main'))

    return render_template('signup.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        emain_input = request.form['email_input']
        password_input = request.form['password_input']
        user = information.query.filter_by(email=emain_input).first()
        
        if user and check_password_hash(user.password, password_input):
            session.clear()
            session['session_user'] = user.email #세션에 id 저장
            return redirect(url_for('html_views.main'))
        
    return render_template('signin.html')

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('html_views.main'))

#DB 표시
@bp.route('/dataview/')
def dataview():
    data = information.query.all()
    return render_template('dataview.html', data=data)
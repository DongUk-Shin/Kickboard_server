from flask import Blueprint, current_app
from flask import redirect, render_template, request, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from kickboard import db
from kickboard.models import information, RideLog

import os

bp = Blueprint('html_views', __name__, url_prefix='/')

#HTML에서 사용하는 테스트 페이지 

@bp.route('/')
def default():
    return redirect('/main')

@bp.route('/main/')
def main():
    session_id = session.get('session_user')
    return render_template("main.html", session_id=session_id)

@bp.route('signupTest/', methods=['GET', 'POST'])
def signupTest():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        name = request.form['name']
        phone_number = request.form['phone_number']

        existing_user = information.query.filter_by(email=email).first()
        if existing_user:
            return "아이디가 이미 존재합니다", 202

        if password != confirm_password:
            return "비밀번호가 일치하지 않습니다", 203
        
        hashed_password = generate_password_hash(password)  # 비밀번호 해싱
        user = information(email=email, password=hashed_password, name=name, phone_number=phone_number)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('html_views.main'))

    return render_template('signup.html')


@bp.route('signinTest/', methods=['GET', 'POST'])
def signinTest():
    if request.method == 'POST':
        emain_input = request.form['email_input']
        password_input = request.form['password_input']
        user = information.query.filter_by(email=emain_input).first()
        
        if user and check_password_hash(user.password, password_input):
            session.clear()
            session['session_user'] = user.email #세션에 id 저장
            return redirect(url_for('html_views.main'))
        
    return render_template('signin.html')

@bp.route('logoutTest/')
def logoutTest():
    session.clear()
    return redirect(url_for('html_views.main'))

#DB 표시
@bp.route('dataviewTest/')
def dataviewTest():
    info = information.query.all()
    ridelog = RideLog.query.all()
    return render_template('dataview.html', info=info, ridelog=ridelog)

# 이미지 받기
@bp.route('imageTest/', methods=['GET', 'POST'])
def getImage():
    if request.method == 'POST':

        if 'image_file' not in request.files:
            return 'File is missing', 404

        image_file = request.files['image_file']

        if image_file.filename == '':
            return 'File is missing', 404

        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))

        return redirect(url_for('html_views.main'))
    return render_template('send2image.html')

#운행 기록 받아서 서버에 저장
@bp.route('saveriderogTest/', methods=['GET', 'POST'])
def saveRideRogTest():
    if request.method == 'POST':

        email = request.form['email_input']
        date = request.form['date_input']
        distance = request.form['distance_input']
        runtime = request.form['runtime_input']
        cost = request.form['cost_input']

        user = RideLog(email=email, date=date, distance=distance, runtime=runtime, cost=cost)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('html_views.main'))
    return render_template('saveriderog.html')


from flask import Blueprint
from flask import redirect, render_template, request, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from kickboard import db
from kickboard.models import information

bp = Blueprint('main_views', __name__, url_prefix='/')

#POST 요청으로 json 받아서 user 객체 생성
@bp.route('/jsontest/', methods=['POST'])
def jsontest():
    if request.method == 'POST':
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        phone_number = data.get('phone_number')

        hashed_password = generate_password_hash(password)
        user = information(email=email, password=hashed_password, name=name, phone_number=phone_number)
        db.session.add(user)
        db.session.commit()
        return "성공"


@bp.route('/jsontest1/', methods=['GET'])
def jsontest1():
    if request.method == 'GET':
        data = request.get_json()

        return 

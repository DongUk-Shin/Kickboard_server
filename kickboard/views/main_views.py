from flask import Blueprint
from flask import redirect, render_template, request, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from kickboard import db
from kickboard.models import information

bp = Blueprint('main', __name__, url_prefix='/')

#POST 요청으로 json 받아서 user 객체 생성
@bp.route('/jsontest/', methods=['POST'])
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


@bp.route('/jsontest1/', methods=['GET'])
def jsontest1():
    if request.method == 'GET':
        data = request.get_json()

        return 

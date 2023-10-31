from flask import Blueprint, current_app
from flask import redirect, render_template, request, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from kickboard import db
from kickboard.models import information, RideLog, Accident

import os

bp = Blueprint('main_views', __name__, url_prefix='/')
initial_start_data = {"start":"X"}

#POST 요청으로 json 받아서 user 객체 생성
@bp.route('signup/', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json() #json 데이터 받아옴
        if not data: 
            return "데이터가 올바르지 않습니다", 400

        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        name = data.get('name')
        phone_number = data.get('phone_number')
        
        existing_user = information.query.filter_by(email=email).first()
        if existing_user:
            return "아이디가 이미 존재합니다", 202

        if password != confirm_password:
            return "비밀번호가 일치하지 않습니다", 203

        hashed_password = generate_password_hash(password)
        user = information(email=email, password=hashed_password, name=name, phone_number=phone_number)
        db.session.add(user)
        db.session.commit()

        return "회원가입이 성공적으로 완료되었습니다", 201


#json 받아서 비밀번호 검증 후 로그인 return
@bp.route('signin/', methods=['POST'])
def signin():
    if request.method == 'POST':
        data = request.get_json()

        if not data: 
            return "데이터가 올바르지 않습니다", 400

        email = data.get('email')
        password = data.get('password')
        
        user = information.query.filter_by(email=email).first()
        

        if user and check_password_hash(user.password, password):
            session.clear()
            name = user.name
            session['session_user'] = user.email #세션에 id 저장
            
            return name, 200
        else:
            return "비밀번호가 일치하지 않습니다" ,401


# 이미지를 폴더에 저장(아직은 사용X)
@bp.route('image/', methods=['POST'])
def getImage():
        if request.method == 'POST':
            if 'image_file' not in request.files:
                return 'File is missing', 404
            
            image_file = request.files['image_file']
            
            if image_file.filename == '':
                return 'File is missing', 404
            
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))

            return "이미지 파일 전송 성공", 200

#운행 기록 받아서 서버에 저장
@bp.route('saveriderog/', methods=['POST'])
def saveRideRog():
    if request.method == 'POST':
        data = request.get_json()

        if not data: 
            return "데이터가 올바르지 않습니다", 400

        email = data.get('email')
        date = data.get('date')
        distance = data.get('distance')
        runtime = data.get('runtime')
        cost = data.get('cost')

        user = RideLog(email=email, date=date, distance=distance, runtime=runtime, cost=cost)
        db.session.add(user)
        db.session.commit()

        return "서버 저장 성공" , 201

#시동걸기
@bp.route('start/', methods=['POST'])
def start():
    data = request.get_json()

    if 'start' in data:
        if data['start'] == 'Start':
            initial_start_data['start'] = 'O'
            return 'O', 201
        elif data['start'] == 'Off':
            initial_start_data['start'] = 'X'
            return 'X', 202
        else:
            if initial_start_data['start'] == 'O':
                return 'O', 201
            else:
                return 'X', 202
    return "start가 안옴", 404

#개인정보 페이지 개인정보return
@bp.route('userinfo/', methods=['POST'])
def userinfo():
    if request.method == 'POST':
            # 현재 로그인한 사용자의 이메일 가져오기
            # html.views.py에서 생성한 세션은 인식하지 못하는 이슈가 있음
            # main.views.py의 singin/ 에서는 정상 동작
            user_email = session.get('session_user')  
            user_info = information.query.filter_by(email=user_email).first() 
            user_log = RideLog.query.filter_by(email=user_email).first()  
            if user_info and user_log:  
                user_data = {
                    'email': user_info.email,
                    'name': user_info.name,
                    'phone_number': user_info.phone_number,
                    'date': user_log.date,
                    'distance': user_log.distance,
                    'runtime': user_log.runtime,
                    'cost': user_log.cost,
                }

                return jsonify(user_data), 200
            else:
                return "사용자 정보를 찾을 수 없습니다.", 404

    return "잘못된 요청 메서드", 405

#사고 기록 받아서 서버에 저장
@bp.route('saveraccident/', methods=['POST'])
def saveAccident():
    if request.method == 'POST':
        accident_data = request.get_json()

        if not accident_data: 
            return "데이터가 올바르지 않습니다", 400

        date =  accident_data.get('date')
        latitude =  accident_data.get('latitude')
        longitude =  accident_data.get('longitude')
        count = accident_data.get('count')

        accident = Accident(date=date, latitude=latitude, longitude=longitude, count=count)
        db.session.add(accident)
        db.session.commit()

        return "서버 저장 성공" , 201

#전체 사고 기록 반환
@bp.route('sendaccident/', methods=['POST'])
def sendAccident():
    result = ""
    accidents = Accident.query.all()

    for accident in accidents:
        result += f"{accident.id} {accident.date} {accident.latitude} {accident.longitude} {accident.count}"

    return result

"""import io
import os
from torchvision import models
from PIL import Image as im
import torch.nn as nn
from torchvision import transforms
import torch
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, 'yolov5'))
model = torch.hub.load(FILES_DIR, 'custom', path=FILES_DIR+'/runs/train/exp4/weights/best.pt', source='local')

#헬멧 이미지 POST, 헬멧 결과 출력
#디버깅 모드 활성화 할 것, 리드미 확인
@bp.route('checkHelmet/', methods=['POST'])
def yolo():
    if request.method == 'POST':
        image = request.files['imageFile']
        im_bytes = image.read()
        im = Image.open(io.BytesIO(im_bytes))

        result = model(im)
        
        print(result)
        
        
        if "HelmetFace" in str(result):
            return "헬멧 감지 성공", 201
        
        if "onlyHelmet" in str(result):
            return "헬멧만 있음", 202

    return '헬멧 감지 실패', 404"""

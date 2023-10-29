# server

플라스크 환경변수
set FLASK_APP=kickboard

__init.py__ 파일 실행

설치 모듈
Flask    
Flask-Migrate
Flask-SQLAlchemy 
Flask-Login
Flask-Session

main_views: 안드로이드 스튜디오와 통신할 URL 
html_views: 테스트용 웹페이지

서버 컴퓨터(동욱컴) 실행 명령
flask run --host=220.69.208.119 --port=8000

디버깅 모드(print 출력 가능하게 함)
set FLASK_DEBUG=true

서버 모델 변경 시
flask db migrate
flask db upgrade
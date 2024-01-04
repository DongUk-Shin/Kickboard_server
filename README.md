# 2023 순천향대학교 공과대학 학술제 동상 수상
![이미지 (4)](https://github.com/karist7/kickboard_app/assets/49408613/fcbbf094-3c79-438f-89e0-7f0e8b2cb26a)
![슬라이드1](https://github.com/karist7/kickboard_app/assets/49408613/e9850620-7f64-4a2b-b6e2-e424c65c6c5e)
![슬라이드2](https://github.com/karist7/kickboard_app/assets/49408613/8493198d-62b2-4f8d-bd9b-1a5a4dc64f27)
![슬라이드3](https://github.com/karist7/kickboard_app/assets/49408613/b3801689-a04e-4f94-809a-4c8bbb034aa4)
![슬라이드4](https://github.com/karist7/kickboard_app/assets/49408613/631253ef-fb70-486f-9ef5-abc790631257)
![슬라이드5](https://github.com/karist7/kickboard_app/assets/49408613/2213b1f2-fe78-4924-8369-458688adc8af)
![슬라이드6](https://github.com/karist7/kickboard_app/assets/49408613/ae660aa5-bf1d-41ab-9a08-ce224a0176f2)
![슬라이드7](https://github.com/karist7/kickboard_app/assets/49408613/84a44e1e-b771-4f6c-97aa-f52cef755b07)
![슬라이드8](https://github.com/karist7/kickboard_app/assets/49408613/6ed02ede-5c40-4f65-8837-dc73ea58ad7e)
![슬라이드9](https://github.com/karist7/kickboard_app/assets/49408613/26065b70-1688-484e-944d-896dc34e079a)
---
<p data-ke-size="size16" style="text-align: left;">개발환경: </p>
<blockquote data-ke-style="style3">
  App: Android Studio / Java
 <br>Server: Flask / Python 
 <br>Object-Detection: Yolov5 / Python 
 
</blockquote>
<p data-ke-size="size16" style="text-align: left;"> <br>App 페이지:</p>
<blockquote data-ke-style="style2"> <a href="https://github.com/SCH-OOPSLA-LAB/kickboard_app" target="_blank"><span>https://github.com/SCH-OOPSLA-LAB/kickboard_app</span></a> 
</blockquote>
<p data-ke-size="size16" style="text-align: left;"> </p></div>

## 사용 방법
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

서버 컴퓨터 실행 명령
flask run --host=220.69.208.119 --port=8000

디버깅 모드(print 출력 가능하게 함)
set FLASK_DEBUG=true

``
서버 모델 변경 시
flask db migrate
flask db upgrade

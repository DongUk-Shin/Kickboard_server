from kickboard import db

#회원정보 클래스
class information(db.Model):
    email = db.Column(db.Text, primary_key=True)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    
#운행 기록 클래스
class RideLog(db.Model):
    email = db.Column(db.Text, primary_key=True)
    date = db.Column(db.Text)
    distance = db.Column(db.Text)
    runtime = db.Column(db.Text)
    cost = db.Column(db.Text)
    
#사고 위치 클래스
class Accident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    latitude = db.Column(db.Float) #위도
    longitude = db.Column(db.Float) #경도.
    count = db.Column(db.Integer)
    


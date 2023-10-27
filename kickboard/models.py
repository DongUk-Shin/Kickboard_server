from kickboard import db

class information(db.Model):
    #unique=True: 같은 값 저장 x
    user_id = db.Column(db.Text, unique=True, primary_key=True)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    birth = db.Column(db.Text)
    call = db.Column(db.Text)
    
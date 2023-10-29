from kickboard import db

class information(db.Model):
    email = db.Column(db.Text, primary_key=True)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    
class RideLog(db.Model):
    email = db.Column(db.Text, primary_key=True)
    date = db.Column(db.Text)
    distance = db.Column(db.Text)
    runtime = db.Column(db.Text)
    cost = db.Column(db.Text)
    
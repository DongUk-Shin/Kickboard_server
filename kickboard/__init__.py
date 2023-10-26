from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

#객체 생성
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)



@app.route('/')
def default():
    return redirect('/main')

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        name = request.form['name']
        birth = request.form['birth']
        call = request.form['call']

        from .models import information
        user = information(user_id=user_id, password=password, name=name, birth=birth, call=call)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
    #app.run(host="220.69.208.119", port=8000, debug=True)
    app.run(port=8000, debug=True)

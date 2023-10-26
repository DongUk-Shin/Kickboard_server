from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/login/')
def login():
    return render_template("main.html")


if __name__ == '__main__':
    #app.run(host="220.69.208.119", port=8000, debug=True)
    app.run(port=8000, debug=True)

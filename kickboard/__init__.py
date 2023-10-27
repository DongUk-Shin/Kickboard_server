from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

#객체 생성
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = 'abcde'

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import html_views
    app.register_blueprint(html_views.bp)
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

if __name__ == '__main__':
    #app.run(host="220.69.208.119", port=8000, debug=True)
    app = create_app()
    app.run(port=8000, debug=True)

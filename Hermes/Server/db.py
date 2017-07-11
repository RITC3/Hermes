from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
init = False

def create_db(app):
    global db, init

    if not init:
        db.app = app
        db.init_app(db.app)
        db.create_all()

        init = True
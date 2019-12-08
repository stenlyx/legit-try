from db import db
from app import app
from ma import ma

db.init_app(app)
ma.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

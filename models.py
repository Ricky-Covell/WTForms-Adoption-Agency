from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"


def connect_db(app):
    '''Connects this database to Flask app'''
    db.app = app
    db.init_app(app)


# # # # # # # # # # # # # # # # MODELS # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class Pet(db.Model):
    '''Table of pets up for adoption'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    



    

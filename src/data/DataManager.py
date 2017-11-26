from flask_sqlalchemy import *
from src.data.DataDefintions import *

class DataManager():

    def __init__(self, db):
        self.engine = db.engine
        self.DBsession= db.session

    def add_user(self, first, last):
        session = self.DBsession()
        new_user = User(FirstName=first, LastName=last)
        session.add(new_user)
        session.commit()
        session.close()

    def get_users(self):
        session = self.DBsession()
        result = session.query(User).all()
        session.close()
        return result
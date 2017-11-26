from sqlalchemy import *

from FlaskApp import db


#flask_sqlalchemy essentially creates tables as classes.
#HEre we define all the table/classes we want and their propeties
#makes queying and accessing attributes a lot easier
class User(db.Model):
    __tablename__ = 'USER'
    ID = Column(Integer, primary_key=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    userImage = Column(String, nullable=True)
    SocPos = Column(String, nullable=True)
    GamesPlayed = Column(Integer, nullable=False, default=0)
    GamesWon = Column(Integer, nullable=False, default=0)
    GamesLost = Column(Integer, nullable=False, default=0)
    TotalPoints = Column(Integer, nullable=False, default=0)
    MoonsShot = Column(Integer, nullable=False, default=0)



    def getID(self):
        return self.ID

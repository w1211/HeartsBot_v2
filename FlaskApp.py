from flask import *
from flask_sqlalchemy import SQLAlchemy
from src.game import *
import os

#########################################################
##                                        Globals init ##
#########################################################
#Slightly hacky, essentially creating the app and database as global variables
from src.game.GameSys import GameSys

app = Flask(__name__)

# tell app where to find the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'resources/database/heartsBot.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # can't remember what exactly this does but creates a
                      # database object for flask to use

from src.data.DataManager import * #import here so that the tables are parsed first

db.create_all()  # create all the tables associated with db (db.Model passed as base class to all our
                 # sql_alch table classes
db.session.commit()


#########################################################
##                                             Routes  ##
#########################################################
# when you navigate directly to a page, flask will look for which func to run using route
@app.route('/')
def home():
    return render_template('home.html', game_started = game_sys.get_game_Started())


@app.route('/review_players')
def review_players():
    res = dm.get_users()
    return render_template('review_players.html', users=res)

@app.route('/game')
def game():
    if(game_sys.get_game_Started()):
        return render_template('game.html', users=dm.get_users()) #temp, replace with actual players when game object deved
    else:
        return render_template('new_game.html', users=dm.get_users())

# Run code
if __name__ == '__main__':
    dm = DataManager(db)
    game_sys = GameSys()
    #dm.add_user('Test2','Person2')
    #print(dm.get_users())
    app.run(debug=True, port=8089)



class GameSys():
    def __init__(self):
        self._game_started = False


    def start_game(self, player):
        self._game_started = True

    def get_game_Started(self):
        return self._game_started
class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, player):
        self.players.append(player) 


    def has_player(self,player):
        if player in self.players:
            return True
    
        return False
        # for player in self.player:
            # if player == player
            # return True
            # not complette code but this can work
    

        
    
    def play_game(self,has_won):
        if has_won:
            self.points += 3


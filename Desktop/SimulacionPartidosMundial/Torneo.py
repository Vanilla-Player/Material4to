



class Match:
  def __init__(self, team1, team2):
    self.team1 = team1
    self.team2 = team2



    def SimulateMatch(self):
        lambda1 = team1.xG*(team1.elo/team2.elo)
        lambda2 = team2.xG*(team2.elo/team1.elo)

        

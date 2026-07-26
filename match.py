#match.py
""" dar in file class match ghara darad """

from team import Team 

class Match:
    """sharh mosabegheh bin do tim """
    def __init__(self, team1, team2, is_knockout= False):
        """meghdardehi avalyeh"""
        self.team1 = team1
        self.team2 = team2
        self.goals1 = 0
        self.goals2 = 0
        self.is_knockout = is_knockout
        self.winner = None
    
    def play(self):
        """anjam mosabegheh va zakhire natayej"""
        self.goals1, self.goals2, self.winner = self.team1.simulate_match(
             self.team2,
            self.is_knockout
        )
 

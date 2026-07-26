#group.py
""" class group gharar darad """

from match import Match

class Group:
     """modiriat tamame kar haye yek goroh"""

     def __init__(self, name):
         self.name = name
         self.teams = []

     def play_all_matches(self):
          """anjame tamame mosabegheh haye gorohi bedone tekrar"""
          #ejraye tamame mosabeghat bedone tekrar
          for i in range(len(self.teams)):
              for j in range(i + 1, len(self.teams)):
                 
                  #sakhte yek mosabeghe beyn do tim
                  game = Match(self.teams[i], self.teams[j])
                  #ejraye mosabeghe va sabt nataije
                  game.play()

     def get_ranking(self):
         """ moratab sazi tim haye goroh """
         return sorted(
             self.teams,
             key=lambda team: (
                 team.points,
                 team.goal_difference(),
                team.goals_for
             ),
             reverse= True    #agar neveshteh nashavad khoroji az kam be ziad moratab mishavad
         )
     def advance_teams(self):
         """bargardandane do teame goroh"""

         #daryafte jadvale maratab shodeh goroh
         ranking = self.get_ranking()
         return ranking[0], ranking[1]

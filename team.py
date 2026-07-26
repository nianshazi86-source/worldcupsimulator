#team.py
""" der in file class team gharar darad """

import numpy as np 


class Team:
    """Team class: stores a national teams ratings (attack, defense, rank) and its running tournament statistics"""
    def __init__(self, name, attack, defense, rank):
        """meghdardehi etelaate tim"""

        self.name = name
        self.attack = attack
        self.defense = defense
        self.rank = rank

        self.goals_for = 0 
        self.goals_against = 0
        self.points = 0 
        self.group = None

        self.last_penalty_goals = 0
        self.last_opponent_penalty_goals = 0 

    def goal_difference(self):
        """return the goal difference."""
        return self.goals_for - self.goals_against
    
    def reset_stats(self):
        """reset tournament statistics"""
        self.goals_for = 0 
        self.goals_against = 0 
        self.points = 0 
            
    def simulate_match(self, opponent, is_knockout=False):
         """shabih sazi mosabeghe beyn do tim"""

         # mohasebe gol haye mored entezar baraye har tim
         self_lambda = (self.attack / 100) * 1.5 + (1 - opponent.defense / 100) * 0.8
         opponent_lambda = (opponent.attack / 100) * 1.5 + (1 - self.defense / 100) * 0.8

         # tolid gol ba estefade az tozie Poisson
         self_goals = np.random.poisson(self_lambda)
         opponent_goals = np.random.poisson(opponent_lambda)

         # marhale gorohi
         if not is_knockout:

             if self_goals > opponent_goals:
                 self.points += 3
                 winner = self

             elif self_goals < opponent_goals:
                 opponent.points += 3
                 winner = opponent

             else:
                  # dar mosavi har do tim yek emtiaz migirand
                  self.points += 1
                  opponent.points += 1
                  winner = None

         # marhale hazfi
         else:

              if self_goals > opponent_goals:
                  winner = self

              elif self_goals < opponent_goals:
                  winner = opponent

              else:
                  # vaqt ezafe (30 min)
                  self_goals += np.random.poisson(self_lambda * 0.3)
                  opponent_goals += np.random.poisson(opponent_lambda * 0.3)

                  if self_goals > opponent_goals:
                     winner = self

                  elif self_goals < opponent_goals:
                     winner = opponent

                  else:
                     # zarbat penalty
                     winner, _, _ = self.penalty_shootout(opponent)

         # berozresani amar gol haye har do tim
         self.goals_for += self_goals
         self.goals_against += opponent_goals

         opponent.goals_for += opponent_goals
         opponent.goals_against += self_goals

         # bargasht natije mosabeghe
         return self_goals, opponent_goals, winner
    
    def penalty_shootout(self, opponent):
        """shabih sazi zarabat penalti"""
        self_penalties = 0
        opponent_penalties = 0

        #5 penalti aval
        for _ in range(5):
            if np.random.rand() < 0.75:
                self_penalties += 1

            if np.random.rand() < 0.75:
                opponent_penalties += 1

        
        while self_penalties == opponent_penalties:
            self_score = np.random.rand() < 0.75
            opponent_score =np.random.rand() < 0.75

            if self_score and not opponent_score:
                self_penalties += 1
            elif opponent_score and not self_score:
                opponent_penalties += 1

        if self_penalties > opponent_penalties:
            winner = self
        else:
            winner = opponent

        return winner, self_penalties, opponent_penalties
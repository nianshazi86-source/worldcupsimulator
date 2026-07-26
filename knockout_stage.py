#knockout_stage.py
""" class knochout_stage inga gharar darad """

class knockoutstage:
    """modiriate marahele hazfi"""
    def __init__(self, round_name, matches):
        #name marhale hazfi
        self.round_name = round_name
        #list masabaghate in marhale     
        self.matches = matches 

    def play_round(self):
        """ anjame tamame mosabeghat dar marhale hazfi"""

        #bargozari tamame mosabeghate marhale
        for match in self.matches:
            match.play()

    def get_winners(self):
        """ bargardandan list tim haye barandeh in marhaleh hazfi """

        #ijad list baraye zakhireh tim haye barandeh
        winners = []

        #ezafeh kardan barandeh har mosabegheh be in list
        for match in self.matches:
            winners.append(match.winner)
        return winners
        
    def display_results(self):
        """ chape natayeje marhaleh hafi"""
        #chape name marhale
        print(f"\n{self.round_name}")
        #chape natijeh har marhaleh
        for match in self.matches:
            print(
                f"{match.team1.name} {match.goals1} - {match.goals2} {match.team2.name}" 
            )
        #chape barandeh har mosabegheh
        print("\nWinners:")
        for winner in self.get_winners():
            print(winner.name)
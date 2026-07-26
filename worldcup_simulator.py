#worldcup_simulator.py
""" class worldcup_simulator dar inga gharar darad """

from team import Team
from group import Group
from match import Match
from knockout_stage import knockoutstage

class WorldCupSimulator: 
    """ class asli baraye shabih sazi jam jahani """
    def __init__(self):
        """ rah andazi avalyeh jam jahani """
        #list tamam goroh ha
        self.teams = []

        #list goroh ha
        self.groups = []

        #marahele hazfi
        self.round_of_16 = None
        self.quarterfinals = None
        self.semifinals = None
        self.final = None

        #ghahraman mosabeghat
        self.champion = None

    def load_teams_from_csv(self, filename):
        """ khandane etelaate tim ha az faile csv va sakhte list ashya """
        self.teams = []
        #baz kardan fail csv
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            #rad kardane satre onvane fail
            next (reader)
            #peymayesh tamame satr haye file
            for row in reader:
                #sakht yek shey az class Time
                team = Team(
                    row[0],
                    int(row[1]),
                    int(row[2]),
                    int(row[3]),
                )
                #ezafeh kardane tim be list tim ha
                self.teams.append(team)

    def seed_and_draw_groups(self):
        """ghoreh keshi goroh ha bar asas seedbandi rankikng fifa"""
        #khali kardane list goroh ha
        self.groups = []
        group_names = ["A","B", "C", "D", "E", "F", "G", "H"]
        #sakhtane goroh ha
        for name in group_names:
            self.groups.append(Group(name))

        #moratab kardane tim ha bar asase rank fifa
        self.teams.sort(key=lambda team: team.rank)

        #taghsime tim ha be chahar seed
        pot1 = self.teams[0:8]
        pot2 = self.teams[8:16]
        pot3 = self.teams[16:24]
        pot4 = self.teams[24:32]

        #makhlot kardane tim haye har seed
        random.shuffle(pot1)
        random.shuffle(pot2)
        random.shuffle(pot3)
        random.shuffle(pot4)

        #gharar dadane yek tim az har seed dar har goroh
        for i in range(8):
            #ezafeh kardane tim hayeh seed aval ta chaharom be goroh 
            self.groups[i].teams.append(pot1[i])
            self.groups[i].teams.append(pot2[i])
            self.groups[i].teams.append(pot3[i])
            self.groups[i].teams.append(pot4[i])
            #sabte goroh har tim
            pot1[i].group = self.groups[i]
            pot2[i].group = self.groups[i]
            pot3[i].group = self.groups[i]
            pot4[i].group = self.groups[i]

    def run_group_stage(self):
        """ ejraye marhele ye gorohi va namayeshe jadvale har goroh"""

    # ejraye mosabeghate hameye goroh ha
        for group in self.groups:
            print(f"\n========== Group {group.name} ==========")
        # anjame tamame mosabeghate goroh
            group.play_all_matches()

        # namayeshe jadvale goroh
            ranking = group.get_ranking()
            print("\nTable:")
            for team in ranking:
                print(
                    f"{team.name} | "
                    f"Points: {team.points} | "
                    f"GF: {team.goals_for} | "
                    f"GA: {team.goals_against} | "
                    f"GD: {team.goal_difference()}"
                )
       
    def setup_knockout_bracket(self):
         """sakhte marhale berakete hazfi bar asae ghavanine fifa"""
         # garaftane do time avale har goroh
         qualified_teams = []

         for group in self.groups:
            first_team, second_team = group.advance_teams()
            qualified_teams.append((first_team, second_team))
         #sakhte mosabeghate marhale yek hashtome nahaea
         matches = [
             Match(qualified_teams[0][0], qualified_teams[1][1], True),  # A1 vs B2
             Match(qualified_teams[2][0], qualified_teams[3][1], True),  # C1 vs D2
             Match(qualified_teams[4][0], qualified_teams[5][1], True),  # E1 vs F2
             Match(qualified_teams[6][0], qualified_teams[7][1], True),  # G1 vs H2

             Match(qualified_teams[1][0], qualified_teams[0][1], True),  # B1 vs A2
             Match(qualified_teams[3][0], qualified_teams[2][1], True),  # D1 vs C2
             Match(qualified_teams[5][0], qualified_teams[4][1], True),  # F1 vs E2
             Match(qualified_teams[7][0], qualified_teams[6][1], True)   # H1 vs G2
         ]

         #sakhte marhaleh ye yek hashtome nahaea
         self.round_of_16 = knockoutstage ("Round of 16", matches)
         #namayeshe payame movafaghyat
         print("\n marhaleh ye yek hashtome nahaea sakhteh shod")

    def run_knockout_stage(self):
        """ ejraye marahele hazfi ta yek chaharome nahaea """
        # ejraye mosabeghate marhale yek hashtome nahaea
        self.round_of_16.play_round()
        # namayashe natayeje marhale yek hashtome
        self.round_of_16.display_results()
        # gereftane tim haye barandeh marhaleh
        winners = self.round_of_16.get_winners()
        # sakhteh mosabeghate marhaleh yek chaharom
        quarter_matches = [
            Match(winners[0], winners[1], True),
            Match(winners[2], winners[3], True),
            Match(winners[4], winners[5], True),
            Match(winners[6], winners[7], True)
        ]
        # sakhteh marhaleh yek chaharome nahaea
        self.quarterfinals = knockoutstage("Quarterfinals", quarter_matches)
        # ejraye marhale yek chaharome
        self.quarterfinals.play_round()
        # namayeshe natayeje marhaleh
        self.quarterfinals.display_results()

    def run_knockout_stage(self):
         """ejraye tamame marhale haye hazfi ta taein ghahreman"""

         #Round Of 16
         print("\n========== Round Of 16 ==========")
         #ejraye tamame mosabeghat
         self.round_of_16.play_round()

         #namayesh natayej mosabeghat
         self.round_of_16.display_results()

         #gereftan tim haye barandeh
         winners = self.round_of_16.get_winners()

         #Quarterfinals
         quarter_matches = []

         #sakhte mosabeghat marhaleh
         for i in range(0, len(winners), 2):
             quarter_matches.append(
                 Match(winners[i], winners[i + 1], True)
             )

         self.quarterfinals = knockoutstage("Quarterfinals", quarter_matches)

         print("\n========== Quarterfinals ==========")
         
         #ejraye yek chaharome nahaea
         self.quarterfinals.play_round()
         #namayesh natayej
         self.quarterfinals.display_results()

         winners = self.quarterfinals.get_winners()

         # Semifinals
         semi_matches = []

         for i in range(0, len(winners), 2):
             semi_matches.append(
                 Match(winners[i], winners[i + 1], True)
             )

         self.semifinals = knockoutstage("Semifinals", semi_matches)

         print("\n========== Semifinals ==========")

         self.semifinals.play_round()
         self.semifinals.display_results()

         winners = self.semifinals.get_winners()

         #  Final
         final_matches = [
             Match(winners[0], winners[1], True)
         ]

         self.final = knockoutstage("Final", final_matches)

         print("\n========== Final ==========")

         self.final.play_round()
         self.final.display_results()

         self.champion = self.final.get_winners()[0]

         print(f"\n Champion: {self.champion.name}")

    def run_full_simulation(self):
        """ejraye yek dore kamel az jam jahani"""

        # reset kardan amar tamame tim ha
        for team in self.teams:
         team.reset_stats()

        # pak kardan goroh haye ghabli
        self.groups = []

        # goroh bandi mojadad
        self.seed_and_draw_groups()

        # ejraye marhale gorohi
        self.run_group_stage()

        # sakhte bracket hazfi
        self.setup_knockout_bracket()

        # ejraye marhale hazfi
        self.run_knockout_stage()

        # bargardandan ghahreman
        return self.champion

    def most_likely_champion(self, num_simulations=1000):
        """mohasebe darsade ghahremani har tim"""
    
        # dictionary baraye zakhire tedad ghahremani har tim
        champions = {}

        # ejraye chandbare shabih sazi
        for _ in range(num_simulations):
            champion = self.run_full_simulation()

            # ezafe kardan tedad ghahremani
            if champion.name in champions:
                champions[champion.name] += 1
            else:
             champions[champion.name] = 1

        print("\n===== Championship Probability =====")

        # mohasebe darsad ghahremani
        for team, count in sorted(
               champions.items(),
               key=lambda item: item[1],
               reverse=True
        ):
            probability = (count / num_simulations) * 100
            print(f"{team}: {probability:.2f}%")
            
    def display_bracket(self):
        """namayeshe bracket akharin shabih sazi"""

        print("\n========== Knockout Bracket ==========")

        # namayeshe Round Of 16
        if self.round_of_16:
          print("\nRound Of 16")
          self.round_of_16.display_results()

        # namayeshe Quarterfinals
        if self.quarterfinals:
         print("\nQuarterfinals")
         self.quarterfinals.display_results()

        # namayeshe Semifinals
        if self.semifinals:
            print("\nSemifinals")
            self.semifinals.display_results()

        # namayeshe Final
        if self.final:
         print("\nFinal")
         self.final.display_results()

        # namayeshe ghahreman
        if self.champion:
         print(f"\n Champion : {self.champion.name}")
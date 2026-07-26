#main.py
""" menoye asli injas """

from worldcup_simulator import WorldCupSimulator

def main():
    """"menu asli barname"""

    simulator = WorldCupSimulator()

    # load kardan file team ha
    simulator.load_teams_from_csv("Worldcup_2026_teams.txt")

    while True:

        print("\n========== World Cup 2026 ==========")
        print("1. Run One Simulation")
        print("2. Championship Probability")
        print("3. Display Last Bracket")
        print("4. Exit")

        # gereftan entekhab karbar
        choice = input("\nEnter your choice: ")

        if choice == "1":

             # ejraye yek dore kamel az jam jahani
             simulator.run_full_simulation()

        elif choice == "2":

             # mohasebe darsad ghahremani tim ha
            simulator.most_likely_champion()

        elif choice == "3":

             # namayeshe bracket akharin shabih sazi
             simulator.display_bracket()

        elif choice == "4":

             # khoroj az barname
            print("\nGood Bye...")
            break

        else:

             # payam baraye vorodi eshtebah
             print("\nInvalid Choice!")

#noghte shoroo barnameh
if __name__ == "__name__":
    main()
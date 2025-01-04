# Fort Boyard Simulation : Lola Lievain-Thibaut ; Emeline Unmar
# Implementation of the utility functions

def introduction():
    # Prints the introduction and game rules
    print("Welcome to the Game!")
    print("--------------------------------------------------")
    print("Game Rules:")
    print("• You must complete challenges to earn keys.")
    print("• The goal is to collect three keys to unlock the treasure room.")
    print("• Each successful challenge brings you closer to the treasure.")
    print("Good luck, and let the adventure begin!")
    print("--------------------------------------------------")

def compose_equipe():
    team = []
    while True:  # Continuously ask for input until valid number is provided
        try:
            n = int(input("Enter the number of players: "))
        except ValueError:  # Handle invalid input 
            print("Error: Please enter a valid number.")
            continue
        if 1 > n or n > 3:  # Ensure the number of players is between 1 and 3
            print("Error: Please enter a number between 1 and 3.")
            continue
        break  # Break the loop if valid input is provided
    for i in range(n):  # Loop through number of players
        print(f"Enter details for Player {i + 1}:")
        name = input("Name: ").strip()
        profession = input("Profession: ").strip()  
        while True:
            leader_response = input("Is this player the team leader? (yes/no): ").strip().lower() 
            if leader_response in ("yes", "no"):
                is_leader = leader_response == "yes" 
                break
            else:
                print("Error: Please answer 'yes' or 'no'.")
        
        # Create a dictionary for each player
        player = {
            "name": name,
            "profession": profession,
            "is_leader": is_leader,
            "keys_won": 0  
        }
        team.append(player)

    # Ensure at least one player is set as the leader
    if not any(player["is_leader"] for player in team):
        print("No leader was designated. The first player will be assigned as the leader.")
        team[0]["is_leader"] = True

    return team

def challenges_menu():
    while True:  # Continuously ask for input until a valid choice is made
        try:
            choice = int(input(
                "Choose a challenge:\n"
                "1. Mathematics Challenge\n"
                "2. Logic Challenge\n"
                "3. Chance Challenge\n"
                "4. Père Fouras's Riddles\n"
                "Enter your choice: "))
        except ValueError:  # Handle invalid input
            print("Error: Please enter a valid number.")
            continue
        if not 1 <= choice <= 4:  # Ensure the choice is between 1 and 4
            print("Error: Please choose a number between 1 and 4.")
            continue
        break  # Break the loop if valid input is provided
    return choice

def choose_player(team):
    i = 1
    for player in team:  # List the players in the team with their role
        print(f"{i}. {player['name']} ({player['profession']}) - {'Leader' if player['is_leader'] else 'Member'}")
        i += 1
    
    while True:  # Continuously ask for input until a valid player is chosen
        try:
            player_number = int(input("Enter the number of the player you want to choose: "))
        except ValueError:  # Handle invalid input (non-integer)
            print("Error: Please enter a valid number.")
            continue
        if not 1 <= player_number <= len(team):  # Ensure the chosen number is valid
            print("Error: Please choose a number between 1 and {}".format(len(team)))
            continue
        break  # Break the loop if valid input is provided
    selected_player = team[player_number - 1]  # Get the selected player from the list
    return selected_player

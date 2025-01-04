

# Function to display the introduction message at the start of the game
def introduction():
    print("Welcome to the Game!")  
    print("--------------------------------------------------")
    print("Game Rules:")
    print("• You must complete challenges to earn keys.")  
    print("• The goal is to collect three keys to unlock the treasure room.")  
    print("• Each successful challenge brings you closer to the treasure.")  
    print("Good luck, and let the adventure begin!")  
    print("--------------------------------------------------")

# Function to allow the user to compose their team
# Returns a list of player dictionaries with player details
def compose_equipe():
    team = []  
    n = int(input("Enter the number of players: "))  
    while 1 > n or n > 3:  
        n = int(input("Error, please enter a number between 1 and 3: "))  
    
    # Loop to gather details for each player
    for i in range(n):
        print(f"Enter details for Player {i + 1}:")
        name = input("Name: ").strip()  
        profession = input("Profession: ").strip()  
        
        # Ask if the player is the team leader and ensure valid response
        while True:
            leader_response = input("Is this player the team leader? (yes/no): ").strip().lower()
            if leader_response in ("yes", "no"):
                is_leader = leader_response == "yes"  # Boolean to determine if player is leader
                break
            else:
                print("Error: Please answer 'yes' or 'no'.")  # Error handling for invalid response

        # Create a player dictionary with their details
        player = {
            "name": name,
            "profession": profession,
            "is_leader": is_leader,
            "keys_won": 0  
        }
        team.append(player)  

    # If no leader was assigned, the first player is set as the leader
    if not any(player["is_leader"] for player in team):  # Check if a leader exists
        print("No leader was designated. The first player will be assigned as the leader.")
        team[0]["is_leader"] = True  

    return team  

# Function to display the challenge menu and get the player's choice
# Returns the chosen challenge option as an integer
def challenges_menu():
    print("Choose a challenge:")
    print("1. Mathematics Challenge")  
    print("2. Logic Challenge")  
    print("3. Chance Challenge")  
    print("4. Père Fouras's Riddles")  
    
    choice = int(input("Enter your choice: "))  
    while choice not in {1, 2, 3, 4}:  # Input validation to ensure valid choice
        choice = int(input("Error: Please choose a number between 1 and 4: "))  
    
    return choice  

# Function to allow the user to choose a player from the team
# Parameter: team (list) - List of players
# Returns the selected player dictionary
def choose_player(team):
    i = 1
    for player in team:
        print(f"{i}. {player['name']} ({player['profession']}) - {'Leader' if player['is_leader'] else 'Member'}")
        i += 1
    
    player_number = int(input("Entrez le numéro du joueur: "))
    selected_player = team[player_number - 1]
    return selected_player

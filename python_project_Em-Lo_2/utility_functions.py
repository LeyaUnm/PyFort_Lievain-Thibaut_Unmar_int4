def introduction():
    print("Welcome to the Game!")
    print("--------------------------------------------------")
    print("Game Rules:")
    print("• You must complete challenges to earn keys.")
    print("• The goal is to collect three keys to unlock the treasure room.")
    print("• Each successful challenge brings you closer to the treasure.")
    print("Good luck, and let the adventure begin!")
    print("--------------------------------------------------")

def compose_equipe() :
    team = []
    n = int(input("Enter the number of players: "))
    while 0 > n or n > 3 :
        n = int(input("Error, please enter a number between 1 and 3: "))
    for i in range(n) :
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

        player = {
            "name": name,
            "profession": profession,
            "is_leader": is_leader,
            "keys_won": 0
        }
        team.append(player)

    if not any(player["is_leader"] for player in team):
        print("No leader was designated. The first player will be assigned as the leader.")
        team[0]["is_leader"] = True

    return team

def challenges_menu() :
    print("Choose a challenge:")
    print("1. Mathematics Challenge")
    print("2. Logic Challenge")
    print("3. Chance Challenge")
    print("4. Père Fouras's Riddles")
    choice = int(input("Enter your choice: "))
    while choice not in {1, 2, 3, 4}:
            choice = int(input("Error: Please choose a number between 1 and 4: "))
    return choice

def choose_player(team):
    i = 1
    for player in team:
        if player['role'] == 'Leader':
            role = 'Leader'  
        else :
            role = 'Member'
        print(f"{i}. {player['name']} ({player['profession']}) - {role}")
        i += 1
    
    player_number = int(input("Entrez le numéro du joueur: "))
    selected_player = team[player_number - 1]
    return selected_player

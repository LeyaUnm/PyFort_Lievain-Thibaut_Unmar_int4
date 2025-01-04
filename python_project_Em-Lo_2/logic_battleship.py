# Fort Boyard Simulation : Lola Lievain-Thibaut ; Emeline Unmar
# Implementation of the battleship challenge's function

from random import randint

def next_player(player):
    return [1,0][player] # Changes the player

def empty_grid():
    return [[" ", " ", " "], # Initialize the grid
            [" ", " ", " "],
            [" ", " ", " "]]

def display_grid_ship(grid, message): # Display function
    print(message)
    print(f"{grid[0][0]} | {grid[0][1]} | {grid[0][2]}\n{grid[1][0]} | {grid[1][1]} | {grid[1][2]}\n{grid[2][0]} | {grid[2][1]} | {grid[2][2]}")
    print("---------")

def ask_position():

    play = input("Enter a position (line, column) between 1 and 3 (ex: 1,2) : ")
    valid = 0

    while not valid:  # Verify that the input is correct

        valid = (len(play) == 3 and play[0] in '123' and play[1] == ',' and play[2] in '123')  # Verify that the input is the correct format
        if not valid: # If input is incorrect, ask gain
            print("Incorrect position, try again.")
            play = input("Enter a position (line, column) between 1 and 3 (ex: 1,2) : ")

    return int(play[0]), int(play[2])

def initialize():

    boats = 2
    grid = empty_grid()

    while boats > 0: # While there is a boat to place

        # Ask the player where he wants to place his boat
        print("Where do you want to place your boat ?")
        print("Boat ", 3-boats) # Boat number
        coords = ask_position()

        if grid[coords[0]-1][coords[1]-1] == " ": # If the emplacement is free, place a boat
            grid[coords[0]-1][coords[1]-1] = "B"
            boats -= 1

        else:
            print("Incorrect position, try again.")

    display_grid_ship(grid, "Here is the grid with your ships")
    return grid

def has_won(grid):
    return sum(grid[i][j] == "X" for i in range(3) for j in range(3)) == 2 # Check if there are two X, is yes then there is a win

def turn(player, player_grid, player_shots_grid, opponent_grid): # Added player_grid as well because I found it to be the easiest way to do so.

    if player:

        print("The master will now play.")

        places = [(i,j) for i in range(3) for j in range(3) if player_grid[i][j] in [" ", "B"]] # Moves the master didnt already picked
        pick = places[randint(0, len(places)-1)] # Pick random place to shot
        print(f"The master shoots in {pick[0]+1},{pick[1]+1}")

        if player_grid[pick[0]][pick[1]] == "B": # If the master shot a boat, place an X on the player grid
            player_grid[pick[0]][pick[1]] = "X"
            print("Hit ! The master has sunk your boat.")

        else: # If the master shot a boat, place a dot (.) on the player grid
            player_grid[pick[0]][pick[1]] = "."
            print("Ploup ! The master missed.")

        display_grid_ship(player_grid, "Here is the grid with your ships.")

    else:

        print("Your turn.")
        pos = ask_position()
        print(f"You shoot on the position {pos[0]},{pos[1]}")

        if opponent_grid[pos[0]-1][pos[1]-1] == "B": # If you shot a boat, add an X on your shot grid
            player_shots_grid[pos[0]-1][pos[1]-1] = "X"
            print("Hit ! You have sunk the master's boat.")

        else: # If you missed, add a dot on your shot grid
            player_shots_grid[pos[0]-1][pos[1]-1] = "."
            print("Ploup... You missed.")

        display_grid_ship(player_shots_grid, "Here is the grid with your shots.")

def master_initialize():

    grid = empty_grid()
    places = [(i, j) for i in range(3) for j in range(3)] # Every usable place for the boats
    boat1 = places.pop(randint(0, len(places)-1)) # Take a random localisation and removes it from the usable places
    boat2 = places[randint(0, len(places)-1)] # Take a random localisation from the usable ones

    # Places the boats on the randomly chosen positions
    grid[boat1[0]][boat1[1]] = "B"
    grid[boat2[0]][boat2[1]] = "B"

    return grid

def battleship_game(): #Main

    print("You and the master will each recieve a 3x3 grid to place your ships.\n"
          "You will take turns in shooting each others' ships.\n"
          "The first one to sink both of their opponent's ships wins.")

    # Initialise grids for the player and the master
    player_grid = initialize()
    player_shots_grid = empty_grid()
    master_grid = master_initialize()

    player = 0 # 0:Player, 1:Master

    while not (has_won(player_grid) or has_won(player_shots_grid)): # While none has won

        turn(player, player_grid, player_shots_grid, master_grid) # Do a turn
        player = next_player(player) # Switch player turn

    if player: # Determine who won, the winner is the inverse from player since we switched after the end of the round
        print("You have sunk both of the master's ships! You win!")
        return True
    else:
        print("All of your boats have been sunken. You lose.")
        return False

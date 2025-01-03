def next_player(player):
    return(1-player)

def empty_grid():
    return ([[" " for _ in range(3)] for _ in range(3)])

def display_grid(grid, message):
    print(message)
    l = ""
    for row in grid:
        for column in row:
            l += "|" + column
        print(l)
        l = ""
    print("-" * 7)


    """display_grid(grid, message) : This function takes two parameters:
o grid: A 2D list representing the grid.
o message: A string that provides context for the grid, such as "Reminder of the
history of the shots you have made:" or "Discover your game grid with your
boats:".
It displays the given message followed by the grid, line by line. Grid cells are
separated by vertical bars (|), and a border is drawn below the grid for clarity. This
function is used to display either the player's shot history or the positions of boats
placed at the start of the game."""

def ask_position():
    pass



def initialize():
    pass

def turn(player, player_shots_grid, opponent_grid):
    pass

def has_won(player_shots_grid):
    pass

def battleship_game():
    pass

display_grid(empty_grid(), "Empty grid")
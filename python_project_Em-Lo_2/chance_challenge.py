# Fort Boyard Simulation : Lola Lievain-Thibaut ; Emeline Unmar
# Implementation of chance challenge's functions

from random import randint

def shell_game(): #Easy
    print("You will play the shell game. Under one of three shells will be hidden the key you are looking for. CHose wisely. You have two attempts, and the key will change shells each time, or not... good luck!")
    shells = ['A', 'B', 'C']
    attempts = 2
    for i in range(2):
        random_shell = shells[randint(0, 2)]
        player_choice = str(input("Attempt : Choose a shell (A, B or C):"))
        if player_choice in shells:
            if player_choice == random_shell:
                print("The key has been found under the shell! You have won the game.")
                return True
            else:    
                print("The player was unsuccessful in this attempt.")
        else:
            print("Invalid choice. Please choose A, B or C.")
    print("The player has lost.")
    return False

def dice_game():
    print("You will play the dice game. You and the master will both have three attempts to roll a 6")
    print("You will roll two dice each time. If one of them is a 6, you win. Else, its the master's turn.")
    print("The first one to roll a 6 wins. Good luck!")
    attempts = 3
    dice = [1, 2, 3, 4, 5, 6]
    for i in range(attempts + 1) :
        print("Please roll your dices by entering the enter key.")
        input()
        a,b = dice[randint(0, 5)], dice[randint(0, 5)]
        print("You have rolled " + str(a) + " and " + str(b))
        if a == 6 or b == 6:
            print("You win the game!")
            return True
        else:
            print("You have not rolled a 6. It is now the master's turn. Master, please roll your dice.")
            c,d = dice[randint(0, 5)], dice[randint(0, 5)]
            print("The master has rolled " + str(c) + " and " + str(d))
            if c == 6 or d == 6:
                print("The master wins the game!")
                return False
            else:
                print("The master has not rolled a 6. It is now your turn. Keep in mind you are on attempt " + str(i + 1) + " of " + str(attempts))
    print("The game is a draw. No one wins.")
    return False



def chance_game():
    result = randint(1, 2)
    success = False
    if result == 1:
        success = shell_game()
    if result == 2:
        success = dice_game()
    return success

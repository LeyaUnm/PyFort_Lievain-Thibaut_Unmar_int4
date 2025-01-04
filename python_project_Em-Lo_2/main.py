from math_challenges import *
from pere_fouras_challenge import *
from logic_battleship import *
from chance_challenge import *
from utility_functions import *
from final_challenge import *

    
def game(): #Main program
    introduction()
    team = compose_equipe()
    key = 0
    while key != 3:
        success = False
        print("You currently have " , key , " keys")
        player = choose_player(team)
        print("Player " , player , "will now play")
        choice = challenges_menu()
        
        if choice == 1: #Maths challenges
                print("you will now participate in a math challenge chosen by the master")
                challenge = math_challenge()

        if choice == 2:#logic challenge, battleship
                print("You will now participate in a logic challenge. You will play against the master in a round of battleship.")
                success = battleship_game()
            
        if choice == 3:#chance challenges
            print("You have chosen a chance challenge.")
                success = chance_game()
            
        if choice == 4:#Pere fouras challenges
                print("You have chosen the Pere Fouras riddle. Read carefully and answer the riddle. You have 3 chances. Good luck")
                success = pere_fouras_riddle()

        if success == True :
            key += 1
            print("You have passed this challenge. Good job on gaining a key!")
        if success == False :
            print("You have failed this challenge. Good luck for the next one.")
        
    print("You have 3 keys ! you can officially access the final challenge. You will have to guess a codeword with clues. You will have three tires, each tries adding on a new clue. If you succeed, you will win the game. if not, you will have lost.")
    treasure_room()

answer = True
while answer == True : 
    game()
    word = str(input("You have finished the game, would you like to play again ? write 'yes' if yes, and 'no' if not"))
    while word != "yes" or word != "no":
            word = str(input("Invalid answer. PLease write 'yes' if yes, and 'no' if not"))
    if word == "yes":
        answer = True
    if word == "no":
        answer = False

from math_challenges import *
from pere_fouras_challenge import *
from logic_battleship import *
from chance8challenge import *

# main programme pour les challenges de math
if __name__ == '__main__' :
    riddles = load_riddles('PFRiddles.json')
    print(riddles)
    
def game():
    introduction()
    compose_equipe()
    key = 0
    while key != 3:
        success = False
        print("You currently have " + key + " keys")
        player = choose_player()
        print("Player " + player + "will now play")
        choice = challenge_menu()
        
        if choice == 1: #Maths challenges
            
                print("you will now participate in a math challenge chosen by the master")
                challenge = math_challenge()
                if challenge == math_challenge_factorial:
                    print("The master has chosen the factorial challenge")
                    success = maths_challenge_factorial()
                    
                if challenge == math_challenge_prime:
                    print("The master has chosen the prime challenge")
                    success = maths_challenge_prime()
                    
                if challenge == math_roulette_challenge:        
                    print("The master has chosen the roulette challenge")
                    success = maths_challenge_roulette()
                    
                if challenge == math_challenge_equation:
                    print("The master has chosen the equation challenge")
                    success = maths_challenge_equation()

        if choice == 2:#logic challenge, battleship
                print("You will now participate in a logic challenge. You will play against the master in a round of battleship.")
                success = battleship_game()
            
        if choice == 3:#chance challenges
                pass
            
        if choice == 4:#Pere fouras challenges
                print("You have chosen the Pere Fouras riddle. Read carefully and answer the riddle. You have 3 chances. Good luck")
                success = pere_fouras_riddle()

        if success == True :
            key += 1
            print("You have passed this challenge. Good job on gaining a key!")
        if success== False :
            print("You have failed this challenge. Good luck for the next one.)
        
            

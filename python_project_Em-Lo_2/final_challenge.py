# Fort Boyard Simulation : Lola Lievain-Thibaut ; Emeline Unmar
# Implemention of the final challenge's function

import json
import random

def treasure_room():
    with open("python_project_Em-Lo_2/TRClues.json", 'r') as f:
        data = json.load(f)

    year = random.choice(list(data.keys()))
    show = random.choice(list(data[year].keys()))
    clues = data[year][show]["Clues"]
    code_word = data[year][show]["CODE-WORD"]
    print ("The first three clues are: ", clues[0], clues[1], clues[2])
    print ("You have three attempts to guess the code word.")

    n = 3
    state = False
    for i in range(3):
        guess = input("Enter your guess: ").upper()
        if guess == code_word:
            print("Correct! You win!")
            state = True
            break
        else:
            n -= 1
            if n > 0:
                print("Incorrect. You have", n, "attempts left.")
                print("The next clue is: ", clues[i + 4])
            else:
                print("You have run out of attempts.")
                print("The correct code word was: ", code_word)
                
    if state == True:
        print("You have won the game! Congratulations!")
    else:
        print("You have lost the game. Better luck next time!")

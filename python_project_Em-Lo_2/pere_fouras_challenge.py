import json
import random


def load_riddles(file) :
    with open('PFRiddles.json' , 'r' ) as f :
        data = json.load(f)

    riddles = []
    for i in data :
        riddle = {
            "question" : i["question"],
            "answer" : i["answer"]
        }
        riddles.append(riddle)
        return riddles
    
def pere_fouras_riddle() :
    riddles = load_riddles('PFRiddles.json')
    riddle = random.choice(riddles)
    attempts = 3 

    print(f"Riddle: {riddle['question']}")

    while attempts > 0 :
        answer = input("Answer: ").strip().lower()

        if answer == riddle["answer"].lower() :
            print("Correct!")
            return True
        else :
            attempts -= 1
            if attempts > 0 :
                print(f"Incorrect. You have {attempts} attempts left.")
            else :
                print("You have no more attempts. Game over. The correct answer is: " , riddle["answer"])
                return False

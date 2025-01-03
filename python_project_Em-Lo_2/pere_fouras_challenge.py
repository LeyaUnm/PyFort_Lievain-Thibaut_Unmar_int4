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

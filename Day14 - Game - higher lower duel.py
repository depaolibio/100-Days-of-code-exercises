import random
from game_data import data
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def item(): #pop an item (dictionary term) from the list of data.
    try:
        return data.pop(random.randint(0, len(data) - 1))
    except ValueError:
        return data.pop()

def scoring(num): #compares numbers/scores within a duel, retrieving score and pulling a new item for the next round. 
    global A, B, SCORE, DIC
    a_score = A["follower_count"]
    b_score = B["follower_count"]
    if DIC == 0:
        SCORE+= 1
        print(f"\nDamn! You got the perfect score of {SCORE}! Congratulations")
        exit()
    elif a_score > b_score and num == "A":
        SCORE += 1
        B = item()
        DIC -= 1
    elif a_score < b_score and num == "B":
        SCORE += 1
        A = B
        B = item()
        DIC -= 1
    elif a_score == b_score:
        SCORE += 1
        B = item()
        DIC -= 1
        print("Extra score! It was a draw")
    else:
        print(f"Wrong... game over, your final score is {SCORE}.")
        exit()

print(logo)
print(f"\nWelcome to the higher - lower game!\nHere you have to guess the winner of each single-elimination duel based on their number of followers on Instagram!\nYou cannot make any mistakes, see if you can get a perfect score of {len(data)-1}! Good Luck!\n")

A = item()
B = item()
SCORE = 0
DIC = len(data)

while True: #keeps dueling until User guess the wrong winner!
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    print(vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    scoring(answer)

    print(f"You're right! Current score: {SCORE}")

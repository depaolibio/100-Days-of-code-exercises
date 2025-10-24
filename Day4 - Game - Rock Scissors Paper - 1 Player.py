rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
options = [rock, paper, scissors]

human = input("Type r (rock), p (paper) or s (scissors) to start playing against the computer: ").lower()
if human not in ("r", "p", "s"):
    print ("come on, type either r, p or s...")
    raise SystemExit

computer = random.choice(options)
if human == "r":
    print(f"user {rock}")
elif human == "p":
    print(f" user {paper}")
else:
    print(f" user {scissors}")


print(f"computer {computer}")

if human == "r" and computer == scissors:
    print("You win")
elif human == "p" and computer == rock:
    print ("You win")
elif human == "s" and computer == paper:
    print ("You win")
elif (computer == rock and human == "r") or (computer == paper and human == "p") or (computer == scissors and human == "s"):
    print ("It's a tie")
else:
    print ("You lose")


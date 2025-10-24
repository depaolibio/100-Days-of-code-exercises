print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Welcome to the Hunt, your mission is to find the treasure! \n")
direction_1 = input(
    "You have an uncoordinated map in your hands showing an island, with a putative house, outside of the main land jungle you're lost in. Luckily, you have some artifacts in your backpack to help you survive, and you wittily built a compass by scratching a needle over your magnetic watch and laying it over a dry leaf floating in a quiet puddle. You must avoid going North since the winter season is approaching, and you know you need to reach an island, so what do you do? Go 'South', 'East' or 'West'? ").lower()

if direction_1 == "south":
    print("You decided to head South, found a lake and while drinking some water you were poisoned... Game Over \n")

elif direction_1 == "east":
    print("You decided to head East, you ran into a bear ready for lunch... Game Over \n")

elif direction_1 == "west":
    print(
        "You decided to head West, and soon enough reached the shore. You can see the Island at a distance... what would you like to do, 'swim' or 'wait'? \n")

    direction_2 = input().lower()
    if direction_2 == "swim":
        print("You decided to swim, but the current was too strong and you drowned... Game Over \n")
    elif direction_2 == "wait":
        print(
            "You decided to wait, and eventually found a boat. You sailed to the island and reached the house! You enter the foyer and see 3 doors, which one would you like to try first? \n")
        direction_3 = input("'Blue' 'Yellow' or 'Red'? ").lower()
        if direction_3 == "blue":
            print(
                "You decided to try the Blue door, and you walked into a dark room... you hear a noise coming from the darkness... it scares the shit out of you and the heart attack was inevitable... Game Over \n")

        elif direction_3 == "red":
            print(
                "You decided to try the Red door, and you saw a seductive human being, which deceived you into believing they were your treasure... you missed the real treasure and the final result is death... Game Over \n")

        elif direction_3 == "yellow":
            print(
                "You decided to try the Yellow door, and you walked right into the red carpet leading to the 'Ark of the Covenant', Congratulations, you win! \n")
        else:
            print(
                "You are suicidal (by choosing an option that doesn't exist), so Game Over. Thank you for playing the game!")
    else:
        print(
            "You are suicidal (by choosing an option that doesn't exist), so Game Over. Thank you for playing the game!")
else:
    print("You are suicidal (by choosing an option that doesn't exist), so Game Over. Thank you for playing the game!")

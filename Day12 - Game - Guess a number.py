from random import randint


logo = r"""
                       .-') _  _ .-') _         .-') _    ('-. .-.   ('-.          .-')      ('-.             _  .-')     ('-.   .-') _              .-') _             _   .-')   .-. .-')    ('-.  _  .-')  ,---. 
                      ( OO ) )( (  OO) )       (  OO) )  ( OO )  / _(  OO)        ( OO ).  _(  OO)           ( \( -O )  _(  OO) (  OO) )            ( OO ) )           ( '.( OO )_ \  ( OO ) _(  OO)( \( -O ) |   | 
   ,------.,-.-') ,--./ ,--,'  \     .'_       /     '._ ,--. ,--.(,------.      (_)---\_)(,------.   .-----. ,------. (,------./     '._       ,--./ ,--,' ,--. ,--.   ,--.   ,--.);-----.\(,------.,------. |   | 
('-| _.---'|  |OO)|   \ |  |\  ,`'--..._)      |'--...__)|  | |  | |  .---'      /    _ |  |  .---'  '  .--./ |   /`. ' |  .---'|'--...__)      |   \ |  |\ |  | |  |   |   `.'   | | .-.  | |  .---'|   /`. '|   | 
(OO|(_\    |  |  \|    \|  | ) |  |  \  '      '--.  .--'|   .|  | |  |          \  :` `.  |  |      |  |('-. |  /  | | |  |    '--.  .--'      |    \|  | )|  | | .-') |         | | '-' /_)|  |    |  /  | ||   | 
/  |  '--. |  |(_/|  .     |/  |  |   ' |         |  |   |       |(|  '--.        '..`''.)(|  '--.  /_) |OO  )|  |_.' |(|  '--.    |  |         |  .     |/ |  |_|( OO )|  |'.'|  | | .-. `.(|  '--. |  |_.' ||  .' 
\_)|  .--',|  |_.'|  |\    |   |  |   / :         |  |   |  .-.  | |  .--'       .-._)   \ |  .--'  ||  |`-'| |  .  '.' |  .--'    |  |         |  |\    |  |  | | `-' /|  |   |  | | |  \  ||  .--' |  .  '.'`--'  
  \|  |_)(_|  |   |  | \   |   |  '--'  /         |  |   |  | |  | |  `---.      \       / |  `---.(_'  '--'\ |  |\  \  |  `---.   |  |         |  | \   | ('  '-'(_.-' |  |   |  | | '--'  /|  `---.|  |\  \ .--.  
   `--'    `--'   `--'  `--'   `-------'          `--'   `--' `--' `------'       `-----'  `------'   `-----' `--' '--' `------'   `--'         `--'  `--'   `-----'    `--'   `--' `------' `------'`--' '--''--'  
   """
print(logo)


#Getting started with a prompt.
print("\nWelcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100. Can you guess what it is??!\n(hint: it's an integeeeeer!)")


#Defining the "list" and the level.
SELECTION = randint(1,100)
level = input("Choose your difficulty. Type 'easy' (10 attempts) or Enter for 'hard' (4 attempts): ").lower()
if level == "easy":
    lives = 10
else:
    lives = 4

#Checking the guess function.
def check_num(guess):
    """Check if user's guess is below, equal, or above the SELECTION and returns True or 'key word'. """
    global SELECTION
    if guess == SELECTION:
        return True
    elif guess > SELECTION:
        return "smaller"
    else:
        return "larger"

#Looping through guesses while counting attempts (includes logic for fluke!)
new_guess = ""
while new_guess != SELECTION and lives > 0:
    new_guess = int(input("Type your guess here: "))
    output = check_num(new_guess)
    if output == True:
        if lives > 8:
            print(f"You lucky dog! It is {new_guess}!!!.")
            exit()
        else:
            print(f"You guessed it, it's {new_guess}.")
            exit()
    elif output == "smaller":
        lives -= 1
        print("it's smaller...")
        if lives == 2:
            print("You only have 2 more attempts!")
    elif output == "larger":
        lives -= 1
        print("it's larger...")
        if lives == 2:
            print("You only have 2 more attempts!")

print(f"Game Over, sorry, the number was {SELECTION}.")

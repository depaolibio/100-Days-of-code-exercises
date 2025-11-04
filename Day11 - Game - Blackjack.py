import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

input("Welcome to Blackjack! Press Enter to get started...\n")

your_cards = [random.choice(cards),random.choice(cards)]
print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

pc_cards = [random.choice(cards)]
print(f"Computer's first card: {pc_cards}")

if your_cards == [11, 10] or your_cards == [10, 11]:
    print("\nYour hand is Blackjack! 😎 You win")
    exit()
else:
    my_card_loop = True
    while my_card_loop == True:
        move_on = input("\nType 'y' to get another card, hit Enter to pass: ")
        if move_on == 'y':
            your_cards.append(random.choice(cards))
            if sum(your_cards) == 21:
                print(f"\nYour final hand is {your_cards}, so your score is {sum(your_cards)}")
            elif sum(your_cards) < 21:
                print(f"Your final hand is {your_cards}, so your score is {sum(your_cards)}")
            else:
                print(f"\nYour final hand is {your_cards}, so your score is {sum(your_cards)} and > 21, you loose!😭")
                exit()
        else:
            my_card_loop = False

    pc_cards.append(random.choice(cards))
    pc_card_loop = True
    while pc_card_loop == True:
        if sum(pc_cards) < 17:
            pc_cards.append(random.choice(cards))
            #print(pc_cards)
        elif sum(pc_cards) <21:
            print(f"Computer's cards: {pc_cards}")
            pc_card_loop = False
        elif sum(pc_cards) == 21:
            if pc_cards == [11,10] or pc_cards == [10,11]:
                print(pc_cards)
                print("\nComputer hit Blackjack! You lose!😤")
                exit()
            else:
                print(f"Computer's cards: {pc_cards}")
                pc_card_loop = False
        else:
            print(f"Computer's cards: {pc_cards}")
            print(f"Computer final hand is {sum(pc_cards)} so you win!😁")
            exit()

    if sum(your_cards) > sum (pc_cards):
        print(f"\nYour final hand is {sum(your_cards)}\n"
              f"Computer final hand is {sum(pc_cards)}, so you win!😁")
        exit()
    elif sum(your_cards) < sum(pc_cards):
        print(f"\nYour final hand is {sum(your_cards)}\n"
              f"Computer final hand is {sum(pc_cards)}, so you lose!😭")
        exit()
    else:
        print(f"\nYour final hand is {sum(your_cards)}\n"
              f"Computer final hand is {sum(pc_cards)}, so it's a draw!🙃")
        exit()
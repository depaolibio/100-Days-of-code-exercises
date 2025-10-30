# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Blind Auction Tool, a place for friends and family to 'lead a bid'\n"
      "You'll be asked to input your name, your bid, and if there are more people to go.")
dic_bids = {}
more_bids = True
while more_bids == True:
    user_name = input("What is your name? : ")
    user_bid = int(input("What is your bid in dollars? e.g, 25 : "))

    if user_bid in dic_bids.values():
        print("Sorry, this bid is taken. Re input your name below and try a different value.")
        continue

    continuation = input("Are there others who need to bid? y or n :").lower()
    dic_bids[user_name] = user_bid

    if continuation == "y":
        print("\n" *20)
    elif continuation == "n":
        print("\n" * 20)
        more_bids = False
    else:
        print("Your bid has not been recorded. Insert it again and please type either 'y' or 'n'.")

# Get the key with the maximum value
winner = max(dic_bids, key=dic_bids.get)

# Get the maximum value using the retrieved key
largest_bid = dic_bids[winner]
result = input("Ok, users and bids have been recorded. Press enter when you're ready to see the Winner")
if result == "go":
    print(f"\n ========== The largest bid was ${largest_bid}, give the item to {winner}! ==========")
else:
    print(f"\n ========== The largest bid was ${largest_bid}, give the item to {winner}! ==========")


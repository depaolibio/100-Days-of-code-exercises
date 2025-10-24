
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? e.g., $154.79\n$"))
tax = float(input("What is the tax amount in dollars? e.g., $11.29\n$"))

tip_input = input("What percentage tip would you like to give? e.g., 20%\n")
tip = int(tip_input.strip().replace("%", ""))

people = int(input("How many people to split the bill? e.g., 2"))

amount_per_person = ((bill * (tip/100)) + bill + tax) / people
print (f"Each person should pay: ${round(amount_per_person, 2)}")
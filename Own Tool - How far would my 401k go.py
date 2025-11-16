print("Welcome to the 401k usage calculator!")


years = 0
_401k = int(input("Type your 401k amount in dollars (e.g., 750000): "))
fix_rate = float(input("Type the expected APR applied to the 401k account from the year you start making withdraws (e.g., 0.025 for 2.5%): "))
desired_income = int(input("Type the annual withdraw you plan to be made from your 401k account (e.g., 30000): "))
inflation = 1+ float(input("Type the expected annual inflation if you'd like to account for adjustments needed to the annual withdraw (e.g., 0.04 for 4%): "))

while _401k > desired_income:
    interest = _401k * fix_rate
    desired_income = (desired_income * inflation)
    _401k = (_401k + interest) - desired_income
    print(f"Interest is {int(interest)}. Income ({int(desired_income)}) is {round(desired_income/_401k*100,1)}% of the Leftover 401k ({int(_401k)}).")
    years +=1

print(f"\nUnder such circumstances your 401k will last {years} years.")


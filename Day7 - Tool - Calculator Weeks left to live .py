def life_in_weeks(birth):
    from datetime import datetime
    for given_date_format in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            given_date = datetime.strptime(birth, given_date_format)
            break
        except ValueError:
            given_date = None

    if given_date is None:
        print("Invalid date format. Use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS")
        return

    current_datetime = datetime.now()
    print(f"Current Date and Time: {current_datetime}")

    try:
        ninetieth = given_date.replace(year=given_date.year + 90) #replaces the current year with the birth year, so you have to add 90.
    except ValueError:
        # Happens for Feb 29 when the 90th year isn't a leap year
        if given_date.month == 2 and given_date.day == 29:
            ninetieth = given_date.replace(year=given_date.year + 90, month=2, day=28)
        else:
            # Re-raise if it's some other unexpected date issue
            raise

    time_difference = ninetieth - current_datetime
    seconds_per_week = 60*60*24*7
    weeks_left = int(time_difference.total_seconds() / seconds_per_week) #.total_seconds() is a function inside datetime already!
    print(f"You have {weeks_left} weeks left.")

birth_input = input("What's your date of birth? YYYY-MM-DD (HH:MM:SS optional) \n")
life_in_weeks(birth_input)

def is_prime(num):
    """Checks if a given number is Prime and returns "True" or "False" """
    has_remainder = 0
    no_remainder = 0
    ioi = int((num ** 0.5)+1)
    test = list(range(2,ioi))
    for _ in test:
        if num % _ == 0:
            no_remainder +=1
        else:
            has_remainder +=1

    if no_remainder == 0:
        return True
    elif has_remainder == len(test):
        return True
    else:
        return False

input = int(input("Type a number to check if it is Prime: "))
result = is_prime(input)
print(result)

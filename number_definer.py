number = float(input())

if number == 0:
    print('Zero')
elif number > 0:
    if number < 1:
       print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(number) < 1:
        print("small negative")
    elif abs(number) > 1000000:
        print("lagre negative")
    else:
        print("negative")

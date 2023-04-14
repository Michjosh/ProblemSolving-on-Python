def guess_birthday(month, year):
    correct_date = False
    while not correct_date:
        d = 26
        guess = int(input("Guess the date: "))
        if guess == d:
            print("Correct Guess")
            correct_date = True
        else:
            print("Incorrect Guess")


guess_birthday(6, 1993)

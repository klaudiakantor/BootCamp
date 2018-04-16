import random

numbersCorrect = True
print("Podaj liczby")
try:
    userNumbers = [int(x) for x in input().split()]
    for i in userNumbers:
        if (i < 1) or (i > 49):
            print("Wrong number")
            numbersCorrect = False
            break
    if len(userNumbers) != len(set(userNumbers)):
        print("Numbers must be unique!")
        numbersCorrect = False
except ValueError:
    numbersCorrect = False
    print("Wrong")

if numbersCorrect:
    win = 0
    loose = 0
    for j in range(0, 20000):
        lottoNumbers = []
        for i in range(0, 100000):
            selectedNumber = random.randint(1, 49)
            if selectedNumber not in lottoNumbers:
                lottoNumbers.append(selectedNumber)
            if len(lottoNumbers) == 6:
                break
        success = True

        for number in userNumbers:
            if number not in lottoNumbers:
                success = False
                break
        if success:
            win += 1
        else:
            loose += 1

    print("Win= ", win, "Loose =", loose)

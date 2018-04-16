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
    three=0
    four=0
    five=0
    six=0
    loose=0
    wonMoney=0
    for j in range(0, 20000):
        lottoNumbers = []
        for i in range(0, 100000):
            selectedNumber = random.randint(1, 49)
            if selectedNumber not in lottoNumbers:
                lottoNumbers.append(selectedNumber)
            if len(lottoNumbers) == 6:
                break

        success = True
        win=0
        for number in userNumbers:
            if number in lottoNumbers:
                win += 1

        if win == 3:
            three += 1
            wonMoney += 20
        elif win == 4:
            four += 1
            wonMoney += 200
        elif win == 5:
            five += 1
            wonMoney += 6000
        elif win == 6:
            six += 1
            wonMoney += 2000000
        else:
            loose += 1

    ticketCost = 20000*3
    print ("Results:")
    print("3 numbers: ", three, " Four numbers: ", four, " Five numbers: ", five, " Six numbers: ",
          six, " Number of lost tickets: ", loose, "Total money earned: ", wonMoney, "Total ticket cost: ", ticketCost)

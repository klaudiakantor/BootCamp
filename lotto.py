import random

numbersCorrect = True
print("Enter 6 integer numbers in range 1-49 separated by whitespace: ")
try:
    userNumbers = [int(x) for x in input().split()]
    for i in userNumbers:
        if (i < 1) or (i > 49):
            print("Number out of range!")
            numbersCorrect = False
            break
    if len(userNumbers) != len(set(userNumbers)):
        print("Numbers must be unique!")
        numbersCorrect = False
except ValueError:
    numbersCorrect = False
    print("Numbers must be integer!")

if numbersCorrect:
    print("Enter amount of lotteries: ")
    lotteries = int(input())
    three = 0
    four = 0
    five = 0
    six = 0
    loss = 0
    wonMoney = 0
    for j in range(0, lotteries):
        lottoNumbers = []
        for i in range(0, 1000000):
            selectedNumber = random.randint(1, 49)
            if selectedNumber not in lottoNumbers:
                lottoNumbers.append(selectedNumber)
            if len(lottoNumbers) == 6:
                break

        success = True
        win = 0
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
            loss += 1

    ticketCost = lotteries*3

    print("Results:")
    print("Three numbers: ", three, "\nFour numbers: ", four, "\nFive numbers: ", five, "\nSix numbers: ",
          six, "\nNumber of lost coupons: ", loss, "\nTotal won money: ", wonMoney, "\nTotal coupons' cost: ",
          ticketCost)

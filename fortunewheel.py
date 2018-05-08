import random

def find_letter(s, letter):
    return [j for j, element in enumerate(s) if element == letter]

words = []

with open('wordlist.txt') as f:
    for line in f.readlines():
        word = line.strip()
        words.append(word)

wordIndex = random.randrange(len(words))
chosenWord = words[wordIndex]
wordLength = len(chosenWord)
blanks = list((wordLength * "_"))
print("This is the word:")
print(blanks, "\n")
#print(chosenWord)
print("You have got 1000 PLN. Buy a letter - each letter costs 200 PLN or guess a word - for each guessed letter ",
      "you earn 200 PLN. For wrong word guess you loose all your money")
gameContinue = True
money = 1000
blankLetters = wordLength
userLetters = []

while gameContinue:
    action = input("Do you want to guess the word? Type Y or N: ")
    if action == 'Y':
        userWord = input("Type the word: ")
        if userWord == chosenWord:
            money += blankLetters * 200
            print("You win! You have ", money, " PLN")
        else:
            print("Game over! You have 0 PLN!")
        gameContinue = False
    if action == 'N':
        print("You bought ", userLetters)
        userLetter = input("What letter do you want to buy? ")

        if userLetter in userLetters:
            print("You have already bought this letter!\n")
        else:
            money -= 200
            userLetters.append(userLetter)
            if userLetter in chosenWord:
                letterIndexes = find_letter(chosenWord, userLetter)
                for a in letterIndexes:
                    blanks[a] = userLetter
                blankLetters -= len(letterIndexes)
            else:
                print("This letter is not found in a word!\n")
            print(blanks)
            print ("You have ", money, "PLN\n")
        if '_' not in blanks:
            print("There are no more letters in the word. This is the end of the game. You have: ", money, " PLN")
            gameContinue = False




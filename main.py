import os
import random
import art


def check(st, booled=True):
    if booled:
        checkd = input(st + "\t").lower()
        if checkd == "y":
            return True
        else:
            return False
    else:
        return booled


def compare(user, com):
    
    """ Compare two Arrays and return which array win """
    if total(user) > 17 or total(com) > 17:
        if total(user) <= 21 and total(user) > total(com):
            print("You win")
            return True
        elif total(user) == total(com):
            print("Draw")
        else:
            print("Ai win")
        return True

    elif total(user) > 21 and total(com) > 21:
        print("both Lose  Scores are greater then 21")
        return True
    else:
        False


def card(arr):
    ran1 = []
    for i in range(0, 4):
        rand = random.randint(0, len(arr) - 1)
        ran1.append(arr[rand])
        arr.remove(arr[rand])

    return [[ran1[0], ran1[1]], [ran1[2], ran1[3]]]


def total(arry):
    total = 0
    for i in range(0, len(arry)):
        total += arry[i]
    return total


def printCard(user, computer, showFull_value=False):
    print(f"Your Cards :\t{user}, current score\t{total(user)}")
    if showFull_value:
        print(f"Ai Cards :\t{com}, current score\t{total(com)}")
    else:
        print(f"Ai First card:\t{computer[0]}")


game = "Do you want to play a game of Blackjack? Type 'y' or 'n':"
chosse = "Type 'y' to get another card, type 'n' to pass:"

while check(game):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    os.system("cls")
    print(art.logo)
    user = card(cards)[0]
    com = card(cards)[1]
    print(cards)
    printCard(user, com)

    while check(chosse):
        if compare(user, com):
            printCard(user, com, True)
            break

        elif len(cards) > 1:  # user card

            ranGen1 = cards[random.randint(0, len(cards) - 1)]
            user.append(ranGen1)
            cards.remove(ranGen1)
            # computer card
            comGen = cards[random.randint(0, len(cards) - 1)]
            com.append(comGen)
            cards.remove(comGen)
            printCard(user, com)
        else:
            print("Card Desk is empty")
            printCard(user, com, True)
            compare(user, com)
            break
    else:
        printCard(user, com, True)
        compare(user, com)

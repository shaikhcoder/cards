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
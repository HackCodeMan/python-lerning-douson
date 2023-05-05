from classCARD import Card, Hand, Deck
def main():
    """Main program"""
    deck1: Deck = Deck()
    print("Появилась колода: ",deck1, sep = "\n")
    deck1.populate()
    print("В колоде появились карты:",deck1, sep = "\n")
    deck1.shuffle()
    print("Карты размешаны:", deck1, sep = "\n")
    my_hand: Hand = Hand()
    your_hand: Hand = Hand()
    hands: list[Hand] = [my_hand, your_hand]
    deck1.deal(hands = hands, per_hand = 6)
    print("Мне и вам на руки из колоды были разданы 6 карт")
    print("У меня на руках:",my_hand)
    print("У него на руках:", your_hand)
    print("Осталось в колоде:", deck1, sep = "\n")
    deck1.clear()
    print("Осталось в колоде после удаления:", deck1, sep="\n")

main()
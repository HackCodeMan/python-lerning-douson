import typing
import random
class Card(object):
    """Карта"""
    RANKS: tuple[str] = ("A","2","3","4","5","6","7","8","9","10","J","Q","K") #Значения карт
    SUITS: tuple[str] = ("c","d","h","s") #Масти
    def __init__(self, rank, suit):
        self.rank: str = rank
        self.suit: str = suit
    def __str__(self) -> str:
        rep: str = self.rank + self.suit
        return rep
class Unprintable_Card(Card):
    """Карта, номинал и масть которого не могут быть выведены на экран"""
    # Переопределение волшебной функции изменяет у себя функционал наследуемого класса
    def __str__(self) -> str:
        return "<Нельзя распечатать>"
class Positionable_Card(Card):
    """Карта, которую можно положит лицом вверх или вниз"""
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank,suit)
        # Можно вызвать на прямую Card.__init__(rank, suit) и всё будет работать,
        # но так делать не рекомендуется, тк иерархия может меняться
        self.face_up = face_up
    def __str__(self):
        if self.face_up:
            rep = super(Positionable_Card,self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        """Переворот карты"""
        self.face_up = not self.face_up
class Hand(object):
    """Рука игрока и карты, которыми владеет игрок"""
    def __init__(self):
        self.cards: list = []
    def __str__(self) -> str:
        if self.cards: #list == True if len(list) > 0 else list == False
            rep = ""
            rounds: int = 0
            for card in self.cards:
                rep += str(card) + " "
                rounds += 1
                if rounds == 8:
                    rep += "\n"
                    rounds: int = 0
        else:
            rep = "<Пусто>"
        return rep
    def clear(self):
        """Удаляет все карты на руке"""
        self.cards.clear()
    def add(self, card):
        """Добавляет карту на руку"""
        self.cards.append(card)
    def give(self, card, other_hand):
        """Передаёт карту из одной руки в другую (между игроками)"""
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    """Виртуальная Колода игральных карт"""
    def populate(self):
        """Создаёт колоду карт"""
        self.cards: typing.Any = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank = rank, suit = suit))
    def shuffle(self):
        """Размешивает колоду карт"""
        random.shuffle(self.cards)
    def deal(self, hands: list[Hand] , per_hand: int):
        """Передаёт карты на руку"""
        for i in range(per_hand):
            for hand in hands:
                if self.cards:
                    self.give(self.cards[0],hand)
                else:
                    print("Не могу сдавать. Карты в колоде закончены.")
if __name__ == "__main__":
    deck1: Deck = Deck()
    deck1.populate()
    deck1.shuffle()
    print(deck1.__dict__) # Показывает список атрибутов
    a = deck1.__str__() # Значение возвращенное от функции __str__() записывается в переменную
    print(f"Значение от __str__() {a} \n") #f-строка
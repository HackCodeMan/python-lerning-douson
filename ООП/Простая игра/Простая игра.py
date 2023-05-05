from easy_game_module import *
from random import randrange
def main():
    """Main program"""
    again = "Y"
    while again != "N":
        input_helper1: Input_Helper = Input_Helper()
        print("Добро пожаловать в самую простую игру")
        number = input_helper1.ask_number\
            (question = "Сколько игроков участвует?", low = 2, high = 5)
        players: list[Player] = []
        def input_players(amount_players: int):
            for i in range (amount_players):
                player_name: str = input("Введите имя " + str(i+1) + " игрока: ")
                player_score: int = randrange(100)
                players.append(Player(name = player_name, score = player_score))
        input_players(number)
        print("Результаты игры: ")
        for obj in players:
            print(obj)
        again = Input_Helper.ask_yes_or_no("Хотите сыграть ещё раз?")

main()

class Player(object):
    def __init__(self, name, score):
        self.name: str = name
        self.score: str = score
    def __str__(self) -> str:
        return self.name + ":\t" + str(self.score)
    def __len__(self):
        return self.score
class Input_Helper(object):
    """Помощник, собирающий информацию у пользователя"""
    @staticmethod
    def ask_yes_or_no(question: str) -> str:
        """Задаёт вопрос с ответом 'да' или 'нет'"""
        answer: None = None
        while answer not in ("Y","N"):
            print(question + " (Y/N)")
            answer: str = input("Ваш выбор: ").upper()
        return answer
    @staticmethod
    def ask_number(question: str,low: int,high: int) -> int:
        """Просит у пользователя число в каком либо диапазоне"""
        number: None = None
        while number not in range(low,high):
            print(question)
            print("Введите число в диапазоне от", low,"до",high)
            number: int = int(input("Введите число: "))
        return number
if __name__ == "__main__":
    print("Это модуль! Он запускается не на прямую, а импортируется в ваш проект")
    print("Импортируй меня в свой проект, а затем пользуйся мной!"
          "\nДля этого в любую строку введи:  from easy_game import *")
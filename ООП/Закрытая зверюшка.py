# Покажет работу закрытых методов и переменных
class Critter:
    def __init__(self, name, age, mood):
        print("На свет появилась новая зверюшка")
        self.name = name
        self.age = age
        self.__mood = mood #Создание приватного аргумента объекта
        #__mood - закрытый, значит защищен от клиентского ввода, при попытке пользовательского
        #ввода, будет возникать ошибка AttributeError
    def who_i(self):
        print("Меня зовут", self.name)
        print("Мне", self.age,"годиков")
        print("у меня настроение", self.__mood)
    # Создание приватного метода его можно использовать в других открытых методах класса
    def __private_method(self):
        print("Я закрытый метод\n Создан с помощью '__'")
    def public_method(self):
        print("Я открытый метод")
        # Использование закрытого метода в другом открытом методе
        self.__private_method()
obj1 = Critter("Гриша", 3, "прекрасное")
try:
    print("вне класса не смогу сказать что настроение у меня",  obj1.mood)
except AttributeError:
    print("Моё настроение вне класса можно узнать насильно", obj1._Critter__mood)
    #Так лучше не делать!!!
obj1.who_i()
obj1.public_method()

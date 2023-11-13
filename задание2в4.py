'''Создать классы Книга (поля – автор, название, год выпуска) и Журнал (поля – название, номер, год выпуска). Создать полиморфные методы для вывода полной информации об экземпляре класса.
'''
class Item:#новый класс элеммент
    def __init__(self, title, year):#конструктор с параметрами title, year
        self.title = title
        self.year = year#инициализируем параметрвы

    def display_info(self):#функция вывода информации
        pass#выполняем ничего

class Book(Item):#новый класс книга
    def __init__(self, author, title, year):#конструктор с параметрами author, title, year
        super().__init__(title, year)
        self.author = author#инициализируем параметрвы

    def display_info(self):#функция вывода информации
        print(f"книга: {self.title} написана {self.author}, опубликована в {self.year}")#то что выводит

class Magazine(Item):#новый класс журнал
    def __init__(self, title, number, year):#конструктор с параметрами title, number, year
        super().__init__(title, year)
        self.number = number#инициализируем параметрвы

    def display_info(self):#функция вывода информации
        print(f"журнал: {self.title}, номер {self.number}, опубликован в {self.year}")#то что выводит

book1 = Book("Пушкиным", "пир во время чумы", 1832)
magazine1 = Magazine("Voice : будущее - это мы", 15, 2021)#создание экземпляров классов

book1.display_info()
magazine1.display_info()#вызов полиморфных методов
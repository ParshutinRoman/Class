meat = 0

class Animals():
    """Class to create an animal"""
    def __init__(self, name, weight, ration, voice):
        """initiate new animal"""
        self.name = name
        self.weight = weight
        self.ration = ration
        self.voice = voice


    def show_animal(self):
        """Prints all info about this animal"""
        info = ("Name is: " + self.name + " weight is: " + str(self.weight) + " ration is " + str(self.ration) +
                " of forage")
        print(info)

    def feed_animal(self, forage=1000):
        """Spend some forage"""
        forage -= self.ration
        self.weight += self.ration / 20

    def says (self):
        print(self.name + "says" + self.voice + "twice")

    def kill_animal(self, meat):
        meat += self.weight * 0.45


class Birds(Animals):
    """Class to create a bird"""
    def __init__(self, name, weight, ration, voice, egg):
        """initiate new bird"""
        super().__init__(name, weight, ration, voice)
        self.egg = egg


class HornedCattle(Animals):
    """Class to create a bird"""
    def __init__(self, name, weight, ration, voice, milk):
        """initiate new bird"""
        super().__init__(name, weight, ration, voice)
        self.milk = milk

class Cattle(Animals):
    """Class to create a bird"""
    def __init__(self, name, weight, ration, voice, wool):
        """initiate new bird"""
        super().__init__(name, weight, ration, voice)
        self.wool = wool




sheep1 = Cattle("Барашек", 87, 8, "бееее", 2.5)
sheep2 = Cattle("Кудрявый", 95, 11, "бееее", 3)
goose1 = Birds("Серый", 4.5, 1, "Гага", 1)
goose2 = Birds("Белый", 3, 0.7, "Гага", 1)
cow = HornedCattle("Манька", 170, 15, "Муууу", 5)
goat1 = HornedCattle("Рога", 60, 11, "Мееее", 3)
goat2 = HornedCattle("Копыта", 65, 9, "Меее", 3.5)
chicken1 = Birds("Ко-Ко", 3, 0.5, "КоКО", 5)
chicken2 = Birds("Кукареку", 2.5, 0.5, "КоКО", 4)
duck = Birds("Кряква", 3.4, 0.5, "КряКря", 1)

animals = (sheep1, sheep2, goat2, goat1, goose1, goose2, cow, chicken1, chicken2, duck)

def heaviest_animal():
    max_weight = 0
    champion_name = "..."
    for animal in animals:
        if animal.weight > max_weight:
            max_weight = animal.weight
            champion_name = animal.name
    print("Самое тяжелое животное - " + champion_name + ", который весит " + str(max_weight))

def total_weight():
    total_weight = 0
    for animal in animals:
        total_weight += animal.weight
    print("Общий вес обитателей фермы - " + str(total_weight))

goat2.show_animal()
goat2.feed_animal()
goat2.show_animal()
print(sheep1.weight)
print(animals)
heaviest_animal()
total_weight()





# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
#
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
#
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

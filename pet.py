from abc import ABCMeta, abstractmethod, abstractproperty

class Animal():
    __metaclass__ = ABCMeta

    @abstractproperty
    def collect():
        pass

class Pet():
    name = 'no name'
    weight = 0
    feed = 0
    voice = 'nothing'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed_animal(self):
        self.feed += 1
        print("Ваше животное по кличке " + self.name + " " + "покормленно")
        return self.feed

    def voice_animal(self):
        print(self.voice)


class Bird(Pet, Animal):
    eggs = 0
    def collect(self):
        self.eggs += 2
        print('Всего собрано яиц  ' + str(self.eggs))
        return self.eggs

class Horned_cattle(Pet):
    milk = 0

    def collect(self):
        self.milk += 1
        print("Животное подоенно")
        return self.milk
        
class Sheep(Pet):
    haircat = 0

    def collect(self):
        self.haircat += 1
        print('Животное подстриженно')
        return self.haircat

class Goose(Bird):
    voice = "га-га-га"


list_animal = []

goose_1 = Goose('Серый', 8)
list_animal.append(goose_1)
goose_2 = Goose('Белый', 7)
list_animal.append(goose_2)
cow = Horned_cattle('Манька', 300)
list_animal.append(cow)
cow.voice = 'Мууу'
sheep_1 = Sheep('Барашек', 35)
list_animal.append(sheep_1)
sheep_2 = Sheep('Кудрявый', 40)
list_animal.append(sheep_2)
chicken_1 = Bird('Ко-Ко', 4)
list_animal.append(chicken_1)
chicken_2 = Bird('Кукареку', 5)
list_animal.append(chicken_2)
goat_1 = Horned_cattle('Рога', 41)
list_animal.append(goat_1)
goat_2 = Horned_cattle('Копыта', 43)
list_animal.append(goat_2)
duck = Bird('Кряква', 5)
list_animal.append(duck)
duck.voice = 'Кря-кря'


dict_animal_weight = {}

def weight_animal(name):
    dict_animal_weight[name.name] = name.weight
    return

for animal in list_animal:
    weight_animal(animal)
    print(animal.feed_animal(), animal.collect())


dict_animal_weight.values()
print('Вес всех животных - ' + str(sum(dict_animal_weight.values())) + 'кг')

heaviest = max(dict_animal_weight.values())

for name in dict_animal_weight:
    if heaviest == dict_animal_weight[name]:
        print('Самое тяжелое животное -',name)


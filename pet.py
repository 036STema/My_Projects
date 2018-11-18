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
        print("Ваше животное по кличке " + self.name + " " + "покормленно раз(а)" + str(self.feed))

    def voice_animal(self):
        print(self.voice)


class Bird(Pet):
    eggs = 0

    def collect_eggs(self, egg):
        self.eggs += 1 * egg
        print('Всего собрано яиц  ' + str(self.eggs))

class Horned_cattle(Pet):
    milk = 0

    def milk_animal(self):
        self.milk += 1
        print("Животное подоенно")

class Sheep(Pet):
    haircat = 0

    def haircat_animal(self):
        self.haircat += 1
        print('Животное подстриженно')

class Gooses(Bird):
    voice = "га-га-га"

    def collect_eggs(self, egg):
        super().collect_eggs(egg*2)


goose_1 = Gooses('Серый', 8)
goose_2 = Gooses('Белый', 7)
cow = Horned_cattle('Манька', 300)
cow.voice = 'Мууу'
sheep_1 = Sheep('Барашек', 35)
sheep_2 = Sheep('Кудрявый', 40)
chicken_1 = Bird('Ко-Ко', 4)
chicken_2 = Bird('Кукареку', 5)
goat_1 = Horned_cattle('Рога', 41)
goat_2 = Horned_cattle('Копыта', 43)
duck = Bird('Кряква', 5)
duck.voice = 'Кря-кря'


goose_1.feed_animal()
goose_1.voice_animal()
goose_1.collect_eggs(7)


goose_2 = Gooses('Белый', 6)
print(goose_2.name)

dict_animal_weight = {}

def weight_animal(name):
    dict_animal_weight[name.name] = name.weight
    return

weight_animal(goose_1)
weight_animal(goose_2)
weight_animal(cow)
weight_animal(sheep_1)
weight_animal(sheep_2)
weight_animal(chicken_1)
weight_animal(chicken_2)
weight_animal(goat_1)
weight_animal(goat_2)
weight_animal(goat_1)
weight_animal(duck)


total_weight = []
for x in dict_animal_weight:
    total_weight.append(dict_animal_weight[x])
print('Вес всех животных - ' + str(sum(total_weight)) + 'кг')

heaviest = max(total_weight)

for name in dict_animal_weight:
    if heaviest == dict_animal_weight[name]:
        print('Самое тяжелое животное -',name)

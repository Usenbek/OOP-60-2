class animal:
    def __init__(self,name: str,age: int ,health: int):
        self.name = name
        self.age = age
        self.health = health
    def info(self):
        return f"имя: {self.name}, возраст: {self.age}, здоровье: {self.health}"
    def use_ability(self):
        return f"{self.name} использует базовую способность"

class flyable():
    def use_ability(self):
        return super().use_ability() + " умеет летать"


class swimable():
    def use_ability(self):
        return super().use_ability() + " умеет плавать."


class invisible():
    def use_ability(self):
        return super().use_ability() + " умеет становится невидимым."
class Duck(flyable,swimable,animal):
    # def use_ability(self):
    ...
class Bat(flyable,animal):
    ...
class Frog(swimable,animal):
    ...
class Pheonix(flyable,invisible,animal):
    ...
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self,animal):
        self.animals.append(animal)
    def show_animals(self):
        for animal in self.animals:
            print(animal.info())
    def perform_abilities(self):
        for animal in self.animals:
            print(animal.use_ability())
obj = Duck("Утка",4,10)
obj2 = Bat("Мышь", 2, 5)
obj3 = Frog("Жаба",7, 8)
obj4 = Pheonix("Феникс", 1000, 100)
zoo = Zoo()
zoo.add_animal(obj)
zoo.add_animal(obj2)
zoo.add_animal(obj3)
zoo.add_animal(obj4)
zoo.show_animals()
zoo.perform_abilities()


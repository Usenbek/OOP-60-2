# class Cat:
#     ...
# cat = Cat()
# cat.name = "Murka"
# cat.age = 3
# print(cat)

class animal:

    def __init__(self,name,species,age,health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
    def feed(self):
        self.health += 10
    def play(self):
        self.health -= 5

class Zooshop():
    def __init__(self):
        self.animals = []
    def add_animal(self,animal):
        self.animals.append(animal)
    def show_animal(self):
        for animal in self.animals:
            print(animal.name,animal.species,animal.health)
    def sell_animal(self,name):
        self.animals.remove(name)

obj = animal("utka","bird",5,80)
obj2 = animal("cat","kitten",3,55)
obj3 = animal("dog","dogs",15,95)
obj4 = animal("frog","poisons",1,35)
zoo = Zooshop()
zoo.add_animal(obj)
zoo.add_animal(obj2)
zoo.add_animal(obj3)
zoo.add_animal(obj4)
zoo.show_animal()
print("\nafter 30 minutes\n")
obj.feed()
obj2.play()
zoo.sell_animal(obj4)
zoo.show_animal()



#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         ...
#     @abstractmethod
#     def move(self):
#         ...
#
# class Dog(Animal):
#
#     def make_sound(self):
#         return "Гав Гав"
#     def move(self):
#         return "Шаг"
# gufi = Dog()
# # print(gufi.make_sound())
#
# class SmsSend(ABC):
#     # @abstractmethod
#     # def send_sms(self):
#
#
# class KgsSms(SmsSend):
#
#     def send_otp(self):
#
#         text = "<text>1234</text>"
#         phone = "<phone>+996779</phone>"
#         # self.send(text, phone)
#
# class RUSms(SmsSend):
#
#     # def send_sms(self):
#
#     def send_otp(self):
#         data = {
#             "text": "1234",
#             "phone": "+7925"
#         }
#         # self.send_sms(data)
#
# inputr = input()
# listi = [float(x) for x in inputr.split()]
# target = int(input())
# filtred = sorted(listi, key= lambda x: abs(x - target))
# tuples = (target,filtred)
# print(tuples)

while True:
    word = input()
    if word == "exit":
        break

    count1 = 0
    count2 = 0
    count3 = 0
    # count4 = 0
    for i in word:
        if i.isalpha():
            count1 += 1
            if i.isupper():
                count3+= 1
            elif i.islower():
                count2 += 1
        if count1 == 0:
            print("NO")
            continue
    low_percent = (count2 / count1) * 100
    high_percent = (count3 / count1) * 100
    print("letters:", count1)
    print("low letters:", count2)
    print("high letters:", count3)
    print(f'{low_percent:.2f}% / {high_percent:.2f}%')
    # print(l)
#Инкапсуляция
class BankAccount:
    def  __init__(self, name, balance, password):
        self.name = name #открытая атрибута
        self._balance = balance #защищенный атрибут
        self.__password = password #приватный атрибут

john = BankAccount("John",100,"123qwerty")
print(john._balance)






































from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...
    @abstractmethod
    def move(self):
        ...

class Dog(Animal):

    def make_sound(self):
        return "Гав Гав"
    def move(self):
        return "Шаг"
gufi = Dog()
# print(gufi.make_sound())

class SmsSend(ABC):
    # @abstractmethod
    # def send_sms(self):


class KgsSms(SmsSend):

    def send_otp(self):

        text = "<text>1234</text>"
        phone = "<phone>+996779</phone>"
        # self.send(text, phone)

class RUSms(SmsSend):

    # def send_sms(self):

    def send_otp(self):
        data = {
            "text": "1234",
            "phone": "+7925"
        }
        # self.send_sms(data)
#Инкапсуляция
import random
import string
class BankAccount:
    def  __init__(self, name, balance, password):
        self.name = name #открытая атрибута
        self._balance = balance #защищенный атрибут
        self.__password = password #приватный атрибут
    def login(self,password):
        if self.__password == password:
            print("вы вошли!")
        else:
            print("вы не вошли!")
    def view_balance(self,password):
        if self.__password == password:
            return self._balance
        else:
            return "неверно"
    def __random_password(self):
        chart =  string.digits
        password = ''.join(random.choice(chart) for _ in range(5))
        return password
    def get_new_password(self):
        return self.__random_password()

john = BankAccount("John",100,"123qwerty")
# print(john._balance)
print(john.get_new_password())

#
# john.login("123qwerty")
# print(john.view_balance(input()))








#
#
#
# from abc import ABC, abstractmethod
# #Абстрактный класс
#
# class animal(ABC):
#         # @abstractmethod
#         def make_sound(self):
#             ...
#         @abstractmethod
#         def move(self):
#             ...
# class Dog(animal):
#     def make_sound(self):
#         return "Gaf Gaf"
#
#     def move(self):
#         return "step"
#
# # gufi = Dog()
# # print(gufi.make_sound())
#
# class SmsSend(ABC):
#
#     @abstractmethod
#     def send_otp(self):
#         pass
# class KgSms(SmsSend):
#     def send_otp(self):
#
#         text = "<text>t1234</text>"
#         phone = "<phone>+996779</phone>"
#
#         self.send(text, phone)
# class RUSms(SmsSend):
#     def send_otp(self):
#         data = {
#             "text": "1234",
#             "phone": "+7925"
#         }
#         # self.send_sms(data;)
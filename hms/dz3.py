import random
import string

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

    def deposit(self, amount, password):
        if self.__password == password:
            self._balance += amount
            return self._balance
        else:
            return "неверный пароль"
    def withdraw(self,amount, password):
        if self.__password != password:
            return "wrong password"
        if amount > self._balance:
            return "нехватает средств"
        if self.__password == password:
            self._balance -= amount
            return self._balance
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return "пароль изменен"
        else:
            return "пароль неверен"
    def get_balance(self, password):
        if self.__password == password:
            return self._balance
        else:
            return "wrong password"

    def __generate_pin(self):
        chart = string.digits
        password = ''.join(random.choice(chart) for _ in range(4))
        return password

    def reset_pin(self,password):
        if self.__password == password:
             self.__password = self.__generate_pin()
             return self.__password
        else:
             return "пароль неверен"

john = BankAccount("John",100,"123qwerty")

print(john.deposit(50, "123qwerty"))        # 150
print(john.withdraw(200, "123qwerty"))      # "Недостаточно средств!"
print(john.get_balance("123qwerty"))        # 150
print(john.change_password("wrong", "new")) # "Старый пароль неверный"
print(f"{john.reset_pin('123qwerty')}")          # например "7291"


from abc import ABC, abstractmethod
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailSender(NotificationSender):
    def send(self, message, recipient):
        self._service = "Gmail"
        return f"Email sent to {recipient}"
    def get_service(self):
        return self._service
class SmsSender(NotificationSender):
    def send(self, message, recipient):
        self._service = "Twilio"
        return f"SMS sent to {recipient}"
    def get_service(self):
        return self._service
class PushSender(NotificationSender):
    def send(self, message, recipient):
        self._service = "Firebase"
        return f"Push sent to {recipient}"
    def get_service(self):
        return self._service
email = EmailSender()
sms = SmsSender()
print(email.send("hello", "john@gmail.com"))
print(sms.send("hello","john"))
print(sms.get_service())

class UserAuth:
    def __init__(self, username, account:BankAccount, notifier:NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier
    def login(self,password):
         res = self.account.get_balance(password)
         if isinstance(res,int):
              print(self.notifier.send(f"успешный вход {self.username}", "любой_номер_или_почта"))
              return True
         else:
              return False
    def transfer(self,amount,password,recipient_account:BankAccount):
         res = self.account.get_balance(password)
         if isinstance(res, int):
             withdraw_result = self.account.withdraw(amount,password)
             if isinstance(withdraw_result,int):
                 recipient_account._balance += amount
                 print(self.notifier.send(f"Перевод {amount} отправлен", f"{self.username}"))
                 print(self.notifier.send(f"Получено {amount} от {self.username}", "контакт_получателя"))
         else:
             return "Wrong!"

john = BankAccount("John", 200, "secret")
alice = BankAccount("Alice", 50, "pass123")
notifier = SmsSender()
user = UserAuth("john_doe", john, notifier)

print(user.login("secret"))

user.transfer(70, "secret", alice)
print("John balance:", john._balance)
print("Alice balance:", alice._balance)
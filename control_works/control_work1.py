class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"
class WarriorHero(MageHero):
      ...
      def action(self):
          return f"{self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount():
    Bank_name = "Simba"
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password
    def login(self, password):
        if self.__password == password:
            return f"Вход успешен"
        else:
            return "Неверный пароль"

    @property
    def full_info(self):
        return self.hero

    @classmethod
    def get_name_bank(cls):
        return f"Банк: {cls.Bank_name}"

    @staticmethod
    def bonus_for_lvl(lvl):
        return f"Бонус за {lvl}: 300 Сом"

    def __str__(self):
        return f"Имя: {self.hero} | Баланс: {self._balance}"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return f"{self._balance} + {other._balance}"
        else:
            return "Герои не одного типа!"
    def __eq__(self, other):
        if type(self.hero) == type(other.hero):
            return True
        else:
            return False

from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
class KGSms(SmsService):
    def send_otp(self, phone):
        code = "<text>1234</text>"
        phone = "<phone>+996777123456</phone>"
class RUSms(SmsService):
    def send_otp(self, phone):
        phone = {
            "code": "1234",
            "phone": "+79915089945"
        }

obj = MageHero("merlin", 10, 100, 50)
obj2 = WarriorHero("kana",50,300,70)
print(obj.action())
print(obj2.action())
obj3 = BankAccount("Merlin",300,"123pass")
print(obj3.login("123pass"))
print(str(obj3))
print(BankAccount.get_name_bank())
print(BankAccount.bonus_for_lvl(50))

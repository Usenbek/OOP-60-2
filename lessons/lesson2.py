# Наследование

# родительский/супер класс
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
    def action(self):
        return self.name
        # return self.hp * self.lvl



class A:
    def act(self):
        return 'A'
class B(A):
    def act(self):
        return "B"
class C(A):
    def act(self):
        print(super().act())
        return 'C'
class D(C,B):
    pass
    # def act(self):
        # return 'D'
obj = D()
print(obj.act())

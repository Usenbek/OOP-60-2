class student:
    def __init__(self,name,age,speed):
        self.name=name
        self.age=age
        self.speed=speed
    def action(self):
        return f'Имя: {self.name}, Возраст:{self.age}, Скорость:{self.speed}'
    def action2(self):
        if self.speed >= 30:
            return self.speed + 30
        else:
            return self.speed + 20

noname1 = student("oleg", 20, 30)
noname2 = student("artem",18,28)
print(noname1.action())
print(noname1.action2())
print(noname2.action())
print(noname2.action2())
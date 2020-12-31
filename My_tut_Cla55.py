class Sbb:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def into_self(self):
        return f'My name is {self.name}'

    def into_colo(self):
        return f'My favourite color is {self.color}'

    def into_weigh(self):
        return f'My weight is {self.weight}'


r1 = Sbb('Suhas', 'Orange', 71)
r2 = Sbb('Saom', 'Yellow', 98)

# r1 = Sbb()
# r1.name = 'suhas'
# r1.color = 'Purple'
# r1.weight = 71
#
# r2 = Sbb()
# r2.name = 'sp'
# r2.color = 'yellow'
# r2.weight = 91

print(r1.into_self())
print(r1.into_colo())
print(r1.into_weigh())

print(r2.into_self())
print(r2.into_colo())
print(r2.into_weigh())



import calendar
class company:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    @classmethod
    def get_mony(cls, salary, bonus):
        company.mysalaries = salary
        company.bonuses = bonus
emp1 = company('SUhas', 'Bhoir')
company.get_mony(10000, 5000)

print(company.mysalaries, company.bonuses)
print(emp1.mysalaries)

print(calendar.firstweekday())
j = calendar.setfirstweekday(calendar.SUNDAY)
print(j)

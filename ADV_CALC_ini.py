import math
from termcolor import colored

class calculator:

    def __init__(self, a, b, c, d, h, n, o, p, v, x, y ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
        self.o = o
        self.p = p
        self.v = v
        self.n = n
        self.x = x
        self.y = y

    def addation(self):
        z = self.x + self.y
        return z

    def subtraction(self):
        z = self.x - self.y
        return z

    def division(self):
        z = self.x // self.y
        return z

    def modulo(self):
        z = self.x % self.y
        return z

    def multipication(self):
        z = self.x * self.y
        return z

    def squart(self):
        z = math.sqrt(self.x)
        return z

    def powerofn(self):
         z = math.pow(self.x, self.n)
         return z

    def sin(self):
        sin0 = self.o/self.h
        return sin0

    def cos(self):
        cos0 = self.a/self.h
        return cos0

    def tan(self):
        tan0 = self.o/self.a
        return tan0

    def are(self):
        area = math.pi * math.pow(self.x, 2)
        return area

    def radid(self):
        r1 = self.d/2
        return r1

    def radic(self):
        r1 = self.c / 2 * math.pi
        return r1

    def salper(self):
        pers = (self.p * self.v) / 100
        return pers

    def quatradic_r(self):
        dec = (self.b**2) - (4*self.a*self.c)
        if dec > 0:
            num_root = 2
            root1 = (((-self.b) + math.sqrt(dec))/(2*self.a))
            root2 = (((-self.b) - math.sqrt(dec))/(2*self.a))
            return 'Two distinct real root exist: root1 = %.2f and root2 = %.2f' % (root1, root2)
        elif dec == 0:
            num_root = 1
            root12 = (-self.b) / (2*self.a)
            return 'There is a one ', root12
        elif(dec < 0):
            num_root = 0
            return 'No roots, discriminant < 0.'

    def pythagores_c(self):
        c = math.sqrt((self.a*self.a) + (self.b*self.b))
        return c

    def pythagores_b(self):
        b = math.sqrt((self.c*self.c) - (self.a*self.a))
        return b

    def pythagores_a(self):
        a = math.sqrt((self.c*self.c) - (self.b*self.b))
        return a

    def fibonacci_itrate(self):
        p_num = 0
        c_num = 1
        for i in range(1, self.n):
            p_p_num = p_num
            p_num = c_num
            c_num = p_p_num + p_num
        return c_num

    if __name__ == '__main__':
        print("Initializing...Program...Advanced Calculator...",  __name__)


calc = calculator('a', 'b', 'c', 'd', 'h', 'n', 'o', 'p', 'v', 'x', 'y')


while True:
    print('*' * 40)
    print('Please select your "Operator" choice')
    print('*' * 40)

    print("please enter", colored('1', 'blue'), "for \"Addition\"", colored('[+]', 'red'))
    print("please enter", colored('2', 'blue'), "for \"subtraction\"", colored('[-]', 'red'))
    print("please enter", colored('3', 'blue'), "for \"division\"", colored('[/]', 'red'))
    print("please enter", colored('4', 'blue'), "for \"modulo\"", colored('[%]', 'red'))
    print("please enter", colored('5', 'blue'), "for \"multiply\"", colored('[x]', 'red'))
    print("please enter", colored('6', 'blue'), "for \"square_Root\"", colored('[√]', 'red'))
    print("please enter", colored('7', 'blue'), "for \"power_of\"", colored('[x^]', 'red'))
    print("please enter", colored('8', 'blue'), "for \"Calculate sin for triangle\"", colored('[sineθ]', 'red'))
    print("please enter", colored('9', 'blue'), "for \"Calculate cos for triangle\"", colored('[cosθ]', 'red'))
    print("please enter", colored('10', 'blue'), "for \"Calculate tan for triangle\"", colored('[tanθ]', 'red'))
    print("please enter", colored('11', 'blue'), "to\" calculate Area of circle\"", colored('[πr^2][AREA]', 'red'))
    print("please enter", colored('12', 'blue'), "to\" calculate Radius of circle\"", colored('[RADIUS]', 'red'))
    print("please enter", colored('13', 'blue'), "to\" calculate percentage\"", colored('[%]', 'red'))
    print("please enter", colored('14', 'blue'), "to\" calculate Table\"", colored('[Table]', 'red'))
    print("please enter", colored('15', 'blue'), "to\" calculate roots of a Quadratic Equation\"", colored('[roots of a Quadratic]', 'red'))
    print("please enter", colored('16', 'blue'), "to\" to calculate one side of a right-angled triangle using Pythagorean Theorem\"", colored('[Pythagoras]', 'red'))
    print("please enter", colored('17', 'blue'), "to\" to find the Fibonacci sequence\"", colored('[Fibonacci]', 'red'))
    try:
        uinp = int(input('\nplease enter number: '))
        if uinp == 1:
            calc.x = int(input('\nPlease enter first number:'))
            calc.y = int(input('\nPlease enter second number:'))
            add = calc.addation()
            print(f'\nTotal of \"{calc.x}\" and \"{calc.y}\" is =', colored(add, 'yellow'))
        elif uinp == 2:
            calc.x = int(input('\nPlease enter first number:'))
            calc.y = int(input('\nPlease enter second number:'))
            sub = calc.subtraction()
            print(f'\nSubtraction of \"{calc.y}\" from \"{calc.x}\" is =', colored(sub, 'yellow'))
        elif uinp == 3:
            calc.x = int(input('\nPlease enter Dividend number:'))
            calc.y = int(input('\nPlease enter Divisor number:'))
            quo = calc.division()
            print(f'\nQuotient is =', colored(quo, 'yellow'))
        elif uinp == 4:
            calc.x = int(input('\nPlease enter Dividend number:'))
            calc.y = int(input('\nPlease enter Divisor number:'))
            rem = calc.modulo()
            print(f'\nRemainder is =', colored(rem, 'yellow'))
        elif uinp == 5:
            calc.x = int(input('\nPlease enter first number:'))
            calc.y = int(input('\nPlease enter second number:'))
            mul = calc.multipication()
            print(f'\nMultiply of \"{calc.x}\" and \"{calc.y}\" is =', colored(mul, 'yellow'))
        elif uinp == 6:
            calc.x = int(input('\nPlease enter the number to find root:'))
            sq = calc.squart()
            print(f'\nSquare root of \"{calc.x}\" is =', colored(sq, 'yellow'))
        elif uinp == 7:
            calc.x = int(input('\nPlease enter main number :'))
            calc.n = int(input('\nPlease enter number which is power of:'))
            power = calc.powerofn()
            print(f'\n\"{calc.x}\" to the power of \"{calc.n}\" is =', colored(power, 'yellow'))
        elif uinp == 8:
            calc.o = float(input('\nPlease enter Triangle Opposite :'))
            calc.h = float(input('\nPlease enter Triangle hypotenuse :'))
            soh = calc.sin()
            print(f'\nSinθ theta is =', colored(soh, 'yellow'))
        elif uinp == 9:
            calc.a = float(input('\nPlease enter Triangle Adjacent :'))
            calc.h = float(input('\nPlease enter Triangle hypotenuse :'))
            cah = calc.cos()
            print(f'\nCosθ theta is =', colored(cah, 'yellow'))
        elif uinp == 10:
            calc.o = float(input('\nPlease enter Triangle Opposite :'))
            calc.a = float(input('\nPlease enter Triangle Adjacent :'))
            toa = calc.tan()
            print(f'\nTangentθ theta is =', colored(toa, 'yellow'))
        elif uinp == 11:
            calc.a = float(input('\n Please enter the value of radius : '))
            area = calc.are()
            print(f'\narea of a circle is =', colored(area, 'yellow'))
        elif uinp == 12:
            urdi = input("If you have Diameter enter \"D\" or you have circumference enter \"C\": ").lower()
            if urdi == 'd':
                calc.d = float(input('\n Enter the value of Diameter : '))
                rd1 = calc.radid()
                print(f'\nradius of a circle is =', colored(rd1, 'yellow'))
            elif urdi == 'c':
                calc.c = float(input('\n Enter the value of circumference : '))
                rd2 = calc.radic()
                print(f'\nradius of a circle is =', colored(rd2, 'yellow'))
            else:
                print('Invalid Input detected')
        elif uinp == 13:
            calc.p = float(input('\n Please enter the percentage value : '))
            calc.v = float(input('\n Please enter the value to percentage of  : '))
            per = calc.salper()
            print(f'\n \"{calc.p}%\" of \"{calc.v}\" is =', colored(per, 'yellow'))
        elif uinp == 14:
            calc.x = int(input('\n Please enter the number u want to calculate table of : '))
            print(f'\nTable of {calc.x} is below\n')
            for i in range(1, 11):
                print(calc.x, 'x', i, '=', calc.x*i)
        elif uinp == 15:
            calc.a = float(input('\n Please enter the "a" value: '))
            calc.b = float(input('\n Please enter the "b" value: '))
            calc.c = float(input('\n Please enter the "c" value: '))
            print('\n', calc.quatradic_r())
        elif uinp == 16:
            print('This is a Pythagorean Theorem calculator! Calculate one side of right-angled triangle.')
            print('\nAssume the sides are a, b, c and c is the hypotenuse.')
            choice = input('\nWhich side (a, b, c) do you want to calculate? side: ')
            if choice == 'c':
                calc.a = float(input('\nEnter the length of side a:'))
                calc.b = float(input('\nEnter the length of side b:'))
                c = calc.pythagores_c()
                print(f'\nThe length of side \'c\' is = {c}')
            elif choice == 'b':
                calc.a = float(input('\nEnter the length of side a:'))
                calc.c = float(input('\nEnter the length of side c:'))
                b = calc.pythagores_b()
                print(f'\nThe length of side \'b\' is = {b}')
            elif choice == 'a':
                calc.b = float(input('\nEnter the length of side b:'))
                calc.c = float(input('\nEnter the length of side c:'))
                a = calc.pythagores_a()
                print(f'\nThe length of side \'a\' is = {a}')
            else:
                print('\nInvalid Input detected')
        elif uinp == 17:
            calc.n = int(input('\n Please enter the number to find fibonacci sequence : '))
            fibo = calc.fibonacci_itrate()
            print(f"Fibonacci sequence of {calc.n} is: -", colored(fibo, 'yellow'))
    except ValueError as vr:
        print("Dont type any letter or special characters, ", vr)
    except ZeroDivisionError as zd:
        print("Dividing by zero is not possibe, ", zd)
        # else:
        #     print('Invalid input detected')
    stop = input("If you want to re calculate enter \"Y\" or you can enter \"N\": ").lower().strip()
    if stop == 'y':
        continue
    elif stop == 'n':
        break
    else:
        print('Entered invalid Input')
















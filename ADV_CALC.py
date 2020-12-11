import math
from termcolor import colored

class calculator:

    def addation(self, x, y):
        z = x + y
        return z

    def subtraction(self, x, y):
        z = x - y
        return z

    def division(self, x, y):
        z = x // y
        return z

    def modulo(self, x, y):
        z = x % y
        return z

    def multipication(self, x, y):
        z = x * y
        return z

    def squart(self, x):
        z = math.sqrt(x)
        return z

    def powerofn(self, x, n):
         z = math.pow(x, n)
         return z

    def sin(self, o, h):
        sin0 = o/h
        return sin0

    def cos(self, a, h):
        cos0 = a/h
        return cos0

    def tan(self, o, a):
        tan0 = o/a
        return tan0

    def are(self, x):
        area = math.pi * math.pow(x, 2)
        return area

    def radid(self, d):
        r1 = d/2
        return r1

    def radic(self, c):
        r1 = c / 2 * math.pi
        return r1

    def salper(self, x, y):
        pers = (x * y) / 100
        return pers

    def quatradic_r(self, a, b, c):
        dec = (b**2) - (4*a*c)
        if dec > 0:
            num_root = 2
            root1 = (((-b) + math.sqrt(dec))/(2*a))
            root2 = (((-b) - math.sqrt(dec))/(2*a))
            return 'Two distinct real root exist: root1 = %.2f and root2 = %.2f' % (root1, root2)
        elif dec == 0:
            num_root = 1
            root12 = (-b) / (2*a)
            return 'There is a one ', root12
        elif(dec < 0):
            num_root = 0
            return 'No roots, discriminant < 0.'

    def pythagores_c(self, a, b):
        c = math.sqrt((a*a) + (b*b))
        return c

    def pythagores_b(self, a, c):
        b = math.sqrt((c*c) - (a*a))
        return b

    def pythagores_a(self, b, c):
        a = math.sqrt((c*c) - (b*b))
        return a

calc = calculator()

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

    uinp = int(input('\nplease enter number: '))
    if uinp == 1:
        x = int(input('\nPlease enter first number:'))
        y = int(input('\nPlease enter second number:'))
        add = calc.addation(x, y)
        print(f'\nTotal of \"{x}\" and \"{y}\" is =', colored(add, 'yellow'))
    elif uinp == 2:
        x = int(input('\nPlease enter first number:'))
        y = int(input('\nPlease enter second number:'))
        sub = calc.subtraction(x, y)
        print(f'\nSubtraction of \"{y}\" from \"{x}\" is =', colored(sub, 'yellow'))
    elif uinp == 3:
        x = int(input('\nPlease enter Dividend number:'))
        y = int(input('\nPlease enter Divisor number:'))
        quo = calc.division(x, y)
        print(f'\nQuotient is =', colored(quo, 'yellow'))
    elif uinp == 4:
        x = int(input('\nPlease enter Dividend number:'))
        y = int(input('\nPlease enter Divisor number:'))
        rem = calc.modulo(x, y)
        print(f'\nRemainder is =', colored(rem, 'yellow'))
    elif uinp == 5:
        x = int(input('\nPlease enter first number:'))
        y = int(input('\nPlease enter second number:'))
        mul = calc.multipication(x, y)
        print(f'\nMultiply of \"{x}\" and \"{y}\" is =', colored(mul, 'yellow'))
    elif uinp == 6:
        x = int(input('\nPlease enter the number to find root:'))
        sq = calc.squart(x)
        print(f'\nSquare root of \"{x}\" is =', colored(sq, 'yellow'))
    elif uinp == 7:
        x = int(input('\nPlease enter main number :'))
        y = int(input('\nPlease enter number which is power of:'))
        power = calc.powerofn(x, y)
        print(f'\n\"{x}\" to the power of \"{y}\" is =', colored(power, 'yellow'))
    elif uinp == 8:
        o = float(input('\nPlease enter Triangle Opposite :'))
        h = float(input('\nPlease enter Triangle hypotenuse :'))
        soh = calc.sin(o, h)
        print(f'\nSinθ theta is =', colored(soh, 'yellow'))
    elif uinp == 9:
        a = float(input('\nPlease enter Triangle Adjacent :'))
        h = float(input('\nPlease enter Triangle hypotenuse :'))
        cah = calc.cos(a, h)
        print(f'\nCosθ theta is =', colored(cah, 'yellow'))
    elif uinp == 10:
        o = float(input('\nPlease enter Triangle Opposite :'))
        a = float(input('\nPlease enter Triangle Adjacent :'))
        toa = calc.tan(o, a)
        print(f'\nTangentθ theta is =', colored(toa, 'yellow'))
    elif uinp == 11:
        a = float(input('\n Please ether the value of radius : '))
        area = calc.are(a)
        print(f'\narea of a circle is =', colored(area, 'yellow'))
    elif uinp == 12:
        urdi = input("If you have Diameter enter \"D\" or you have circumference enter \"C\": ").lower()
        if urdi == 'd':
            d = float(input('\n Enter the value of Diameter : '))
            rd1 = calc.radid(d)
            print(f'\nradius of a circle is =', colored(rd1, 'yellow'))
        elif urdi == 'c':
            c = float(input('\n Enter the value of circumference : '))
            rd2 = calc.radic(c)
            print(f'\nradius of a circle is =', colored(rd2, 'yellow'))
        else:
            print('Invalid Input detected')
    elif uinp == 13:
        p = float(input('\n Please ether the percentage value : '))
        v = float(input('\n Please ether the value to percentage of  : '))
        per = calc.salper(p, v)
        print(f'\n \"{p}%\" of \"{v}\" is =', colored(per, 'yellow'))
    elif uinp == 14:
        x = int(input('\n Please ether the number u want to calculate table of : '))
        print(f'\nTable of {x} is below\n')
        for i in range(1, 11):
            print(x, 'x', i, '=', x*i)
    elif uinp == 15:
        a = float(input('\n Please enter the "a" value: '))
        b = float(input('\n Please ether the "b" value: '))
        c = float(input('\n Please ether the "c" value: '))
        print('\n', calc.quatradic_r(a, b, c))
    elif uinp == 16:
        print('This is a Pythagorean Theorem calculator! Calculate one side of right-angled triangle.')
        print('\nAssume the sides are a, b, c and c is the hypotenuse.')
        choice = input('\nWhich side (a, b, c) do you want to calculate? side: ')
        if choice == 'c':
            a = float(input('\nEnter the length of side a:'))
            b = float(input('\nEnter the length of side b:'))
            c = calc.pythagores_c(a, b)
            print(f'\nThe length of side \'c\' is = {c}')
        elif choice == 'b':
            a = float(input('\nEnter the length of side a:'))
            c = float(input('\nEnter the length of side c:'))
            b = calc.pythagores_b(a, c)
            print(f'\nThe length of side \'b\' is = {b}')
        elif choice == 'a':
            b = float(input('\nEnter the length of side b:'))
            c = float(input('\nEnter the length of side c:'))
            a = calc.pythagores_a(b, c)
            print(f'\nThe length of side \'a\' is = {a}')
        else:
            print('\nInvalid Input detected')

    else:
        print('Invalid input detected')
    stop = input("If you want to re calculate enter \"Y\" or you can enter \"N\": ").lower().strip()
    if stop == 'y':
        continue
    elif stop == 'n':
        break
    else:
        print('Entered invalid Input')
















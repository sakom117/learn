                # lesson 42 type() -возвращает тип агрумента
                # lesson 41 abs() - модуль числа

'''            # lesson40 print()
#с разделителем
print("you are", "bla-bla", "the best one", sep = ':::')
#с окончанием
print("123", end = ' ')


                # lesson39 eval() самостоятельно выбирает int|float
                в зависимости от поступивших данных
number = input("enter a number: ")
double_number = number * 3
double_number_int = int(number) * 3
print(double_number, double_number_int)

number = eval(input("enter a number: "))
double_number = number * 3
print(double_number)

result = eval("1 + 2 + 3 + 4 + 5 + 6")
print(result)       # он сложит и выдаст 21 в результат

calc = input("напиши уравнение для у: ")
for x in range(0, 30, 10):
    print("For x =", x, ": y = ", eval(calc))


                # lesson 37-38 ord() func - показывает код символа в Юникоде,
                 chr() func - показывает символ по указанному коду
chars = 'ABCD abcd'
for char in chars:
    char_code = ord(char)
    print(char, char_code)

for code in range(97, 97 + 26):
    char = chr(code)
    print(code, char)

for code in range(58, 64):
    char = chr(code)
    print(code, char)


                    # lesson 34-36 multiple assignment, trace tables,
                  simultanious assignment
x = 1
y = 2
print(x, y)
x, y = y, x
print(x, y)

# trace tables
a = 1
b = 2
c = 3
x, y, z = a, b, c
print(x, y, z)

# simultanious assignment
a = 0
b = 1
a = b
b = a + b
print(a, b)

x = 0
y = 1
x, y = y, x + y
print(x, y)


                # lesson 31-32 logic operations NOT, AND, OR
#    c = a OR b
#    a   b   c
#    t   t   T
#    t   f   T       C true когда один из операторов или оба true
#    f   t   T
#    f   f   F

#    c = a AND b
#    a   b   c
#    t   t   T
#    t   f   F       C true когда оба оператора true
#    f   t   F
#    f   f   F

age = int(input("Age: "))
income = int(input("Annual income: "))
if (age >= 18) and (income >= 1000):
    print('zbs')
else:
    print('fig tebe')


                # lesson 29-30 arithmetic operations

x = 10
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)    # неделимый остаток после деления Х на У
print(x ** y)   # возведение в степень
print(x // y)   # деление с отбрасыванием дробной части


                # lesson 28 FOR func (for count in (0,1,2))

for count in (0, 1, 2):
    print(count)
print("end of count 1")
for count in range(0, 10, 3):
    print(count)
print("end of count 2")


                # lesson 27 RANGE func range(start,stop,[step])

x = range(0, 10 , 1)
y = list(x)
print(y)

                # lesson 26 IF-ELIF-ELSE func

i = int(input("Enter percentage mark: "))
if i >= 70:
    print("distinction")
elif 60 <= i <= 69:
    print("merit")
elif 40 <= i <= 59:
    print("merit")
else:
    print("fail")


hpr = float(input("rate per hour: "))
hw = float(input("hours worked: "))
gross_pay = int(hpr*hw)
print('the gross is ' + str(gross_pay))


count = 10
y = 2
print(count)
count += 1
print(count)

# lesson 20
bank_charge = 10
bonus = 7
balance = 10
if balance < 0:
    balance = balance - bank_charge
else:
    balance = balance + bonus
print('the account balance is ' + str(balance))
'''

# def f1():
#
#     num1 = int(input('введи первое число\n'))
#     num2 = int(input('введи второе число\n'))
#     num3 = int(input('введи третье число\n'))
#     otvet = input('что с ними сделать?, * - умножить, + - сложить\n')
#     if otvet=='*':
#         result = num1*num2*num3
#         print(f'произведение чисел равно {result}')
#     elif otvet=='+':
#         result = num1+num2+num3
#         print(f'сумма чисел равна {result}')
#     else:
#         print('Выбери из того что предлогают.')

# f1()

def calc(znak):
    if znak == '+':
        result = num1 + num2
        print(f"Сумма чисел равна {result}")
    elif znak == '-':
        result = num1 - num2
        print(f"Разность чисел равна {result}")
    elif znak == '*':
        result = num1 * num2
        print(f"Произведение чисел равно {result}")
    elif znak == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Частное чисел равно {result}")
        else:
            print("ERROR на ноль не делим")


while True:
    num1 = int(input('Введите первое число\n'))
    num2 = int(input('Введите второе число\n'))
    znak = input("Выберите операцию +, -, *, / или введите 'q' для выхода\n")

    if znak == 'q':
        break
    elif znak not in ['+', '-', '*', '/']:
        continue

    calc(znak)


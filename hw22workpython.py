# num = int(input('число\n'))
# ...
# if(){
#
#
# }
# ...

# if num > 0:
#     print('ok')
#     if num>10:
#         print('ok 10')
#         if num>20:
#             print('ok 20')

# else:
#     print('neok')

# if num > 0:
#     print('ok')
# elif num==10:
#     print('ok 10')
# elif num<0:
#     print('ok 20')
#
# else:
#     print('neok')

# num = int(input('Сколько лет коту вашему\n'))
# if (num ==0 and num<=1):
#     print('мелкий')
# elif (num ==5 and num<=9):
#     print('взрослый')
# elif (num >10):
#     print('очень взрослый')
#
# else:
#     print('не верно')

# num = int(input('Сколько будет 2 * 2\n'))
# num1 = int(input('Сколько будет 2 + 2\n'))
# num2 = int(input('Сколько будет 2 - 2\n'))

# if num == 4:
#     print('verno')
#     num1 = int(input('Сколько будет 2 + 2\n'))
#     else:
#     print('ne verno')
#        if num1 == 4:
#         print('verno +')
#             else:
#         print('ne verno')
#         num2 = int(input('Сколько будет 2 - 2\n'))
#                 if num2 == 0:
#             print('verno ++')
#                     else:
#             print('ne verno')
# print('proshel ')

# n1 = '2'
# n2 = '2'
# print(n1+n2)
# name = 'barsik'
# print('hello',name, sep='###', end='end\n')
# print('hello',name, sep='###', end='end\n')

# def f1():
#     print('hello')
#     pass
# def f2(n='cow', x=11):
#     print('world',n,x)
#     pass
# f1()
# f2('cat',33)
# f2()
num = 1
def talon(bukva):
    print('ваш номер', bukva, num)
    pass
while True:
    otvet = input('куда 1-банк, 2-цирк,3-поликлинника')
    if otvet=='1':
        talon('Б')
        num+=1
    elif otvet=='2':
        talon('Ц')
        num+=1
    elif otvet=='3':
        talon('П')
        num+=1
    elif otvet ==  'q':
        break





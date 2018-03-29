import random
number = []
numberString = ''
test = True
i = 0
num = 0
comparison = ''
bulls = 0
cows = 0
print('Правила игры:')
print('Загадано 4-х значное число, состоящее из не повторяющихся цифр,')
print('ваша задача угадать это число.')
print('Если в вашем числе будет стоять цифра, такая же как и в загаданном числе')
print('и на том же месте что и в загаданном, то будет добавлен бык.')
print('Если в вашем числе будет находиться цифра, которая есть в загаданном')
print('числе, но не соответствует позиции будет добавлена корова.')
print('')
while len(number) < 4:
    test = True
    num = random.randint(0,9)
    while i < len(number) and test == True:
        if num == number[i]:
            test = False
        else:
            test = True
        i = i + 1
    if test == True:
        number.append(num)
    i = 0
while i < 4:
    numberString = numberString + str(number[i])
    i = i + 1
while bulls < 4:
    bulls = 0
    cows = 0
    i = 0
    comparison = str(input('Введите 4 цифры, учтите что цифры не могут повторяться: '))
    if len(comparison) == 4 and comparison[0] != comparison[1] and comparison[0] != comparison[2] and comparison[0] != comparison[3] and comparison[1] != comparison[2] and comparison[1] != comparison[3] and comparison[2] != comparison[3]:
        while i < 4:
            if comparison[i] == numberString[i]:
                bulls = bulls + 1
            else:
                if comparison[i] == numberString[0]:
                    cows = cows + 1
                if comparison[i] == numberString[1]:
                    cows = cows + 1
                if comparison[i] == numberString[2]:
                    cows = cows + 1
                if comparison[i] == numberString[3]:
                    cows = cows + 1
            i = i + 1
        print('Bulls:', bulls)
        print('Cows:', cows)
    else:
        print('Вы ввели не 4 цифры, либо цифры повторились!')
print('Загаданное число:', numberString)
print('Ваше число: ', comparison)
print('Поздравляю с победой, вы угадали число!!!!!!!!!!')

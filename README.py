import random
number = []
numberString = ''
test = True
i = 0
num = 0
comparison = ''
bulls = 0
cows = 0
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
print('Загаданное число:', numberString)
print('Ваше число: ', comparison)
print('Поздравляю с победой, вы угадали число!!!!!!!!!!')

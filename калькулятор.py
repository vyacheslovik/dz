import math

results = []
functions = ('Сложение','вычитание', 'умножение', 'деление', 'возведение в степень', 'логарифм',
'округление в большую сторону', 'округление в меньшую сторону')
while True:
    
    if len(results) != 0:
        for i in range(len(results)):
            print(f'{i+1} результат =',results[i])
            
    ### СЧИТЫВАНИЕ ФУНКЦИИ
    print(f'Введите необходимую функцию {functions}')
    while True:
        func = str(input())
        if func in functions:
            break
        else:
            print('Введите допустимую функцию!!')
            
    ### СЧИТЫВАНИЕ ЧИСЕЛ
    print('Введите первое число')
    try:
        first = float(input())
        first = float(first)
    except:
        print('Введите число!')
        try:
            first = float(input())
            first = float(first)
        except:
            print('Пока:)')
            break
            
    print('Введите второе число')
    try:
        second = float(input())
        second = float(second)
    except:
        print('Введите число!')
        try:
            second = float(input())
            second = float(second)
        except:
            print('Пока:)')
            break
            
    ### РАБОТА С ЧИСЛАМИ        
    if func == 'Сложение':
        if first+second == int(first+second):
            print(int(first+second))
            results.append(int(first+second))
        else:
            print(first+second)
            results.append(first+second)
        
    if func == 'вычитание':
        if first-second == int(first-second):
            print(int(first-second))
            results.append(int(first-second))
        else:
            print(first-second)
            results.append(first-second)

    if func == 'умножение':
        if first*second == int(first*second):
            print(int(first*second))
            results.append(int(first*second))
        else:
            print(first*second)
            results.append(first*second)
        
    if func == 'деление':
        if first/second == first//second:
            print(first//second)
            results.append(first//second)
        else:
            print(first/second)
            results.append(first/second)

    if func == 'возведение в степень':
        if first**second == int(first**second):
            print(int(first**second))
            results.append(int(first**second))
        else:
            print(first**second)
            results.append(first**second)

    if func == 'логарифм':
        if math.log(second,first) == int(math.log(second,first)):
            print(int(math.log(second,first)))
            results.append(int(math.log(second,first)))
        else:
            print(math.log(second,first))
            results.append(math.log(second,first))

    if func == 'округление в большую сторону':
        print('С каким числом работаем?(1,2)')
        try:
            number = int(input())
        except:
            number = 's'
        while number not in (1,2):
            print('Введите 1 или 2!!')
            try:
                number = int(input())
            except:
                continue
        print('Введите число N до какой цифры после запятой нужно округлить')
        try:
            N = int(input())
        except:
            N = 's'
        while type(N) != type(5):
            print('Введите корректное число!')
            try:
                N = int(input())
            except:
                continue
        if number == 1:
            while N+2 > len(str(first)):
                print('Введите допустимое значение!')
                N = int(input())
            if int(str(first)[N+1]) != 9:
                print(str(first)[:N+1] + str(int(str(first)[N+1]) + 1))
                results.append(float(str(first)[:N+1] + str(int(str(first)[N+1]) + 1)))
            elif N == 1:
                print(int(first) + 1)
                results.append(int(first) + 1)
            else:
                print(str(first)[:N] + str(int(str(first)[N]) + 1))
                results.append(float(str(first)[:N] + str(int(str(first)[N]) + 1)))
        else:
            while N+2 > len(str(second)):
                print('Введите допустимое значение!')
                N = int(input())
            if int(str(second)[N+1]) != 9:
                print(str(second)[:N+1] + str(int(str(second)[N+1]) + 1))
                results.append(float(str(second)[:N+1] + str(int(str(second)[N+1]) + 1)))
            elif N == 1:
                print(int(second) + 1)
                results.append(int(second) + 1)
            else:
                print(str(second)[:N] + str(int(str(second)[N]) + 1))
                results.append(float(str(second)[:N] + str(int(str(second)[N]) + 1)))

    if func == 'округление в меньшую сторону':
        print('С каким числом работаем?(1,2)')
        try:
            number = int(input())
        except:
            number = 's'
        while number not in (1,2):
            print('Введите 1 или 2!!')
            try:
                number = int(input())
            except:
                continue
        print('Введите число N до какой цифры после запятой нужно округлить')
        try:
            N = int(input())
        except:
            N = 's'
        while type(N) != type(5):
            print('Введите корректное число!')
            try:
                N = int(input())
            except:
                continue
        if number == 1:
            while N+2 > len(str(first)):
                print('Введите допустимое значение!')
                N = int(input())
            if int(str(first)[N+1]) not in (0,1):
                print(str(first)[:N+1] + str(int(str(first)[N+1])))
                results.append(float(str(first)[:N+1] + str(int(str(first)[N+1]))))
            elif N == 1:
                print(int(first))
                results.append(int(first))
            else:
                print(str(first)[:N] + str(int(str(first)[N])))
                results.append(float(str(first)[:N] + str(int(str(first)[N]))))
        else:
            while N+2 > len(str(second)):
                print('Введите допустимое значение!')
                N = int(input())
            if int(str(second)[N+1]) not in (0,1):
                print(str(second)[:N+1] + str(int(str(second)[N+1])))
                results.append(float(str(second)[:N+1] + str(int(str(second)[N+1]))))
            elif N == 1:
                print(int(second))
                results.append(int(second))
            else:
                print(str(second)[:N] + str(int(str(second)[N])))
                results.append(float(str(second)[:N] + str(int(str(second)[N]))))
    print('Вы желаете продолжить работу с калькулятором?')
    ans = str(input())
    if ans not in ('да','Да','дА','ДА'):
        print('Ваши результаты:',results)
        break

    
            
            
            
        
    


    
    

    

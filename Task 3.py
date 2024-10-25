a = int(input('Beginning: '))
b = int(input('End: '))
a, b = (b, a) if a > b else (a, b)

while a != b:
    if  a % 3 == 0 and  a % 5 == 0:
        print('Fizz Buzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print(a)

    a += 1
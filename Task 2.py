a = int(input('Beginning: '))
b = int(input('End: '))

def firstTask(beginning, end):
    result = str()
    while beginning != end + 1:
        result += f'{beginning} '
        beginning += 1

    return result

def secondTask(beginning, end):
    result = str()

    while end != beginning - 1:
        result += f'{end} '
        end -= 1

    return result

def thirdTask(beginning, end):
    result = str()

    while beginning != end + 1:
        if beginning % 7 == 0:
            result += f'{beginning} '
        beginning += 1

    return result

def fourthTask(beginning, end):
    result = int()

    while beginning != end + 1:
        if beginning % 5 == 0:
            result += 1
        beginning += 1

    return result

a, b = (b, a) if a > b else (a, b)

print(f'1. All numbers in the range: {firstTask(a, b)}')
print(f'2. All numbers in the range in descending order: {secondTask(a, b)}')
print(f'3. All numbers that are a multiple of 7: {thirdTask(a, b)}')
print(f'4. The number of numbers that are multiples of 5: {fourthTask(a, b)}')
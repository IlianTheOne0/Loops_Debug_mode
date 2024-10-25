beginning = int(input('Beginning: '))
end = int(input('End: '))

beginning, end = (end, beginning) if beginning > end else (beginning, end)

while beginning != end + 1:
    if beginning % 7 == 0:
        print(beginning)
    beginning += 1
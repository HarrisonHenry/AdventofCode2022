with open('Day1Part1.txt') as RawInput:
    currentList = []
    biggest = 0
    for i in RawInput:
        if i == '\n':
            x = sum(currentList)
            if biggest < x:
                biggest = x
            currentList = []
        else:
            i = int(i.strip('\n'))
            currentList.append(i)
    print(biggest)        
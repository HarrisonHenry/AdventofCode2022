with open('Day1Part1.txt') as RawInput:
    currentList = []
    sumList = []
    for i in RawInput:
        if i == '\n':
            sumList.append(sum(currentList))
            currentList = []
        else:
            i = int(i.strip('\n'))
            currentList.append(i)
    sumList.sort()
    print(sumList[-1] + sumList[-2] + sumList[-3])

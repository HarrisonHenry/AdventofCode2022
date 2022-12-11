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
    finalList = sumList.sort()
    print(finalList) 
    print(sorted(sumList))    
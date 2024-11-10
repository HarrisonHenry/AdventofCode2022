with open('Day5input.txt') as RawInput:
    counter = 0
    instructionList = []
    containerList =[['F', 'C', 'P', 'G', 'Q', 'R'],
    ['W', 'T', 'C', 'P'],
    ['B', 'H', 'P', 'M', 'C'],
    ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
    ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
    ['D', 'P', 'J'],
    ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
    ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
    ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']]
    for i in RawInput:
        if counter >=10:
            i = i.split()
            instructionList.append(i)
        counter += 1
for i in instructionList:
    interimList = []
    for n in range(int(i[1])):
        interimList.append(containerList[int(i[3])-1].pop())

    for n in interimList:
        containerList[int(i[5])-1].append(interimList.pop())
    print(interimList)

resultStr = ''
for i in containerList:
    resultStr += i[-1]
print(resultStr)

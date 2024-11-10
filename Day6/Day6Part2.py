with open('Day6input.txt') as RawInput:
    inputStr = RawInput.readline().strip()

counter = 0
evalList = []

for i in inputStr:
    if counter>=14:
        if len(set(evalList)) == 14:
            print(counter)
            break
        evalList.pop(0)
        evalList.append(i)
    else:
        evalList.append(i)
    counter += 1

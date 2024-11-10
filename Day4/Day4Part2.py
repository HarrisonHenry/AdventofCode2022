import re
with open('Day4input.txt') as RawInput:
    score = 0
    for i in RawInput:
        i = i.strip()
        i = re.split(('[,-]'), i)

        rangeA = range(int(i[0]), int(i[1])+1)
        rangeB = range(int(i[2]), int(i[3])+1)

        for i in rangeA:
            if i in rangeB:
                score+=1
                break

    print(score)

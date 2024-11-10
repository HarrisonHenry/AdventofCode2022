with open('Day3input.txt') as RawInput:
    score = 0
    RawList = []
    counter = 0
    for i in RawInput:
        RawList.append(i.strip())
    for i in range(0, len(RawList), 3):
        found = False
        counter += 1
        for x in RawList[i]:
            for y in RawList[i+1]:
                for z in RawList[i+2]:
                    if x == y == z:
                        print(x)
                        if ord(x) >= 97:
                            score += ord(x)-96
                        else:
                            score += ord(x)-38
                        found = True
                        break
                if found == True:
                    break
            if found == True:
                break
    print(score)

with open('Day3input.txt') as RawInput:
    score = 0
    for i in RawInput:
        i = i.strip()
        size = int ((len(i))/2)
        firstHalf = i[0:size]
        secondHalf = i[size:]
        found = False
        for x in firstHalf:
            for y in secondHalf:
                if x == y:
                    if ord(x) >= 97:
                        score += ord(x)-96
                    else:
                        score += ord(x)-38
                    found = True
                    break
            if found:
                break
    print(score)

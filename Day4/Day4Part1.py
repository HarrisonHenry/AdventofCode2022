import re
with open('Day4input.txt') as RawInput:
    score = 0
    for i in RawInput:
        i = i.strip()
        i = re.split(('[,-]'), i)

        if int(i[0]) >= int(i[2]) and int(i[1]) <= int(i[3]):
            print(i)
        elif int(i[0]) <= int(i[2]) and int(i[1]) >= int(i[3]):
            score += 1

    print(score)

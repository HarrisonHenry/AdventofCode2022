solutionDict = {'A X' : 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z' : 9, 'C Z': 6}

with open('Day2input.txt') as RawInput:
    score = 0
    for i in RawInput:
        score += solutionDict[i.strip()]
    print(score)
solutionDict = {'A X' : 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z' : 9, 'C Z': 7}

with open('Day2input.txt') as RawInput:
    score = 0
    for i in RawInput:
        score += solutionDict[i.strip()]
    print(score)
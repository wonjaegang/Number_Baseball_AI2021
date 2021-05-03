import random


# Randomly set secret number
def setSecretNum(digit):
    secretNum = []
    for _ in range(digit):
        while True:
            num = random.randrange(0, 10)
            if num not in secretNum:
                secretNum.append(num)
                break
    return secretNum


# select secret number
def setQuestionNum(digit):
    questionNum = []
    for _ in range(digit):
        while True:
            num = random.randrange(0, 10)
            if num not in questionNum:
                questionNum.append(num)
                break
    return questionNum

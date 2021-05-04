
# =================================== AI pitcher : Oh ============================================
#
#   Oh's strategy:
#     - Oh 'RANDOMLY' pick his secret number.
#     - Oh 'RANDOMLY' pick his question number among the 'AVAILABLE NUMBERS'.
#
# ================================================================================================

import random

digit = 0
lastQuestion = ""
lastReply = False


class AnswerSet:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0


def initializeAI(setDigit):
    global digit
    digit = setDigit


def setSecretNum():
    secretNum = ""
    for _ in range(digit):
        while True:
            num = str(random.randrange(0, 10))
            if num not in secretNum:
                secretNum = secretNum + num
                break
    return secretNum


def setQuestionNum():

    questionNum = "1234"

    global lastQuestion
    lastQuestion = questionNum
    return questionNum


def checkReply(targetNum, questionNum):
    answerSet = AnswerSet()
    for index, num in enumerate(questionNum):
        if num in targetNum:
            if targetNum.index(num) == index:
                answerSet.strike += 1
            else:
                answerSet.ball += 1
        else:
            answerSet.out += 1
    return answerSet

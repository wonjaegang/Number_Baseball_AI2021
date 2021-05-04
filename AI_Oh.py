
# =================================== AI pitcher : Oh ============================================
#
#   Oh's strategy:
#     - Oh 'RANDOMLY' pick his secret number.
#     - Oh 'RANDOMLY' pick his question number among the 'AVAILABLE NUMBERS'.
#
# ================================================================================================

import random
import itertools


digit = 0
lastQuestion = ""
lastReply = False
availableTarget = []


# Set digit, initialize available target numbers.
def initializeAI(setDigit):
    global digit
    digit = setDigit
    availableTarget.extend(list(map(lambda x: "".join(x), list(itertools.permutations("0123456789", digit)))))


def setSecretNum():
    secretNum = random.choice(availableTarget)
    print(availableTarget)
    return secretNum


def setQuestionNum():

    questionNum = "1234"

    global lastQuestion
    lastQuestion = questionNum
    return questionNum


def updateAvailable():
    pass


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


class AnswerSet:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0

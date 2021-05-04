
# =================================== AI pitcher : PARK ==========================================
#
#   PARK's strategy:
#     - PARK 'RANDOMLY' pick his secret number.
#     - PARK pick his question number Which has the 'HIGHEST CHANCE' to 'MINIMIZE' available number
#            among the 'AVAILABLE NUMBERS'
#
# ================================================================================================

import random
import itertools

digit = 0
lastQuestion = ""
lastReply = []
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
    updateAvailableTarget()
    questionNum = random.choice(availableTarget)
    global lastQuestion
    lastQuestion = questionNum
    return questionNum


def updateAvailableTarget():
    if lastReply:
        correctNums = []
        for target in availableTarget:
            if checkReply(target, lastQuestion).strike == lastReply[0]:
                if checkReply(target, lastQuestion).ball == lastReply[1]:
                    if checkReply(target, lastQuestion).out == lastReply[2]:
                        correctNums.append(target)
        availableTarget.clear()
        availableTarget.extend(correctNums)


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

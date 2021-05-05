
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
lastQuestion = []
lastReply = []
availableTarget = []


# Set digit, initialize available target numbers.
def initializeAI(setDigit):
    global digit
    digit = setDigit
    availableTarget.extend(list(map(lambda x: "".join(x), list(itertools.permutations("0123456789", digit)))))


def setSecretNum():
    secretNum = random.choice(availableTarget)
    return secretNum


def setQuestionNum():
    if not lastReply:
        questionNum = random.choice(availableTarget)
    else:
        updated = checkAvailableTarget(availableTarget, lastQuestion.pop(), lastReply)
        availableTarget.clear()
        availableTarget.extend(updated)

        questionNum = random.choice(availableTarget)

    lastQuestion.append(questionNum)
    return questionNum


def checkAvailableTarget(availableList, question, reply):
    correctNums = []
    for target in availableList:
        if checkReply(target, question) == reply:
            correctNums.append(target)
    return correctNums


def checkReply(targetNum, questionNum):
    answerSet = [0, 0, 0]
    for index, num in enumerate(questionNum):
        if num in targetNum:
            if targetNum.index(num) == index:
                answerSet[0] += 1
            else:
                answerSet[1] += 1
        else:
            answerSet[2] += 1
    return answerSet

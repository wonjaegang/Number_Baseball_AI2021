
# =================================== AI pitcher : KIM ===========================================
#
#   KIM's strategy:
#     - Kim 'RANDOMLY' pick his secret number.
#     - Kim 'RANDOMLY' pick his question number.
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
    questionNum = random.choice(availableTarget)
    global lastQuestion
    lastQuestion = questionNum
    return questionNum

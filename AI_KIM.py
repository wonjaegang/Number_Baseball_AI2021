
# =================================== AI pitcher : KIM ===========================================
#
#   KIM's strategy:
#     - Kim 'RANDOMLY' pick his secret number.
#     - Kim 'RANDOMLY' pick his question number.
#
# ================================================================================================

import random

digit = 0
lastReply = 0


def setSecretNum(setDigit):
    global digit
    digit = setDigit
    secretNum = ""
    for _ in range(digit):
        while True:
            num = str(random.randrange(0, 10))
            if num not in secretNum:
                secretNum = secretNum + num
                break
    return secretNum


def setQuestionNum():
    questionNum = ""
    for _ in range(digit):
        while True:
            num = str(random.randrange(0, 10))
            if num not in questionNum:
                questionNum = questionNum + num
                break
    return questionNum

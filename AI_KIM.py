
# =================================== AI pitcher : KIM ===========================================
#
#   KIM's strategy:
#     - Kim 'RANDOMLY' pick his secret number.
#     - Kim 'RANDOMLY' pick his question number among the 'AVAILABLE NUMBERS'.
#
# ================================================================================================

import random


def setSecretNum(digit):
    secretNum = []
    for _ in range(digit):
        while True:
            num = random.randrange(0, 10)
            if num not in secretNum:
                secretNum.append(num)
                break
    return secretNum

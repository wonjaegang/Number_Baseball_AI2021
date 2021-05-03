import random
import AI_KIM

AINameList = ["김광현", "오승환", "박찬호", "양현종", "류현진"]


def setSecretNum(digit, AIName):
    if AIName == "김광현":
        return AI_KIM.setSecretNum(digit)
    elif AIName == "오승환":
        return 0
    elif AIName == "박찬호":
        return 0
    elif AIName == "양현종":
        return 0
    elif AIName == "류현진":
        return 0


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

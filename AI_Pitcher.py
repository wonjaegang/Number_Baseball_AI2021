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


def setQuestionNum(AIName):
    if AIName == "김광현":
        return AI_KIM.setQuestionNum()
    elif AIName == "오승환":
        return 0
    elif AIName == "박찬호":
        return 0
    elif AIName == "양현종":
        return 0
    elif AIName == "류현진":
        return 0

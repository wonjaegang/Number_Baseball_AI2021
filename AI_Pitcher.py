import AI_KIM
import AI_Oh

AINameList = ["김광현", "오승환", "박찬호", "양현종", "류현진"]


def name2header(name):
    if name == "김광현":
        return AI_KIM
    elif name == "오승환":
        return AI_Oh
    elif name == "박찬호":
        return AI_Oh
    elif name == "양현종":
        return AI_Oh
    elif name == "류현진":
        return AI_Oh


def setSecretNum(digit, AIName):
    return name2header(AIName).setSecretNum(digit)


def setQuestionNum(AIName):
    return name2header(AIName).setQuestionNum()


def listenReply(answer, AIName):
    name2header(AIName).lastReply = answer

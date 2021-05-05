import AI_KIM
import AI_Oh
import AI_PARK

AINameList = ["김광현", "오승환", "박찬호", "양현종", "류현진"]


def name2header(name):
    if name == "김광현":
        return AI_KIM
    elif name == "오승환":
        return AI_Oh
    elif name == "박찬호":
        return AI_PARK
    elif name == "양현종":
        pass
    elif name == "류현진":
        pass


def setSecretNum(digit, AIName):
    name2header(AIName).initializeAI(digit)
    return name2header(AIName).setSecretNum()


def setQuestionNum(AIName):
    return name2header(AIName).setQuestionNum()


def listenReply(answer, AIName):
    name2header(AIName).lastReply = answer

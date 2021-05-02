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

import AI_Pitcher
import Game_settings


class Umpire:
    def __init__(self):
        self.digits = Game_settings.digits
        self.secret_num = []

    def reply(self, playerNum, questionNum):
        answerSet = AnswerSet()
        target_secretNum = self.secret_num[1 - playerNum]
        for index, num in enumerate(questionNum):
            if num in target_secretNum:
                if target_secretNum.index(num) == index:
                    answerSet.strike += 1
                else:
                    answerSet.ball += 1
            else:
                answerSet.out += 1
        return answerSet


class Pitcher:
    def __init__(self, playerNum, playerType):
        self.playerNum = playerNum
        self.digit = Game_settings.digits
        self.type = playerType

    def receive_secretNum(self):
        if self.type == "User":
            return self.receive_secretNum_User()
        elif self.type == "AI":
            return self.receive_secretNum_AI()

    def receive_secretNum_User(self):
        print("Player%d, please enter your %d digit secret number." % (self.playerNum + 1, self.digit))
        secret_num = input()
        return secret_num

    def receive_secretNum_AI(self):
        pass
        return 0

    def receive_questionNum(self):
        print("Player%d, please enter your %d digit question number." % (self.playerNum + 1, self.digit))
        question_num = input()
        return question_num


class AnswerSet:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0

    def __str__(self):
        return 'Answer: {} Strike, {} Ball, {} Out'.format(self.strike, self.ball, self.out)


def StartingQuestion():
    print("===============Number Baseball Game===============")
    print("Please select the game type.")
    print("1. User VS User")
    print("2. User VS AI")
    answer = int(input())
    return answer


if __name__ == "__main__":
    gameType = StartingQuestion()
    if gameType == 1:
        player1 = Pitcher(0, "User")
        player2 = Pitcher(1, "User")
    else:
        player1 = Pitcher(0, "User")
        player2 = Pitcher(1, "AI")
    players = [player1, player2]
    umpire = Umpire()

    for player in players:
        secretNum = player.receive_secretNum()
        umpire.secret_num.append(secretNum)
        print("\n" * 20)

    gameOn = True
    inning = 0
    while gameOn:
        inning += 1
        print("***** Inning : %d *****" % inning)
        for order, player in enumerate(players):
            question = player.receive_questionNum()
            replied = umpire.reply(order, question)
            print(replied)
        print()

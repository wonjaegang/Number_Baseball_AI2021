import AI_Pitcher


class Umpire:
    def __init__(self):
        self.secret_num = []
        self.victory = [False, False]

    # Answer the question by comparing it to the opponent's secret number.
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
        if answerSet.strike == settings.digit:
            self.victory[playerNum] = True
        return answerSet

    # Make sure if the winner has been decided.
    def isGameOver(self):
        if sum(self.victory) == 2:
            print("***** DRAW!! ****")
            return True
        elif sum(self.victory) == 1:
            print("***** Player%d WIN!! *****" % (self.victory.index(True) + 1))
            return True
        else:
            return False


class Pitcher:
    def __init__(self, playerNum):
        self.playerNum = playerNum
        self.type = settings.playerType[playerNum]
        self.name = settings.playerName[playerNum]

    # Get secret number from user or AI. To AI, initialize the number of digit too.
    def receive_secretNum(self):
        if self.type == "User":
            return self.receive_secretNum_User()
        elif self.type == "AI":
            return self.receive_secretNum_AI()

    def receive_secretNum_User(self):
        print("Player%d, please enter your %d digit, non-duplicate secret numbers."
              % (self.playerNum + 1, settings.digit))
        secret_num = input()
        return secret_num

    def receive_secretNum_AI(self):
        print("Player%d, please enter your %d digit, non-duplicate secret numbers."
              % (self.playerNum + 1, settings.digit))
        secret_num = AI_Pitcher.setSecretNum(settings.digit, self.name)
        print(secret_num)
        return secret_num

    # Get question number from user or AI
    def receive_questionNum(self):
        if self.type == "User":
            return self.receive_questionNum_User()
        elif self.type == "AI":
            return self.receive_questionNum_AI()

    def receive_questionNum_User(self):
        print("Player%d, please enter your %d digit question numbers." % (self.playerNum + 1, settings.digit))
        question_num = input()
        return question_num

    def receive_questionNum_AI(self):
        print("Player%d, please enter your %d digit, question numbers."
              % (self.playerNum + 1, settings.digit))
        question_num = AI_Pitcher.setQuestionNum(self.name)
        print(question_num)
        return question_num

    # Send AI to umpire's reply
    def listenToReply(self, answer):
        if self.type == "AI":
            AI_Pitcher.listenReply(answer, self.name)


class AnswerSet:
    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0

    def __str__(self):
        return 'Answer: {} Strike, {} Ball, {} Out'.format(self.strike, self.ball, self.out)


class Settings:
    def __init__(self):
        self.digit = 4
        self.playerType = ["", ""]
        self.playerName = ["", ""]

    # Get settings from User input
    def getUserSettings(self):
        print("===============Number Baseball Game===============")
        print("Please select the game type.")
        print("1. User VS User")
        print("2. User VS AI")
        print("3. AI VS AI")
        answer = int(input())
        if answer == 1:
            self.playerType[0] = "User"
            self.playerName[0] = "User"
            self.playerType[1] = "User"
            self.playerName[1] = "User"
        elif answer == 2:
            self.playerType[0] = "User"
            self.playerName[0] = "User"
            self.playerType[1] = "AI"
            print("Please select your opponent.")
            self.getAIName(1)
        elif answer == 3:
            self.playerType[0] = "AI"
            self.playerType[1] = "AI"
            for i in range(2):
                print("Please select player%d." % (i + 1))
                self.getAIName(i)

    # Get AI name from int-type User input
    def getAIName(self, playerNum):
        for index, name in enumerate(AI_Pitcher.AINameList):
            print("%d.%s" % (index + 1, name))
        nameIndex = int(input())
        self.playerName[playerNum] = AI_Pitcher.AINameList[nameIndex - 1]


if __name__ == "__main__":
    # Set game settings and declare instances
    settings = Settings()
    settings.getUserSettings()
    player1 = Pitcher(0)
    player2 = Pitcher(1)
    players = [player1, player2]
    umpire = Umpire()

    # Set each player's secret number, and resister it to umpire instance
    for player in players:
        secretNum = player.receive_secretNum()
        umpire.secret_num.append(secretNum)
        print(".\n" * 20)

    # Game starts
    gameOn = True
    inning = 0
    while gameOn:
        inning += 1
        print("***** Player1(%s) VS Player2(%s) - Inning : %d *****" % (player1.name, player2.name, inning))
        for order, player in enumerate(players):
            question = player.receive_questionNum()
            replied = umpire.reply(order, question)
            print(replied)
            player.listenToReply(replied)
        print()
        if umpire.isGameOver():
            print("[It took %d inning(s)]" % inning)
            break

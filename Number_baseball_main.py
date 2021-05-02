import AI_Pitcher
import Game_settings


class Umpire:
    def __init__(self):
        self.digits = Game_settings.digits
        self.target_num = []


class Pitcher:
    def __init__(self, order):
        self.order = order
        self.digits = Game_settings.digits

        print("Enter player%d's object number." % order)
        self.object_num = input()
        umpire.target_num.append(self.object_num)


if __name__ == "__main__":
    umpire = Umpire()
    player1 = Pitcher(1)
    player2 = Pitcher(2)

    gameOn = True
    while gameOn:
        pass

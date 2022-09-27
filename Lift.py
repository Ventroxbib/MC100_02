
class Lift:
    velocity = 0.0
    level = 0
    targetLevel = 0

    def __init__(self, vel, lvl, tLvl):
        self.velocity = vel
        self.level = lvl
        self.targetLevel = tLvl


    def Movement(self):
        YDirection = ""
        while (self.level != self.targetLevel):
            if (self.level < self.targetLevel):
                YDirection = "faehrt aufwaerds"
                self.level += 1
                print("Zw->" + str(self.level))
            else:
                YDirection = "faehrt abwaerds"
                self.level -= 1
                print("Zw->" + str(self.level))
        self.level = self.targetLevel
        print("Aktuelle Etage: " + str(self.level))
        return YDirection

    def Display(self):
        print("Geschwindigkeit: ", str(self.velocity))
        print("Etage: ", str(self.level))
        print("Ziel Etage: ", str(self.targetLevel))

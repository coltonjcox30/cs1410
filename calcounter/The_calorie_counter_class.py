class Calorie_Counter():
    def __init__(self,Height,Weight,Age,Gender):
        self.mHeight = float(Height)
        self.mWeight = float(Weight)
        self.mAge = float(Age)
        self.mGender = Gender
        self.mBalance = 0
        self.CalCalculation()
    def CurrentBalance(self):
        return self.mBalance

    def AddCal (self, Add):
        self.mBalance = self.mBalance + float(Add)

    def CalCalculation(self):
        if self.mGender.upper() == 'M':
            self.mBalance = 0-(66 + (12.7 * self.mHeight) + (6.23 * self.mWeight) - (6.8 * self.mAge))
        if self.mGender.upper() == 'F':
            self.mBalance = 0-(655 + (4.7 * self.mHeight) + (4.35 * self.mWeight) - (4.7 * self.mAge))
    def Exercise(self,cpm,M):
        self.mBalance = self.mBalance - float(cpm * M * self.mWeight)


        
        
        







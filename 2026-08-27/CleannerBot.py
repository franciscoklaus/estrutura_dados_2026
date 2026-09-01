class CleannerBot:
    def __init__(self, name='',energyLevel=100, isOn=False, color='black',waterCapacity=50, positionX=0, positionY=0, local='',area=0):
        self.name = name
        self.energyLevel = energyLevel
        self.isOn = isOn
        self.color = color
        self.waterCapacity = waterCapacity
        self.positionX = positionX
        self.positionY = positionY
        self.local = local
        self.area = area


    def __str__(self):
        return f'Name: {self.name}\nEnergy Level: {self.energyLevel}\nLigado: {self.isOn}\nPosição X: {self.positionX}\nPosição Y: {self.positionY}'

    def moveX(self, newX):
        self.positionX = newX

    def moveY(self,newY):
        self.positionY

    

samsung = CleannerBot()

xiaomi = CleannerBot('xiaomi', 40, False, 'blue')
print(xiaomi)

xiaomi.moveX(10)


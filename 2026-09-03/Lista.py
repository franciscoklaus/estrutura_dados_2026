class ArrayList:
    def __init__(self) -> None:
        self.LEN = 1
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0

    def insert(self,data: any) -> None:
        if self.isMemoryFull():
            self.increaseMemory()
        self.arrayList[self.insertPosition] = data
        self.insertPosition += 1

    def removeLast(self) -> None:
        if self.isEmpty():
            print("Lista vazia")
            return
        self.insertPosition -= 1
        return self.arrayList[self.insertPosition]
        

    def isEmpty(self) -> bool:
        return self.insertPosition == 0

    def isMemoryFull(self) -> bool:
        return self.insertPosition == len(self.arrayList)

    def increaseMemory(self) -> None:
        newArray = [None] * (self.LEN * 2 )
        self.LEN = len(newArray)
        self.copyElements(newArray, self.arrayList)
        self.arrayList = newArray
        newArray = None

    def copyElements(self, newArray: list, oldArray: list) -> None:
        for position in range(len(oldArray)):
            newArray[position] = oldArray[position]


    def insertAt(self,element : any, position : int) -> None:
        if position < 0 or position > self.insertPosition:
            print("Posição inválida")
            return
        if self.isMemoryFull():
            self.increaseMemory()
        for i in range(self.insertPosition, position, -1):
            self.arrayList[i] = self.arrayList[i-1]
        self.arrayList[position] = element
        self.insertPosition += 1


    def show(self) -> None:
        for position in range(self.insertPosition):
            print(self.arrayList[position])




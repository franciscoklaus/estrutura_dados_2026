class Node:
    def __init__(self,valor, proximo):
        self.info = valor
        self.proximo = proximo
    
class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.proximo
        self.quant -= 1

    def inserir(self,valor):
        if self.quant == 0:
            self.prim = self.ult = Node(valor,None)
        else:
            self.ult.proximo = self.ult = Node(valor,None)
        self.quant += 1

    def ver_primeiro(self):
        if self.prim:
            print(self.prim.info)

    def show(self):
        atual = self.prim
        while atual is not None:
            print(atual.info, end=' -> ')
            atual = atual.proximo
        print()
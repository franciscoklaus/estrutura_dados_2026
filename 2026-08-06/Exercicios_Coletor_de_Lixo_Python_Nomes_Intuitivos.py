"""
Exercícios – Referências de Objetos e Coletor de
Lixo em Python
Determine quantos objetos serão coletados pelo coletor de lixo ao final da execução de
cada trecho de código. Não apresente a resposta durante a resolução.
"""

#Exercício 1

class Book:
    def __init__(self, title):
        self.title = title

Book("1984") 

harryBook = Book("Harry Potter") 

favoriteBook = harryBook 

twilightBook = Book("Twilight") 

harryBook = None 

favoriteBook = None 

print("Fim do programa")
print("Total de objetos coletados: 2 (1984, Harry Potter) - Twilight ainda é referenciado por twilightBook")
#===========================================================

#Exercício 2
class Car:
    def __init__(self, model):
        self.model = model

fuscaCar = Car("Fusca")
opalaCar = Car("Opala")
golCar = Car("Gol")
opalaCar = golCar
fuscaCar = opalaCar
golCar = None

print("Análise do coletor")
print("Total de objetos coletados: 2 (Fusca, Opala) - Gol ainda é referenciado por fuscaCar e opalaCar")
#===========================================================

#Exercício 3

class Animal:
    def __init__(self, name):
        self.name = name

Animal("Leão")

cat = Animal("Gato")

dog = Animal("Cachorro")

pet = dog

cat = pet

dog = None

print("Garbage Collector acionado")
print("Total de objetos coletados: 2 (Leão e Gato) - Cachorro ainda é referenciado por pet e cat")
#===========================================================

#Exercício 4

class Product:
    def __init__(self, name):
        self.name = name
Product("Celular")

notebook = Product("Notebook")

tablet = Product("Tablet")

mainProduct = notebook

monitor = Product("Monitor")

notebook = None

tablet = None

mainProduct = None

monitor = monitor

print("Verifique os objetos coletados")
print("Total de objetos coletados: 3 (Celular, Notebook, Tablet) - Monitor ainda é referenciado por monitor")
#===========================================================

#Exercício 5
class Person:
    def __init__(self, name):
        self.name = name
ana = Person("Ana")

bruno = Person("Bruno")

bestFriend = bruno

carlos = Person("Carlos")

bruno = carlos

carlos = ana

ana = None


print("Total de objetos coletados: 0 - Ana, Bruno, Carlos ainda são referenciados")
print("Encerrando...")
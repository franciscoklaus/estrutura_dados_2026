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

Book("1984") # -> created but not referenced, garbage collected

harryBook = Book("Harry Potter") # -> created and referenced by harryBook

favoriteBook = harryBook # -> favoriteBook references the same object as harryBook

twilightBook = Book("Twilight") # -> created and referenced by twilightBook

harryBook = None # -> reference to none, but favoriteBook still references the object

favoriteBook = None # -> reference to none, twilightBook still references the object

print("Análise do coletor")
print(id(Book("1984")))  # Output: <unique_id>
print(id(harryBook))  # Output: None
print(id(favoriteBook))  # Output: None
print(id(twilightBook))  # Output: <unique_id>

print("Fim do programa")
# total de objetos coletados: 3(1984, harrybook, favoriteBook) - twilightBook is still referenced
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
# total de objetos coletados: 3(Fusca, Opala, Gol) - all references are set to None or overwritten
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
# total de objetos coletados: 4 (Leão, Gato, Cachorro, pet) - all references are set to None or overwritten
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

print("Encerrando...")
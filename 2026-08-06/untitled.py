class Client:
    def __init__(self):
        self.name = ""
        self.age = ""


cliente = Client()
copy = Client()

cliente.name = "Ana"

print(copy.name)  # Output: ""
print(id(Client()))  # Output: <unique_id>

Client()

ze = Client()
ana = Client()
print(id(ze))  # Output: <unique_id>
print(id(ana))  # Output: <unique_id>


ana = ze
print(id(ana))  # Output: <unique_id>

lista = []
lista.append(Client())
lista.append(Client())
lista.append(Client())

print(lista)
print(lista[0].name)  # Output: ""
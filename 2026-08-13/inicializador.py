class Person:

    def __init__(self, nome, idade, genero):
        self.name = nome
        self.age = idade
        self.gender = genero

    
    def introduce(self):
        return f"O meu nome é {self.name}"

    def calculate_birth_year(self):
        current_year = 2026
        birth_year = current_year - self.age
        return birth_year



person1 = Person("João", 30, "Masculino")

print(f"Nome: {person1.name}")
print(person1.introduce())

print(f"Ano de nascimento: {person1.calculate_birth_year()}")

print("--------------------------------------------------------------------")


person2 = Person("Maria", 25, "Feminino")
print(f"Nome: {person2.name}")
print(person2.introduce())
print(f"Ano de nascimento: {person2.calculate_birth_year()}")   




class Vehicle:

    def __init__(self, marca="Toyota", modelo="Corolla", ano=2020):
        self.brand = marca
        self.model = modelo
        self.year = ano
        self.plate = ""

    def get_vehicle_info(self):
        return f"Marca: {self.brand}, Modelo: {self.model}, Ano: {self.year}"

    def set_plate(self, plate):
        self.plate = plate



carro1 = Vehicle("Honda", "Civic", 2022)
print(carro1.get_vehicle_info())
carro1.set_plate("ABC-1234")
print(f"Placa: {carro1.plate}")



class BankAccount:
    def __init__(self, **kargs):
        self.account_number = kargs.get("account_number")
        self.holder_name = kargs.get("holder_name")
        self.balance = kargs.get("balance", 0)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Depósito de {amount} realizado com sucesso. Saldo atual: {self.balance}"
        else:
            return "O valor do depósito deve ser positivo."





from Matematica import soma

soma = soma(1,2,3)
print(soma)


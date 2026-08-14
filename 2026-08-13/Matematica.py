class Matematica:
    def somar(cls, *numeros):
        resultado = 0
        for x in numeros:
            resultado += x

        return resultado 
    
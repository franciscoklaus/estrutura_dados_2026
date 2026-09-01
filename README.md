# estrutura_dados_2026

## Aula 2026-08-06 
### Introdução
* [Material 01](./2026-08-06/untitled.py)
* [Material 02](./2026-08-06/Exercicios_Coletor_de_Lixo_Python_Nomes_Intuitivos.py)

<details>

<summary>Respostas</summary>

* Resposta 1

![alt text](./2026-08-06/image-1.png)

* Resposta 2

![alt text](./2026-08-06/image-2.png)

* Resposta 3

![alt text](./2026-08-06/image-3.png)

* Resposta 4

![alt text](./2026-08-06/image-4.png)

* Resposta 5

![alt text](./2026-08-06/image-5.png)

</details>


## Aula 2026-08-13
<details>

<summary>Classes</summary>

**Classes e Objetos**

* Classes associam dados (atributos) e operações (métodos) em uma só estrutura.
* Um objeto é uma variavel cujo tipo é uma classe, ou seja, um objeto é uma instancia de uma classe.
* Quando declaramos uma classe, estamos criando um novo tipo de dados.
* Da mesma forma que quando criamos uma lista ou uma string, estamos instanciando ou criando uma instancia dessas classes.
* É a mesma coisa fazer lista = [] ou lista = list()
* O método ```__init__``` é chamado construtor e é chamado na criação do objeto.

```python
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv_quarto = Televisao()
tv_sala = Televisao()
tv_quarto.ligada # False
tv_quarto.canal # 2

tv_sala.ligada = True
tv_sala.ligada # True
tv_sala.canal = 5
tv_sala.canal # 5
```

* O parâmetro self significa o objeto televisao em si.
* self.ligada é um valor de self, ou seja, do objeto televisao.
* Sempre que criamos atribuitos do objeto, devemos associá-los a self.
* Caso contrário, se escrevêssemos apenas ligada = False, ligada seria apenas uma variável do método e não um atributo

* [Material 01](./2026-08-13/inicializador.py)
* [Material 02](./2026-08-13/Matematica.py)
* [Cliente.py](./2026-08-13/Cliente.py) | [Conta.py](./2026-08-13/Conta.py) | [ContaTeste.py](./2026-08-13/ContaTeste.py)

</details>

## Aula 2026-08-27
[Material](./2026-08-27/CleannerBot.py)
[Material](./2026-08-27/Elevator.py)


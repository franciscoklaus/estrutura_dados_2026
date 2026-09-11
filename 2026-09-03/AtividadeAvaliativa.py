"""
A atividade consiste em utilizar a estruturas de dados do tipo lista para desenvolver uma
aplicação interativa estilo CLI em que o usuário ira executar comandos. O gerenciamento
da aplicação deve usar uma lista para controlar o comportamento da aplicação proposta.
Após a implementação um video deverá ser gravado explicando como funciona a aplicação
proposta e como a estrutura de dados foi utilizada. O video deverá ser postado no linkedin
e o link do post enviado aqui na tarefa. O código deve estar postado no github e o link
do github deverá constar na postagem.
"""

"""
Sistema de Fila de Atendimento (posto de saúde, banco, correios, etc)

A ideia é trazer a ArrayList de Lista.py para uma situação real: uma fila de
atendimento onde a maioria das pessoas entra no final, mas quem tem
prioridade legal (idoso, gestante, pessoa com deficiência) "fura" a fila e
entra logo depois do último prioritário já presente.

Como a ArrayList é usada:
- entrada comum          -> ArrayList.insert            (insere no final)
- entrada prioritária    -> ArrayList.insertAt           (insere em posição específica)
- chamar próximo da fila -> ArrayList.removeAt(0)        (remove o primeiro, FIFO)
- desistência de alguém  -> ArrayList.removeAt(posicao)  (remove de qualquer posição)
- fila vazia?            -> ArrayList.isEmpty

Além disso, o PRÓPRIO MENU da aplicação é guardado em uma ArrayList de tuplas
(código, descrição, função). É essa lista que controla o comportamento do
programa: o menu impresso e o comando executado vêm dela. Para adicionar uma
nova funcionalidade ao sistema, basta dar um insert() nessa lista de comandos.
"""

from Lista import ArrayList


class Pessoa:
    def __init__(self, nome: str, prioritario: bool = False) -> None:
        self.nome = nome
        self.prioritario = prioritario

    def __str__(self) -> str:
        marcador = " (prioritário)" if self.prioritario else ""
        return f"{self.nome}{marcador}"


class FilaDeAtendimento:
    def __init__(self) -> None:
        self.fila = ArrayList()
        self.totalAtendidos = 0

    def entrar(self, nome: str, prioritario: bool = False) -> None:
        pessoa = Pessoa(nome, prioritario)
        if prioritario:
            posicao = self._posicaoAposUltimoPrioritario()
            self.fila.insertAt(pessoa, posicao)
        else:
            self.fila.insert(pessoa)
        print(f"{pessoa} entrou na fila.")

    def _posicaoAposUltimoPrioritario(self) -> int:
        posicao = 0
        for i in range(self.fila.insertPosition):
            if self.fila.arrayList[i].prioritario:
                posicao = i + 1
        return posicao

    def chamarProximo(self) -> None:
        if self.fila.isEmpty():
            print("Não há ninguém na fila no momento.")
            return
        pessoa = self.fila.arrayList[0]
        self.fila.removeAt(0)
        self.totalAtendidos += 1
        print(f"Chamando: {pessoa}")

    def mostrar(self) -> None:
        if self.fila.isEmpty():
            print("Fila vazia.")
            return
        print("-- Fila de atendimento --")
        for i in range(self.fila.insertPosition):
            print(f"{i + 1}º - {self.fila.arrayList[i]}")

    def desistir(self, posicao: int) -> None:
        indice = posicao - 1
        if indice < 0 or indice >= self.fila.insertPosition:
            print("Posição inválida.")
            return
        pessoa = self.fila.arrayList[indice]
        self.fila.removeAt(indice)
        print(f"{pessoa} desistiu da fila.")


def entrarComum(fila: FilaDeAtendimento) -> None:
    nome = input("Nome: ").strip()
    if nome:
        fila.entrar(nome, prioritario=False)


def entrarPrioritario(fila: FilaDeAtendimento) -> None:
    nome = input("Nome: ").strip()
    if nome:
        fila.entrar(nome, prioritario=True)


def chamarProximo(fila: FilaDeAtendimento) -> None:
    fila.chamarProximo()


def mostrarFila(fila: FilaDeAtendimento) -> None:
    fila.mostrar()


def desistirDaFila(fila: FilaDeAtendimento) -> None:
    fila.mostrar()
    if fila.fila.isEmpty():
        return
    try:
        posicao = int(input("Posição de quem vai desistir: "))
    except ValueError:
        print("Posição inválida.")
        return
    fila.desistir(posicao)


def mostrarResumo(fila: FilaDeAtendimento) -> None:
    print(f"Pessoas atendidas até agora: {fila.totalAtendidos}")
    print(f"Pessoas aguardando: {fila.fila.insertPosition}")


def sair(fila: FilaDeAtendimento) -> None:
    print("Encerrando o sistema de atendimento. Até logo!")


def main() -> None:
    fila = FilaDeAtendimento()

    # A lista de comandos é o que controla o comportamento da aplicação:
    # cada posição guarda (código digitado, descrição, função a executar).
    # Para adicionar um novo comando ao sistema, basta inserir um novo
    # item nessa lista - o menu e o despacho de ações são gerados a partir dela.
    comandos = ArrayList()
    comandos.insert(("1", "Entrar na fila", entrarComum))
    comandos.insert(("2", "Entrar na fila prioritária (idoso, gestante, PCD)", entrarPrioritario))
    comandos.insert(("3", "Chamar próximo da fila", chamarProximo))
    comandos.insert(("4", "Ver fila completa", mostrarFila))
    comandos.insert(("5", "Desistir da fila", desistirDaFila))
    comandos.insert(("6", "Ver resumo do atendimento", mostrarResumo))
    comandos.insert(("0", "Sair", sair))

    while True:
        print("\n=== Sistema de Fila de Atendimento ===")
        for i in range(comandos.insertPosition):
            codigo, descricao, _funcao = comandos.arrayList[i]
            print(f"[{codigo}] {descricao}")

        escolha = input("Escolha uma opção: ").strip()

        comandoEncontrado = None
        for i in range(comandos.insertPosition):
            codigo, descricao, funcao = comandos.arrayList[i]
            if codigo == escolha:
                comandoEncontrado = funcao
                break

        if comandoEncontrado is None:
            print("Opção inválida, tente novamente.")
            continue

        comandoEncontrado(fila)

        if escolha == "0":
            break


if __name__ == "__main__":
    main()

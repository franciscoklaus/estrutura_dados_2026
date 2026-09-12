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

Em vez de uma única fila com "furada" por prioridade, cada tipo de
atendimento tem a sua própria fila (sua própria ArrayList):
    idoso, gestante, PCD e atendimento normal.

Todas essas filas ficam guardadas dentro de uma ArrayList "mestra"
(SistemaDeFilas.filas), na ordem em que devem ser atendidas. É essa lista
que controla o comportamento da aplicação: para chamar o próximo, o
sistema percorre essa lista mestra na ordem em que ela está montada e
atende a primeira fila não vazia que encontrar. Ou seja, a PRIORIDADE de
atendimento é simplesmente a ORDEM dos elementos dentro da lista mestra -
para mudar a política de atendimento (ex: dar prioridade máxima a idosos)
basta reordenar essa lista, sem tocar no resto do código.

Como a ArrayList (Lista.py) é usada:
- cada categoria (idoso, gestante, pcd, normal) tem sua própria fila
  -> ArrayList.insert            (pessoa entra no final da sua fila)
- a lista mestra guarda as 4 filas em ordem de prioridade
  -> ArrayList.insert            (montagem das filas na inicialização)
- chamar próximo                 -> ArrayList.removeAt(0) (remove o primeiro da fila
  escolhida, mantendo o FIFO dentro de cada categoria)
- desistência de alguém          -> ArrayList.removeAt(posicao)
- fila vazia?                    -> ArrayList.isEmpty

Além disso, o PRÓPRIO MENU da aplicação também é guardado em uma ArrayList
de tuplas (código, descrição, função). O menu impresso e o comando
executado vêm dessa lista - para adicionar uma nova funcionalidade ao
sistema, basta um insert() a mais nela.
"""

from Lista import ArrayList


# Ordem de atendimento: a posição de cada categoria aqui é a prioridade dela.
# Mudar a ordem desta lista muda a política de atendimento do sistema inteiro.
CATEGORIAS = [
    ("idoso", "Idosos"),
    ("gestante", "Gestantes"),
    ("pcd", "Pessoas com deficiência (PCD)"),
    ("normal", "Atendimento normal"),
]


class SistemaDeFilas:
    def __init__(self) -> None:
        # Lista mestra: guarda, em ordem de prioridade, uma fila (ArrayList)
        # para cada categoria de atendimento.
        self.filas = ArrayList()
        for chave, nome in CATEGORIAS:
            self.filas.insert((chave, nome, ArrayList()))
        self.totalAtendidos = 0

    def _buscarFila(self, chave: str):
        for i in range(self.filas.insertPosition):
            categoriaChave, nome, fila = self.filas.arrayList[i]
            if categoriaChave == chave:
                return nome, fila
        return None, None

    def entrar(self, chave: str, nomePessoa: str) -> None:
        nomeCategoria, fila = self._buscarFila(chave)
        if fila is None:
            print("Categoria inválida.")
            return
        fila.insert(nomePessoa)
        print(f"{nomePessoa} entrou na fila de {nomeCategoria}.")

    def chamarProximo(self) -> None:
        for i in range(self.filas.insertPosition):
            _chave, nome, fila = self.filas.arrayList[i]
            if not fila.isEmpty():
                pessoa = fila.arrayList[0]
                fila.removeAt(0)
                self.totalAtendidos += 1
                print(f"Chamando: {pessoa} (fila: {nome})")
                return
        print("Todas as filas estão vazias no momento.")

    def mostrarTudo(self) -> None:
        algumaOcupada = False
        for i in range(self.filas.insertPosition):
            _chave, nome, fila = self.filas.arrayList[i]
            if fila.isEmpty():
                continue
            algumaOcupada = True
            print(f"-- {nome} --")
            for j in range(fila.insertPosition):
                print(f"  {j + 1}º - {fila.arrayList[j]}")
        if not algumaOcupada:
            print("Todas as filas estão vazias.")

    def desistir(self, chave: str, posicao: int) -> None:
        nomeCategoria, fila = self._buscarFila(chave)
        if fila is None:
            print("Categoria inválida.")
            return
        indice = posicao - 1
        if indice < 0 or indice >= fila.insertPosition:
            print("Posição inválida.")
            return
        pessoa = fila.arrayList[indice]
        fila.removeAt(indice)
        print(f"{pessoa} desistiu da fila de {nomeCategoria}.")


def _escolherCategoria() -> str:
    print("Categorias:")
    for chave, nome in CATEGORIAS:
        print(f"  {chave} - {nome}")
    return input("Categoria: ").strip().lower()


def entrarNaFila(sistema: SistemaDeFilas) -> None:
    chave = _escolherCategoria()
    nome = input("Nome: ").strip()
    if nome:
        sistema.entrar(chave, nome)


def chamarProximo(sistema: SistemaDeFilas) -> None:
    sistema.chamarProximo()


def mostrarFilas(sistema: SistemaDeFilas) -> None:
    sistema.mostrarTudo()


def desistirDaFila(sistema: SistemaDeFilas) -> None:
    sistema.mostrarTudo()
    chave = _escolherCategoria()
    try:
        posicao = int(input("Posição de quem vai desistir: "))
    except ValueError:
        print("Posição inválida.")
        return
    sistema.desistir(chave, posicao)


def mostrarResumo(sistema: SistemaDeFilas) -> None:
    print(f"Pessoas atendidas até agora: {sistema.totalAtendidos}")
    for i in range(sistema.filas.insertPosition):
        _chave, nome, fila = sistema.filas.arrayList[i]
        print(f"  {nome}: {fila.insertPosition} aguardando")


def sair(sistema: SistemaDeFilas) -> None:
    print("Encerrando o sistema de atendimento. Até logo!")


def main() -> None:
    sistema = SistemaDeFilas()

    # A lista de comandos é o que controla o comportamento da aplicação:
    # cada posição guarda (código digitado, descrição, função a executar).
    # Para adicionar um novo comando ao sistema, basta inserir um novo
    # item nessa lista - o menu e o despacho de ações são gerados a partir dela.
    comandos = ArrayList()
    comandos.insert(("1", "Entrar em uma fila", entrarNaFila))
    comandos.insert(("2", "Chamar próximo (respeitando a ordem de prioridade)", chamarProximo))
    comandos.insert(("3", "Ver todas as filas", mostrarFilas))
    comandos.insert(("4", "Desistir de uma fila", desistirDaFila))
    comandos.insert(("5", "Ver resumo do atendimento", mostrarResumo))
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

        comandoEncontrado(sistema)

        if escolha == "0":
            break


if __name__ == "__main__":
    main()

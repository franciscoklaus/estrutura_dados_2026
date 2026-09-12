# Atividade Avaliativa - Sistema de Fila de Atendimento

Aplicação de terminal (CLI) que simula o sistema de senhas de um local de
atendimento ao público (posto de saúde, banco, correios, etc), usando a
`ArrayList` implementada em [Lista.py](./Lista.py) como estrutura de dados
para gerenciar todo o comportamento da aplicação.

## O problema

Locais de atendimento presencial precisam lidar com duas regras ao mesmo
tempo:

1. Quem chega primeiro é atendido primeiro (ordem de chegada).
2. Certos grupos têm prioridade legal de atendimento: idosos, gestantes e
   pessoas com deficiência (PCD).

A atividade pedia uma aplicação CLI cujo comportamento fosse controlado por
uma lista. A solução foi modelar cada uma dessas regras com listas:

- A **ordem de chegada dentro de um mesmo grupo** é resolvida por uma fila
  (FIFO), implementada com a `ArrayList`.
- A **prioridade entre os grupos** é resolvida pela **posição de cada fila
  dentro de uma lista mestra** - o grupo cuja fila aparece primeiro nessa
  lista é sempre atendido primeiro.

## Como o código foi desenvolvido

### 1. Cada categoria tem sua própria fila

Em vez de uma única fila em que pessoas prioritárias "furam" a fila comum,
o sistema mantém **quatro filas independentes**, uma para cada categoria,
cada uma sendo uma instância separada de `ArrayList`:

```python
CATEGORIAS = [
    ("idoso", "Idosos"),
    ("gestante", "Gestantes"),
    ("pcd", "Pessoas com deficiência (PCD)"),
    ("normal", "Atendimento normal"),
]
```

Dentro de cada fila, a ordem de chegada é garantida pelos próprios métodos
da `ArrayList`:

- `insert` → a pessoa entra sempre no final da fila da sua categoria.
- `removeAt(0)` → ao chamar alguém, remove-se sempre o primeiro da fila
  (comportamento FIFO).

### 2. A lista mestra define a prioridade entre as filas

As quatro filas ficam guardadas, nessa mesma ordem, dentro de outra
`ArrayList` (`SistemaDeFilas.filas`). Chamar o próximo da fila é, na
prática, percorrer essa lista mestra do início ao fim e atender a primeira
fila que não estiver vazia:

```python
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
```

Isso significa que **a prioridade de atendimento é apenas a ordem dos
elementos na lista `CATEGORIAS`**. Para mudar a política de atendimento -
por exemplo, atender PCD antes de idosos - basta reordenar essa lista, sem
alterar nenhuma outra parte do código.

### 3. O próprio menu da aplicação é uma lista

O menu do CLI também é montado a partir de uma `ArrayList`, onde cada
posição guarda uma tupla `(código digitado, descrição, função a executar)`:

```python
comandos = ArrayList()
comandos.insert(("1", "Entrar em uma fila", entrarNaFila))
comandos.insert(("2", "Chamar próximo (respeitando a ordem de prioridade)", chamarProximo))
comandos.insert(("3", "Ver todas as filas", mostrarFilas))
comandos.insert(("4", "Desistir de uma fila", desistirDaFila))
comandos.insert(("5", "Ver resumo do atendimento", mostrarResumo))
comandos.insert(("0", "Sair", sair))
```

O laço principal (`main`) apenas percorre essa lista para imprimir o menu e
para descobrir qual função executar de acordo com a opção digitada. Isso
quer dizer que **é a lista quem controla o comportamento da aplicação**:
adicionar um novo comando ao sistema é só um `insert()` a mais, sem mexer
no laço principal.

## Estrutura do código

| Item                     | Papel                                                              |
|--------------------------|---------------------------------------------------------------------|
| `CATEGORIAS`             | Lista com a ordem de prioridade de atendimento entre as categorias |
| `SistemaDeFilas`         | Guarda a lista mestra de filas e implementa as regras de negócio    |
| `SistemaDeFilas.filas`   | `ArrayList` mestra: uma fila (`ArrayList`) por categoria             |
| `entrarNaFila` etc.      | Funções chamadas pelo menu, cada uma recebendo o `SistemaDeFilas`   |
| `comandos` (em `main`)   | `ArrayList` que define o menu e o despacho de comandos do CLI       |

## Como executar

```bash
cd 2026-09-03
python3 AtividadeAvaliativa.py
```

## Exemplo de uso

```
=== Sistema de Fila de Atendimento ===
[1] Entrar em uma fila
[2] Chamar próximo (respeitando a ordem de prioridade)
[3] Ver todas as filas
[4] Desistir de uma fila
[5] Ver resumo do atendimento
[0] Sair
Escolha uma opção: 1
Categorias:
  idoso - Idosos
  gestante - Gestantes
  pcd - Pessoas com deficiência (PCD)
  normal - Atendimento normal
Categoria: normal
Nome: Carlos
Carlos entrou na fila de Atendimento normal.
```

Cadastrando também um idoso, uma gestante e uma pessoa com deficiência,
mesmo entrando depois do Carlos:

```
Escolha uma opção: 3
-- Idosos --
  1º - Seu Zé
-- Gestantes --
  1º - Maria
-- Pessoas com deficiência (PCD) --
  1º - João
-- Atendimento normal --
  1º - Carlos
```

Ao chamar o próximo (opção 2), quem chegou por último, mas está numa fila
prioritária, é atendido antes de quem chegou primeiro na fila normal:

```
Escolha uma opção: 2
Chamando: Seu Zé (fila: Idosos)

Escolha uma opção: 2
Chamando: Maria (fila: Gestantes)
```

O resumo (opção 5) mostra quantas pessoas já foram atendidas e quantas
ainda aguardam em cada fila:

```
Escolha uma opção: 5
Pessoas atendidas até agora: 2
  Idosos: 0 aguardando
  Gestantes: 0 aguardando
  Pessoas com deficiência (PCD): 1 aguardando
  Atendimento normal: 1 aguardando
```

## Arquivos

- [Lista.py](./Lista.py) - implementação da `ArrayList` (lista dinâmica
  baseada em array) usada como base de todo o sistema.
- [ListaTeste.py](./ListaTeste.py) - testes simples de uso da `ArrayList`.
- [AtividadeAvaliativa.py](./AtividadeAvaliativa.py) - a aplicação CLI do
  sistema de fila de atendimento.

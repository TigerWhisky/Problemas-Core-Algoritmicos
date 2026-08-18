**# Problemas Core Algorítmicos

Repositório de exercícios e implementações focadas em **lógica algorítmica pura**, estruturas de controlo de fluxo e manipulação básica de memória.

Este projeto foi desenvolvido no âmbito do curso de Engenharia Informática com o objetivo de consolidar os fundamentos da programação e do pensamento algorítmico.

## Objetivos

- Dominar estruturas de controlo de fluxo (`if`, `for`, `while`, `break`, `continue`)
- Compreender e aplicar **recursão**
- Implementar algoritmos clássicos de **pesquisa** e **ordenação**
- Analisar complexidade temporal e espacial
- Entender conceitos básicos de manipulação de memória (referências, mutabilidade, etc.)

## Estrutura

| Pasta                    | Conteúdo                                      |
|--------------------------|-----------------------------------------------|
| `docs/`                  | Explicações teóricas                          |
| `problemas/01_basicos`   | Problemas fundamentais                        |
| `problemas/02_pesquisa`  | Algoritmos de pesquisa                        |
| `problemas/03_ordenacao` | Algoritmos de ordenação                       |
| `problemas/04_recursao`  | Problemas recursivos                          |
| `problemas/05_memoria`   | Exemplos de manipulação de memória            |
| `tests/`                 | Testes unitários                              |

## Como executar

```bash
# Exemplos
python problemas/01_basicos/fatorial.py
python problemas/03_ordenacao/bubble_sort.py

# Correr testes
pip install pytest
pytest**

Conceitos Abordados

Controlo de fluxo
Recursão e casos base
Pesquisa linear e binária
Ordenação (Bubble, Selection, Insertion, Merge)
Complexidade Big-O
Mutabilidade e referências em Python

## Testes

O repositório inclui testes unitários automatizados com `pytest`.

### Instalação

```bash
pip install -r requirements.txt

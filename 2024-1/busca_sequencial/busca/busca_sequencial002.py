"""
Programa busca_sequencial.py
descrição: Este programa busca um valor em uma base de dados.
Autor: Vitor de Almeida Netto
Data: 27/05/2024
Versão: 0.0.2
correço~es realizadas: informação mais intuitiva ao usuário da posição em que o seu cpf foi encontrado.
"""
## Alocação de memoria

lista = []
achou = False
posicao = 0
cpf = 0

# Base de dados

base = [ 1, 5, 2, 87, 31]
lista = base
# leitura de dados

cpf = int(input("Digite o valor a procurar:"))


# processamento de dados

while posicao < len(lista):
    if lista [posicao] == cpf:
        achou = True
        break
    posicao += 1


# saída de dados

if achou:
    print(f"\nO valor {cpf} foi achado na posição {posicao + 1}.")
else:
    print(f"\nO valor {cpf} não foi achado.")
    


"""
Programa busca_sequencial.py
descrição: Este programa busca um valor em uma base de dados.
Autor: Vitor de Almeida Netto
Data: 27/05/2024
Versão: 0.0.3
correço~es realizadas: 1.informação mais intuitiva ao usuário da posição em que o seu cpf foi encontrado.
2. Informação mais precisa de que o valor procurado é um cpf.
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

cpf = int(input("Digite o CPF a procurar:"))


# processamento de dados

while posicao < len(lista):
    if lista [posicao] == cpf:
        achou = True
        break
    posicao += 1


# saída de dados

if achou:
    print(f"\nO CPF {cpf} foi achado na posição {posicao + 1}.")
else:
    print(f"\nO CPF {cpf} não foi achado.")
    


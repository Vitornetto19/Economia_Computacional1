""" 
Programa Medidor de temperatura
Descrição: Este prgrama pergunta a temperatura do local ao usuário e retorna na tela se está frio(sendo isso até 18 graus Celsius), se está Agradável(sendo isso entre 19 e 28 graus Celsius) e se está Quente(sendo isso qualquer temperatura acima de 28 graus celsius).
Autor: Vitor de Almeida Netto
Data: 26/05/2024
Versão: 0.0.1
"""
# Alocação de memória
Temperatura: int = 0


# Entrada de dados

Temperatura = int(input("qual é a temperatura, em Celsius, do ambiente?"))


# Processamento de dados

if Temperatura <= 18:
    print("Esta Frio")
elif Temperatura > 18 and Temperatura <= 28:
    print("Esta agradável")
else:
    print("Esta quente")
    
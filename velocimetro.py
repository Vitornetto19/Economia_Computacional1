"""
Programa Velocímetro
Descrição: Este programa recebe a velocidadde que o usuário coloca em um numero inteiro de km/h e o tranforma com a sigla KM/h. caso a velocidade colocada pelo usuário ultrapasse os 80KM/h o programa avisa que o usuário esta multado e calcula o valor respeitando o critério de R$5 por KM/h excedido.Logo após exibe a multa e os km/h excedidos.
Autor: Vitpr de Almeida Netto
Data: 24/05/2024
Versão: 0.0.1
"""
#Alocação de memoria
velocidade: int = 0
multa: int = 0

#Entrada de dados
velocidade = int(input("qual é a velocidade do veículo em km/h"))

#Processamento e saída de dados
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você exedeu a velocidade da pista em: {velocidade - 80}Km/h\nVocê esta multado em {multa}R$")
else:
    print(f"Sua velocidade é {velocidade}KM/h") 
    

    

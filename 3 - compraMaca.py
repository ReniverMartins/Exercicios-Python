'''As maçãs custam:
    R$ 1,30 cada se forem compradas menos de uma dúzia
    R$ 1,00 se forem compradas pelo menos 12. 

Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.'''

preco = 0
qtdMaca = int(input()) #Leitura quantidade de Maças

if(qtdMaca >= 12):
    preco = 1.00
else:
    preco = 1.30

valorPgmto = qtdMaca * preco
print(valorPgmto)
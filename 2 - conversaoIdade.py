'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.'''

ageYear =   int(input()) #Leitura Year
ageMonth =  int(input()) #Leitura Month
ageDay =    int(input()) #Leitura Day

ageFinaly = (ageYear*365)+(ageMonth*30)+(ageDay)

print(ageFinaly)
'''Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos:
    < brancos > 
    <  nulos  >
    < válidos >
Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.'''


while (True):
    totalEleitores  =    int(input()) #Leitura total de eleitores
    votosBrancos    =    int(input()) #Leitura total de votos Brancos
    votosNulos      =    int(input()) #Leitura total de votos nulos
    votosValidos    =    int(input()) #Leitura total de votos validos
    if((votosBrancos+votosNulos+votosValidos)<=totalEleitores):
        percBrancos =   (votosBrancos/totalEleitores)*100
        percNulos   =   (votosNulos/totalEleitores)*100
        percValidos =   (votosValidos/totalEleitores)*100

        print(percBrancos,"%")
        print(percNulos,  "%")
        print(percValidos,"%")

    else:
        print("Ocorreu um erro, volume de votos maior que o total de eleitores!!!")
       

#Necessario refatoração, para incluir o loop de re-inserção de dados em caso de erro.
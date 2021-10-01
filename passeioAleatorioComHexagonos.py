import random

def passeioAleatorio(n):
    x, y = 0, 0
    for i in range(n):
# no exagono temos 2 opções, em um ponto ele pode ir para cima, baixo e direita e tambem tem a opção para ir para cima baixo e esquerda, entao
        if i % 2 == 0: # quando o mod do i for igual a 0
            (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0)]) # ele tem a opção de ir para cima, baixo e direita
        else: 
            (dx, dy) = random.choice([(0, 1), (0, -1), (-1, 0)]) # ele tem a opção de ir para cima, baixo e esquerda

        x += dx
        y += dy     

    return (x,y)

numberOfWalks = 10000 # numero de caminhadas

for walk_lenght in range(1, 31): # caminhada de 1 ate 30 quarteiroes
    noTransport = 0
    for i in range(numberOfWalks):
        (x, y) = passeioAleatorio(walk_lenght)
        distance = abs(x) + abs(y) # calculamos a distancia absoluta (sem valores negativos)
        if distance <= 4: # se a distancia de casa for menor que 5, nao necessita de transporte
            noTransport += 1 # adicionamos 1
    noTransportPercentage = float(noTransport)/numberOfWalks # pegamos a %
    print("tamanho do caminho = ", walk_lenght, "/ % of no transport = ", noTransportPercentage*100)    

print("Distancia:", distance) # retornamos a distancia absoluta
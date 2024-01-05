from dealer import Dealer
from jogador import Jogador
import random


identificacao = int(input("Informe a identificação do Dealer: "))
dealer = Dealer(identificacao)

quantidade = int(input("Insira a quantidade de jogadores: "))

jogadores = []
jogadoresParar = []

for i in range(quantidade):
    nome = input("\nInforme o nome do jogador: ")
    idade = int(input("Informe a idade do jogador: "))
    jogador = Jogador(nome, idade)
    jogadores.append(jogador)


for jogador in jogadores:
    dealer.cartas_iniciais(jogador)

while True:
    
    for i in range(quantidade):
        total = sum(jogadores[i].cartas_maos)

        if jogadores[i].jogou == True:
            continue
            
        print(f"\nCartas sorteadas na primeira rodada para {jogadores[i].nome}: {jogadores[i].cartas_maos}"
                f"\nA soma das cartas do {jogadores[i].nome}: {total}")

        deseja = int(input(f"\nJogador {jogadores[i].nome} deseja: \n1 - Continuar \n2 - Parar\n"))

        if deseja == 1:
            dealer.comprar_cartas(jogadores[i])
            total = sum(jogadores[i].cartas_maos)

            print(f"\nCartas na mão do jogador {jogadores[i].nome}: {jogadores[i].cartas_maos}")
            print(f"\nA soma de suas cartas é {jogadores[i].nome}: {total}")
            #print(jogadoresParar)

        elif (deseja == 2):
            total = sum(jogadores[i].cartas_maos)

            print(f"\nA soma de suas cartas é {total}")
            #jogadoresParar.append(jogadores[i])
            jogadores[i].parar()

        if sum(jogadores[i].cartas_maos) > 21:
            print("Você perdeu!")
            jogadores[i].parar()

        # if (jogadoresParar.__len__ == quantidade):
        #     max(total)
        #     print(max(total))

        elif sum(jogadores[i].cartas_maos) == 21:
            print("Você venceu!")
            exit()

        if dealer.todos_pararam(jogadores) == True:
            print(f"Vencedor: {dealer.vencedor(jogadores)}")
            exit()
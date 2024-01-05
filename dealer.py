import random
from jogador import Jogador

class Dealer(Jogador):
    def __init__(self, id: str):
        self.id = id
        self.cartas_baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def cartas_iniciais(self, jogador):
        cartas = []

        sorteio = random.sample(self.cartas_baralho, 2)  # Sorteia 2 elementos da lista

        for carta_sorteada in sorteio:
            cartas.append(carta_sorteada)
            self.cartas_baralho.remove(carta_sorteada)
        jogador.setCartas_maos(cartas)

    def comprar_cartas(self, jogador):
        sorteio = random.sample(self.cartas_baralho, 1)
        carta_sorteada = sorteio[0]
        jogador.cartas_maos.append(carta_sorteada)
        self.cartas_baralho.remove(carta_sorteada)

    def vencedor(self, jogadores):
        vencedor = None
        maior_pontuacao = -1

        for jogador in jogadores:
            pontos = sum(jogador.cartas_maos)
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                vencedor = jogador.nome
        return vencedor
    
    def todos_pararam(self, jogadores):
        for jogador in jogadores:
            if jogador.jogou == False:
                return False
        return True

class Jogador:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.pontos = 0
        self.cartas_maos = []
        self.jogou = False

    def setCartas_maos(self, cartas):
        self.cartas_maos = cartas
    
    def parar(self):
        self.jogou = True

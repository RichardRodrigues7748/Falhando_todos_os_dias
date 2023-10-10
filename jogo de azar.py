class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.jogos = []

    def add_game(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id == id:
                self.jogos.remove(jogo)
                return f"Jogo com ID {id} removido da plataforma."
        return f"Jogo com ID {id} não encontrado na plataforma."

    def listar_jogos(self):
        if not self.jogos:
            return "Nenhum jogo na plataforma."
        else:
            return "\n".join([str(jogo) for jogo in self.jogos])

    def __str__(self):
        return f"Total de jogos na plataforma: {len(self.jogos)}"

plataforma = Plataforma()
jogo1 = Jogo("Blackjack", "Cartas", 10.0, 1)
jogo2 = Jogo("Caça-Níqueis", "Slots", 5.0, 2)
jogo3 = Jogo("Jackpot Casino", "Cartas", 15.0, 3)
plataforma.add_game(jogo1)
plataforma.add_game(jogo2)
plataforma.add_game(jogo3)

print(plataforma.listar_jogos())
print(plataforma.remover_jogo(2))
print(plataforma)

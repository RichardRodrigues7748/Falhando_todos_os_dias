class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nota_nova):
        self.nota = nota_nova

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, id):
        for estudante in self.estudantes:
            if estudante.id == id:
                self.estudantes.remove(estudante)
                return f"Estudante com ID {id} removido da turma."
        return f"Estudante com ID {id} não encontrado na turma."

    def media_da_turma(self):
        if not self.estudantes:
            return 0.0
        else:
            soma_notas = sum([estudante.nota for estudante in self.estudantes])
            return soma_notas / len(self.estudantes)

    def melhor_estudante(self):
        if not self.estudantes:
            return "Nenhum estudante na turma."
        else:
            melhor = max(self.estudantes, key=lambda estudante: estudante.nota)
            return f"Best estudante: {melhor.nome}, Nota: {melhor.nota}"

turma = Turma()
estudante1 = Estudante("Romes", 39, 10.0, 1)
estudante2 = Estudante("Vitinho", 18, 7.7, 2)
estudante3 = Estudante("Flavio", 17, 5.9, 3)
estudante4 = Estudante("Sebastiao", 48, 2.4, 4)
turma.adicionar_estudante(estudante1)
turma.adicionar_estudante(estudante2)
turma.adicionar_estudante(estudante3)
turma.adicionar_estudante(estudante4)

print(turma.melhor_estudante())
print("A média da turma é:", turma.media_da_turma())
print(turma.remover_estudante(1))
print(estudante4.informacoes())

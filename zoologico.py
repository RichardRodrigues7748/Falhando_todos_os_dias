class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return f"{self.nome} é um {self.especie} de {self.idade} anos que é {self.dieta}. Habitat: {self.habitat}"

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                return f"{nome} foi retirado do zoológico."
        return f"{nome} não foi encontrado no zoológico."

    def listar_animais(self):
        if not self.animais:
            return "O zoológico está vazio."
        else:
            return "\n".join([animal.descricao() for animal in self.animais])

    def buscar_por_especie(self, especie):
        animais_especie = [animal for animal in self.animais if animal.especie == especie]
        if animais_especie:
            return "\n".join([animal.descricao() for animal in animais_especie])
        else:
            return f"Não há animais da espécie {especie} no zoológico."

    def listar_animais_por_habitat(self, habitat):
        animais_habitat = [animal for animal in self.animais if animal.habitat == habitat]
        if animais_habitat:
            return "\n".join([animal.descricao() for animal in animais_habitat])
        else:
            return f"Não há animais no habitat {habitat} no zoológico."

zoo = Zoologico()
animal1 = Animal("LUAN", "Leão", 5, "Carnívoro", "Savana")
animal2 = Animal("RICHARD", "Pinguim", 3, "Piscívoro", "Polo Sul")
animal3 = Animal("DANIEL", "Cobra", 2, "Carnívoro", "Floresta Tropical")
zoo.adicionar_animal(animal1)
zoo.adicionar_animal(animal2)
zoo.adicionar_animal(animal3)

print(zoo.listar_animais())
print(zoo.buscar_por_especie("Pinguim"))
print(zoo.listar_animais_por_habitat("Floresta Tropical"))
print(zoo.remover_animal("LUAN"))

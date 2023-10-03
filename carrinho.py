class Carrinho:
    def __init__(self, marca, modelo, ano, preco, vendido):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = vendido
    
    def exibir_info(self):
        return f'marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, preco: {self.preco}, vendido: {self.vendido}'
    
veiculoA = Carrinho('Audi', 'Audi A5', 2002, 400000, False)
veiculoB = Carrinho('BMW', '320I', 2022, 500000, False)
veiculoC = Carrinho('Fiat', 'uno', 2003, 10000, True)

if veiculoA.vendido:
    print("Veículo 1 está vendido")
else:
    print("Veículo 1 não está vendido")
if veiculoB.vendido:
    print("Veículo 2 está vendido")
else:
    print("Veículo 2 não está vendido")
if veiculoC.vendido:
    print("Veículo 3 está vendido")
else:
    print("Veículo 3 não está vendido")

print(veiculoA.exibir_info())
print(veiculoB.exibir_info())
print(veiculoC.exibir_info())


   
        

    

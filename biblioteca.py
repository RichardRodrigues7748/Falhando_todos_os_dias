class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def add_book1(self, livro):
        self.livros[livro.titulo] = livro

    def register_member(self, membro):
        self.membros[membro.nome] = membro

    def lend_book(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "disponível":
                livro.status = "emprestado"
                self.membros[nome_membro].livros_emprestados.append(livro)
                return f"O livro '{titulo_livro}' foi emprestado para {nome_membro}."
            else:
                return "O livro não está disponível no momento."
        else:
            return "Livro ou membro não encontrado."

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            membro = self.membros[nome_membro]
            if livro.status == "emprestado" and livro in membro.livros_emprestados:
                livro.status = "disponível"
                membro.livros_emprestados.remove(livro)
                return f"O livro '{titulo_livro}' foi devolvido por {nome_membro}."
            else:
                return "Este livro não foi emprestado para este membro."
        else:
            return "Livro ou membro não encontrado."

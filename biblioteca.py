class Biblioteca:
    def __init__(self):
        self.livros = []
    def AdicionarLivro(self,livro):
        self.livros.append(livro)
        for i in self.livros:
            print(i)
    def BuscarLivro(self,titulo):
        for lupa in self.livros:
            if lupa.titulo == titulo:
                return lupa
    def ConsultarDetalhes(self,titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            return livro
        else:
            print("Livro não encontrado")
    def EmprestarLivro(self,titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            if livro.status == False:
                print("Livro disponível para empréstimo")
                livro.status = True
                print("Livro emprestado com sucesso")
            else:
                print("Livro já emprestado.")
        else:
            print("Livro não encontrado.")
    def MostrarLivros(self):
        for i in self.livros:
                print ('-----'*10)
                print(i)
                print ('-----'*10)
    def DevolverLivro(self,titulo):
        livro = self.BuscarLivro(titulo)
        if livro:
            if livro.status == True:
                print("Livro devolvido com sucesso")
                livro.status == False
            else:
                print("Este livro já foi devolvido")
        else:
            print("Livro não encontrado")
class Livro():
    def __init__(self,nome,autor,editora,pag) :
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.pag = pag
    def alterar_editora(self):
        self.editora = (input("Altere a editora do livro: "))
        print ("Editora alterada com sucesso!")
    def mostrar_detalhes(self):
        print(f'Nome do livro: {self.nome}')
        print(f'Nome do(a) autor(a): {self.autor}')
        print(f'Nome da editora: {self.editora}')
        print(f'Quantidade de páginas: {self.pag}')

livro1 = Livro("Orgulho e preconceito","Jane Austen","Editora Moderna",240)
livro1.alterar_editora()
livro1.mostrar_detalhes()
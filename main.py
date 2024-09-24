from biblioteca import Biblioteca
from Livros import Livro
def ExibirMenu():
    print("-----MENU-----")
    print("1 - Adicionar livro")
    print("2 - Consultar detalhes do Livro")
    print("3 - Emprestar um livro")
    print("4 - Listar todos os livros da biblioteca")
    print("5 - Devolver livro")
    print("6 - Sair")
    print("-"*15)
biblioteca = Biblioteca()
while True:
    ExibirMenu()
    op = int(input("Digite a opção: "))
    if op ==1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        paginas = int(input("Digite a quantidade de páginas: "))
        livro = Livro(titulo,autor,paginas)
        biblioteca.AdicionarLivro(livro)
    elif op ==2:
        titulo = input("Digite o título que deseja procurar: ")
        detalhes = biblioteca.ConsultarDetalhes(titulo)
        print(detalhes)
    elif op == 3:
        titulo = input("Digite o título do livro que deseja buscar: ")
        biblioteca.EmprestarLivro(titulo)
    elif op == 4:
        biblioteca.MostrarLivros()
    elif op == 5:
        titulo = input("Digite o título do livro que deseja buscar: ")
        biblioteca.DevolverLivro(titulo)
    elif op == 6:
        print("Obrigado por usar o nosso sistema!")
        break
    else:
        print("Opção não encontrada, tente novamente")
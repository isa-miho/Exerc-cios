notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
notaTres = float(input("Digite a terceira nota: "))
media = (notaUm + notaDois + notaTres)/3
if media>= 7:
    print ("Aprovado")
if media<7:
    print("Reprovado")
if media == 10:
    print("Aprovado com Distinção")
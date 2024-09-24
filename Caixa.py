valor = int(input("Digite o valor do saque (entre 10 e 600): "))
if 10 <= valor <= 600:
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = {nota: 0 for nota in notas}
    for nota in notas:
        if valor >= nota:
            quantidade_notas[nota] = valor // nota
            valor %= nota
    for nota, quantidade in quantidade_notas.items():
        if quantidade > 0:
            print(f'{quantidade} nota(s) de {nota} reais')
else:
    print("Valor inválido. Por favor, digite um valor entre 10 e 600.")
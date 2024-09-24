numero = int(input("Digite um numero menor que 1000: "))
if numero > 1000:
    print("Número inválido, por favor coloque um número menor que 1000")
else:
    centenas = numero // 100
    dezenas = (numero - centenas * 100) // 10
    unidades = numero - centenas * 100 - dezenas * 10
    if centenas > 0:
        print(f'{centenas} centenas, {dezenas} dezenas e {unidades} unidades')
    elif dezenas > 0:
        print(f'{dezenas} dezenas e {unidades} unidades')
    else:
        print(f'{unidades} unidades')
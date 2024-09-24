numeros = [1,56,7,45,8,10,35,22,5,20,45]
par = []
impar = []
partotal = 0
imparTotal = 0 
for i in numeros:
    if i % 2 == 0:
        partotal += i
        par.append(i)
    else:
        imparTotal += i
        impar.append(i)

print(f'Números impares: {impar}\nSoma dos números impares: {imparTotal}\nNúmeros pares: {par}\nSoma dos números pares: {partotal}')
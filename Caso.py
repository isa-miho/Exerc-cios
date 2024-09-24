print("Por favor responda apenas com sim ou não")
telefone = input("Telefonou para vítima?: ")
local = input("Esteve no local do crime?: ")
mora = input("Mora perto da vítima?: ")
deve = input("Devia para vítima?: ")
job = input("Já trabalhou com a vítima?: ")

telefone = 1 if telefone.lower() == "sim" else 0
local = 1 if local.lower() == "sim" else 0
mora = 1 if mora.lower() == "sim" else 0
deve = 1 if deve.lower() == "sim" else 0
job = 1 if job.lower() == "sim" else 0

provas = telefone + local + mora + deve + job 

if provas <= 1:
    print("Inocente")
elif provas < 3:
    print("Suspeito")
elif provas <= 4:
    print("Cúmplice")
elif provas == 5:
    print("Assassino")
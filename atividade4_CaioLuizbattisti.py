#Escreva um programa para pedir um número e em seguida o nome.
#Exiba o nome (uma letra de cada vez em cada linha)
#e repita isso para o número de vezes que ele digitou.
nome =input("digite seu nome: ")
num = int(input("digite um numero: "))
for _ in range(num):
    for letra in nome:
        print(letra)
        print("----")
        print("CaioLuizBattisti")
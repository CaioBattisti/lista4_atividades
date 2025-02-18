#faça um programa que solicite ao usuário para digitar o seu nome e um numero qualquer 
#e em seguida exiba seu nome varias vezes de acordo com o número que ele digitou
nome =input("digite seu nome: ")
num = int(input("digite um numero: "))
for _ in range(num):
    print(nome)
#Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]).
#Se ele selecionar para cima, peça o número superior e conte de 1 até esse número.
#Se ele selecionar para baixo, peça-lhe para inserir um número abaixo de 20 e, em seguida, faça uma contagem regressiva de 20 até esse número.
#Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".
Direcao =input("Qual direção deseja seguir? Cima ou Baixo? ").strip().lower()
if Direcao == "c":
     num1 =int(input("digite um numero maior que 1: "))
for numeros in enumerate (num1):
    print(num1)
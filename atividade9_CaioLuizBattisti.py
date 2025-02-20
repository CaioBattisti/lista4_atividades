#Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]).
#Se ele selecionar para cima, peça o número superior e conte de 1 até esse número.
#Se ele selecionar para baixo, peça-lhe para inserir um número abaixo de 20 e, em seguida, faça uma contagem regressiva de 20 até esse número.
#Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".
Direcao =input("Qual direção deseja seguir? Cima ou Baixo? ").strip().lower()
if Direcao == "c":
     num1 =int(input("digite um numero maior que 1: "))
     if num1 > 1:
          for i in range(1,num1 + 1):
               print(i)
               print("CaioLuiBatisti")
     else:
          print("Numero invalido!")
          print("CaioLuiBatisti")
elif Direcao == "b":
     num1=int(input("digite um numero maior que 20: "))
     if num1 < 20:
          for i in range(20,num1 -1, -1):
               print(i)
               print("CaioLuiBatisti")
     else:
          print("numero invalido!")
          print("CaioLuiBatisti")
else:
     print("Direção invalida!")
     print("CaioLuiBatisti")
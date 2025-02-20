#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
pessoas =int(input("Quantas pessoas deseja convidar? "))
if pessoas < 10:
    nomes =[]
    for i in range(pessoas):
        nome = input(f"digite o nome da {i+1}° pessoa: ")
        nomes.append(nome)
    print("\nlista de convidados: ")
    print("CaioLuiBatisti")
    for nome in nomes:
        print(nome)
else:
    print("muitas pessoas para convidar!")
    print("CaioLuiBatisti")
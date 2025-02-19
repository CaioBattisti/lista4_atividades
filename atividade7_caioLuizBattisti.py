#Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10, exiba o nome dele esse número de vezes;
#caso contrário, exiba a mensagem “Numero muito alto" três vezes.
nome =input("digite seu nome: ")
num1 =int(input("digite um numero menor que 10: "))
if num1 < 10:
    for _ in range(num1):
        print(nome)
else:
      for _ in range(3):
        print("Numero muito Alto!")
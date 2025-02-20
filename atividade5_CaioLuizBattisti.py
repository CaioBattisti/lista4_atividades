#Peça ao usuário para inserir um número que deseja a tabuada e, em seguida, exibir a tabuada para esse número.
num1 =int(input("digite um numero: "))
print(f"A tabuada do {num1}: ")
for i in range(1, 11):
    print(f"{num1} x {i} = {num1*i}")
    print("CaioLuiBatisti")
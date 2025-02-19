#Peça um número abaixo de 50 e, em seguida, faça uma contagem regressiva de 50 até esse número,
#certificando-se de mostrar o número que eles inseriram na saída.
num1 =int(input("Digite um numero abaixo de 50: "))
if num1 < 50:
    for i in range(50, num1 -1,-1):
        print(i)
else:
    print("numero invalido! Deve ser menor que 50!")
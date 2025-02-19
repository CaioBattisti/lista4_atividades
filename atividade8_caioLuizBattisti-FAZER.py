#Defina uma variável chamada total como 0 (Zero). Peça ao usuário para inserir cinco números e
#após cada entrada,pergunte se ele deseja que esse número seja incluído (S ou s, N ou n).
#Se ele desejar, adicione o número ao total. Se ele não quiser incluí-lo, não o adicione ao total.
#Depois de inserir todos os cinco números, exiba o total.
total = 0
for _ in range(5):
    num1 =int(input("Digite um numero: "))
    incluir=input("Deseja inclur esse numero na soma?(S/N): ").strip().lower()
if incluir == "S":
    total += num1
if incluir == "N":
    print("o total é:{total}")
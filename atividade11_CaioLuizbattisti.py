#Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
#Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
#O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
#No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
#Desenvolva um programa em Python que:
#1.Solicite ao usuário o número de tarefas a serem inseridas.
#2.Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
#3.Conte e exiba o número de tarefas concluídas e não concluídas.
num_tarefas =int(input("Quantas tarefas devem ser inseridas? "))
tarefas_concluidas = 0
for i in range(num_tarefas):
    nome_tarefa=input(f"Digite o nome da tarefa:{i+1} ")
    estatus =input(f"a tarefa'{nome_tarefa}'esta cocluida? (S/N): ").strip().lower()
    if estatus in ("s"):
        tarefas_concluidas += 1
        tarefas_pendentes = num_tarefas - tarefas_concluidas
    print("\nresumo das tarefas: ")
    print(f"total de tarefas:{num_tarefas}")
    print(f"total de tarefas concluidas:{tarefas_concluidas}")
    print(f"total de tarefas pendentes:{tarefas_pendentes}")
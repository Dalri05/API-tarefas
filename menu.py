import webbrowser
import requests
from os import system
from time import sleep


def escrever():
    system("cls")
    print("Digite 'menu' para voltar para o menu")
    tarefa = input("Digite uma nova tarefa: ")
    if tarefa == "menu": 
        system("cls")
        return  
    else:
        with open("tarefas.txt", "a") as arquivo: 
            arquivo.write(tarefa + "\n")
        print("Tarefa foi escrita no arquivo 'tarefas.txt'")
        sleep(1)
        escrever()  

def excluir_todas():
    system("cls")
    with open("tarefas.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("Sem nenhuma tarefa! Retornando ao menu...")
        sleep(3)
        system("cls")
        return

    print("Tem certeza que deseja excluir suas tarefas?")
    ctz = input("Digite 'sim' ou 'nao': ")
    if ctz == "sim":
        with open("tarefas.txt", "w") as arquivo:
            print("As tarefas foram excluídas com sucesso!")
            sleep(3)
            system("cls")  
            return
    elif ctz == "nao":
        print("Retornando ao menu!")
        sleep(1)
        system("cls")
    else:
        print("Opção incorreta...")
        sleep(1)
        system("cls")
        excluir_todas()

def concluida():
    system("cls")
    with open("tarefas.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("Sem tarefas escritas... retornando ao menu!")
        sleep(3)
        system("cls")
        return

    for i, linha in enumerate(linhas, 1):
        print(f"{i}. {linha.strip()}")

    numero_tarefa = input("Digite o número da tarefa que deseja excluir ou 'menu' para retornar ao menu: ")

    if numero_tarefa.isdigit():
        numero_tarefa = int(numero_tarefa)
        if 1 <= numero_tarefa <= len(linhas):
            del linhas[numero_tarefa - 1]
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(linhas)
            print("Tarefa concluída com sucesso!")
            input("Pressione ENTER para continuar...")
            concluida()
        else:
            print("Número de tarefa inválido.")
            input("Pressione ENTER para continuar...")
            concluida()
    elif numero_tarefa.lower() == "menu":
        system("cls")
        return
    else:
        print("Entrada inválida. Tente novamente.")
        input("Pressione ENTER para continuar...")
        concluida()

def mostrar_tarefas():
    system("cls")
    with open("tarefas.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("Sem nenhuma tarefa! Retornando ao menu...")
        sleep(2)
        system("cls")
        return

    for i, linha in enumerate(linhas, 1):
        print(f"{i}. {linha.strip()}")
    
    pg = int(input("aperte 1 para voltar ao menu:"))
    if pg == 1:
        system("cls")
        menu()
    else:
        system("opção incorreta!")
        mostrar_tarefas()

def saveapi():
    with open("tarefas.txt", "r") as arquivo:
        conteudo = arquivo.read()

    conteudo = "\n".join(conteudo.splitlines())

    url = 'http://localhost:5000/'
    data = {'conteudo': conteudo}

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Dados salvos na nuvem com sucesso!")
        else:
            print("Erro ao salvar dados na API.")
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

def menu():
    
    while True:
        
        print('''
        [1] - Escrever nova tarefa
        [2] - Marcar uma tarefa como concluída
        [3] - Excluir todas as tarefas
        [4] - mostrar tarefas escritas
        [5] - sair
        
        OBS: todos os dados são salvados automaticamente na API
        ''')

        op = input("Digite a opção desejada: ")

        if op == "1":
            escrever()
        elif op == "2":
            concluida()
        elif op == "3":
            excluir_todas()
        elif op == "4":
            mostrar_tarefas()
        elif op == "5":
            print("Saindo do programa...")
            break
        else:
            system("cls")
            print("Opção inválida. Por favor, escolha uma opção válida.")
            menu()
menu()
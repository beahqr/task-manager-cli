import json
import os


class TaskManager:
    def __init__(self):
        self.arquivo = "tasks.json"
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        if not os.path.exists(self.arquivo):
            return []

        with open(self.arquivo, "r") as f:
            return json.load(f)

    def salvar_tarefas(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.tarefas, f, indent=4)

    def adicionar(self):
        titulo = input("Digite o nome da tarefa: ")
        tarefa = {"titulo": titulo, "concluida": False}
        self.tarefas.append(tarefa)
        self.salvar_tarefas()
        print("Tarefa adicionada!")

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return

        for i, tarefa in enumerate(self.tarefas):
            status = "✓" if tarefa["concluida"] else "✗"
            print(f"{i+1}. [{status}] {tarefa['titulo']}")

    def concluir(self):
        self.listar()
        try:
            numero = int(input("Número da tarefa: "))
            if 0 < numero <= len(self.tarefas):
                self.tarefas[numero - 1]["concluida"] = True
                self.salvar_tarefas()
                print("Tarefa concluída!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

    def menu(self):
        while True:
            print("\n1 - Adicionar")
            print("2 - Listar")
            print("3 - Concluir")
            print("4 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.adicionar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.concluir()
            elif opcao == "4":
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    app = TaskManager()
    app.menu()
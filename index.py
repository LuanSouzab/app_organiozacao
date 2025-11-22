from datetime import datetime

tarefas = [] 

def mostrar_menu():
    print("\n--- Menu ---") 
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Gerar relatório")
    print("5. Sair")

def adicionar_tarefa():
    try:
        titulo = input("Título da tarefa: ").strip()
        descricao = input("Descrição: ").strip()
        prioridade = int(input("Prioridade (1-5): "))
        prazo_str = input("Prazo (dd/mm/aaaa): ")
        prazo = datetime.strptime(prazo_str, "%d/%m/%Y")

        tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "prazo": prazo,
            "data_criacao": datetime.now(),
            "concluida": False
        }
        tarefas.append(tarefa)
        print("✅ Tarefa adicionada com sucesso!")
    except ValueError:
        print("❌ Entrada inválida. Tente novamente.")

def listar_tarefas():
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas):
        status = "✅ Concluída" if tarefa["concluida"] else "⌛ Pendente"
        print(f"\n[{i}] {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Prazo: {tarefa['prazo'].strftime('%d/%m/%Y')}")
        print(f"Status: {status}")

def concluir_tarefa():
    try:
        listar_tarefas()
        indice = int(input("\nDigite o número da tarefa a concluir: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("✅ Tarefa marcada como concluída.")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada inválida. Use apenas números.")

def gerar_relatorio():
    try:
        with open("relatorio_tarefas.txt", "w", encoding="utf-8") as f:
            f.write("📄 RELATÓRIO DE TAREFAS\n\n")
            for tarefa in tarefas:
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                f.write(f"Título: {tarefa['titulo']}\n")
                f.write(f"Descrição: {tarefa['descricao']}\n")
                f.write(f"Prioridade: {tarefa['prioridade']}\n")
                f.write(f"Prazo: {tarefa['prazo'].strftime('%d/%m/%Y')}\n")
                f.write(f"Status: {status}\n")
                f.write("-" * 40 + "\n")
        print("📁 Relatório gerado com sucesso: relatorio_tarefas.txt")
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {e}")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            gerar_relatorio()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida. Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()


import os
os.system('cls')

def obter_texto_valido(mensagem):
    """Garante que nome e sobrenome não fiquem em branco."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("❌ Campo obrigatório. Não pode ficar em branco.")


def cadastrar_paciente(pacientes):
    print("\n--- CADASTRO ---")
    nome = obter_texto_valido("Nome: ")
    sobrenome = obter_texto_valido("Sobrenome: ")
    pacientes.append([nome, sobrenome])
    print("Paciente cadastrado!")


def listar_pacientes(pacientes):
    print("\n--- LISTA DE PACIENTES ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for idx, p in enumerate(pacientes, start=1):
            print(f"{idx}. {p[0]} {p[1]}")


def atualizar_paciente(pacientes):
    print("\n--- ATUALIZAR ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    listar_pacientes(pacientes)
    try:
        numero = int(input("\nNúmero do paciente a atualizar: "))
        if 1 <= numero <= len(pacientes):
            novo_nome = obter_texto_valido("Novo Nome: ")
            novo_sobrenome = obter_texto_valido("Novo Sobrenome: ")
            pacientes[numero - 1] = [novo_nome, novo_sobrenome]
            print("Paciente atualizado!")
        else:
            print("Número de paciente inexistente.")
    except ValueError:
        print("Opção inválida! Digite um número.")


def excluir_paciente(pacientes):
    print("\n--- EXCLUIR ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    listar_pacientes(pacientes)
    try:
        numero = int(input("\nNúmero do paciente a excluir: "))
        if 1 <= numero <= len(pacientes):
            removido = pacientes.pop(numero - 1)
            print(f"Paciente {removido[0]} {removido[1]} removido!")
        else:
            print("Número de paciente inexistente.")
    except ValueError:
        print("Opção inválida! Digite um número.")


def buscar_paciente(pacientes):
    print("\n--- BUSCA ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    termo = input("Digite o nome ou sobrenome a buscar: ").strip().lower()
    encontrados = False
    for idx, p in enumerate(pacientes, start=1):
        if termo in p[0].lower() or termo in p[1].lower():
            print(f"{idx}. {p[0]} {p[1]}")
            encontrados = True
    
    if not encontrados:
        print("Nenhum paciente encontrado.")


def menu():
    pacientes = []
    
    while True:
        print("\n==============================")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Atualizar paciente")
        print("4. Excluir paciente")
        print("5. Buscar paciente")
        print("0. Sair")
        print("==============================")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            listar_pacientes(pacientes)
            input("\n[Pressione ENTER para voltar ao menu]")
        elif opcao == "3":
            atualizar_paciente(pacientes)
            input("\n[Pressione ENTER para voltar ao menu]")
        elif opcao == "4":
            excluir_paciente(pacientes)
            input("\n[Pressione ENTER para voltar ao menu]")
        elif opcao == "5":
            buscar_paciente(pacientes)
            input("\n[Pressione ENTER para voltar ao menu]")
        elif opcao == "0":
            print("\nPrograma encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
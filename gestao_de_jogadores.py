import os
os.system('cls')

def obter_texto_valido(mensagem_prompt):
    """Garante que a entrada não é vazia nem contém apenas espaços."""
    while True:
        texto = input(mensagem_prompt).strip()
        if texto:
            return texto
        print("❌ Erro: O campo não pode ficar em branco. Tente novamente.")


def obter_camisa_valida(mensagem_prompt, jogadores, camisa_atual=None):
    """Garante que a camisa é um número inteiro positivo e único no elenco."""
    while True:
        try:
            camisa = int(input(mensagem_prompt))
            if camisa <= 0:
                print("❌ Erro: O número da camisa deve ser um número positivo (maior que 0).")
                continue
            
            # Verifica se o número da camisa já pertence a outro jogador
            camisa_existente = False
            for j in jogadores:
                # Se estiver a atualizar, permite manter a camisa que o próprio jogador já tinha
                if j[2] == camisa and camisa != camisa_atual:
                    camisa_existente = True
                    break
            
            if camisa_existente:
                print(f"❌ Erro: A camisa #{camisa} já está a ser utilizada por outro jogador!")
            else:
                return camisa
        except ValueError:
            print("❌ Erro: Introduza apenas números inteiros válidos.")


def cadastrar_jogador(jogadores):
    print("\n--- CADASTRO DE JOGADOR ---")
    nome = obter_texto_valido("Nome: ")
    posicao = obter_texto_valido("Posição: ")
    camisa = obter_camisa_valida("Camisa: ", jogadores)
    
    jogadores.append([nome, posicao, camisa])
    print("✅ Jogador cadastrado!")


def listar_jogadores(jogadores):
    print("\n--- ELENCO DE JOGADORES ---")
    if not jogadores:
        print("⚠️ O elenco está vazio.")
    else:
        for idx, j in enumerate(jogadores, start=1):
            print(f"{idx}. {j[0]} | {j[1]} | #{j[2]}")


def atualizar_jogador(jogadores):
    print("\n--- ATUALIZAR JOGADOR ---")
    if not jogadores:
        print("⚠️ O elenco está vazio.")
        return

    listar_jogadores(jogadores)
    try:
        numero = int(input("\nNúmero do jogador a atualizar: "))
        if 1 <= numero <= len(jogadores):
            jogador_atual = jogadores[numero - 1]
            print(f"\nAtualizando dados de {jogador_atual[0]}:")
            
            novo_nome = obter_texto_valido("Novo Nome: ")
            nova_posicao = obter_texto_valido("Nova Posição: ")
            nova_camisa = obter_camisa_valida("Nova Camisa: ", jogadores, camisa_atual=jogador_atual[2])
            
            jogadores[numero - 1] = [novo_nome, nova_posicao, nova_camisa]
            print("✅ Jogador atualizado com sucesso!")
        else:
            print("❌ Número de jogador inexistente.")
    except ValueError:
        print("❌ Opção inválida! Introduza um número válido.")


def excluir_jogador(jogadores):
    print("\n--- EXCLUIR JOGADOR ---")
    if not jogadores:
        print("⚠️ O elenco está vazio.")
        return

    listar_jogadores(jogadores)
    try:
        numero = int(input("\nNúmero do jogador a excluir: "))
        if 1 <= numero <= len(jogadores):
            removido = jogadores.pop(numero - 1)
            print(f"✅ Jogador '{removido[0]}' (Camisa #{removido[2]}) removido do elenco!")
        else:
            print("❌ Número de jogador inexistente.")
    except ValueError:
        print("❌ Opção inválida! Introduza um número válido.")


def buscar_jogador(jogadores):
    print("\n--- BUSCAR JOGADOR ---")
    if not jogadores:
        print("⚠️ O elenco está vazio.")
        return

    termo = input("Digite o nome ou posição a buscar: ").strip().lower()
    encontrados = False
    
    for idx, j in enumerate(jogadores, start=1):
        if termo in j[0].lower() or termo in j[1].lower():
            print(f"{idx}. {j[0]} | {j[1]} | #{j[2]}")
            encontrados = True
            
    if not encontrados:
        print("❌ Nenhum jogador encontrado com esse termo.")


def menu():
    jogadores = []
    
    while True:
        print("\n==============================")
        print("     GERENCIAMENTO DE ELENCO   ")
        print("==============================")
        print("1. Cadastrar jogador")
        print("2. Listar jogadores")
        print("3. Atualizar jogador")
        print("4. Excluir jogador")
        print("5. Buscar jogador")
        print("0. Sair")
        print("==============================")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_jogador(jogadores)
            input("\n[Pressione ENTER para continuar]")
        elif opcao == "2":
            listar_jogadores(jogadores)
            input("\n[Pressione ENTER para continuar]")
        elif opcao == "3":
            atualizar_jogador(jogadores)
            input("\n[Pressione ENTER para continuar]")
        elif opcao == "4":
            excluir_jogador(jogadores)
            input("\n[Pressione ENTER para continuar]")
        elif opcao == "5":
            buscar_jogador(jogadores)
            input("\n[Pressione ENTER para continuar]")
        elif opcao == "0":
            print("\nPrograma encerrado.")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
            input("\n[Pressione ENTER para continuar]")


if __name__ == "__main__":
    menu()
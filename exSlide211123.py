vetor = []


def menu():
    print(
        """Escolha uma das opções abaixo:
1 - Inserir número
2 - Buscar número
    * Busca Sequencial
    * Busca Binária
3 - Exibir Lista
4 - Sair"""
    )
    return int(input())


while True:
    choice = menu()

    match choice:
        case 1:
            vetor += [int(input("Informe um número: "))]
            continue
        case 2:
            if len(vetor) <= 0:
                print("Primeiro é necessário inserir valores no vetor.")
                continue
            v = int(input("Digite o número que você busca: "))
            isOrdenado = False
            if len(vetor) > 1:
                for i in range(len(vetor)):
                    if vetor[i] <= vetor[i + 1]:
                        continue
                    else:
                        isOrdenado = False
                        break

                    if isOrdenado == True:
                        break
                    else:
                        for i in range(len(vetor)):
                            if vetor[i] == v:
                                print(f"O valor {v} está na posição {i}")
                            break
            else:
                if v == vetor[0]:
                    print("")

            print("Valor não encontrado")
            continue
        case 3:
            print(f"Lista: {vetor}")
            continue
        case 4:
            print("Saindo...")
            break
        case _:
            print("Informe um valor dentre as opções!")
            continue
    break

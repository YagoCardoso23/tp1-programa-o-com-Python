def main():
    
    votos_opcao1 = 0
    votos_opcao2 = 0
    votos_opcao3 = 0
    print("Por favor, vote nas opções abaixo:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")

    while True:
        voto = input("Digite o número correspondente à sua escolha (ou '0' para encerrar): ")

        if voto == '0':
            break
        elif voto == '1':
            votos_opcao1 += 1
        elif voto == '2':
            votos_opcao2 += 1
        elif voto == '3':
            votos_opcao3 += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

   
    print("\nResultado da votação:")
    print("Opção 1:", votos_opcao1, "votos")
    print("Opção 2:", votos_opcao2, "votos")
    print("Opção 3:", votos_opcao3, "votos")

if __name__ == "__main__":
    main()

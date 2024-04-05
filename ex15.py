def historia_interativa():
    print("Bem-vindo à história interativa!")

    
    print("\nVocê está em uma encruzilhada. Qual caminho você escolhe?")
    print("1. Caminho da esquerda")
    print("2. Caminho da direita")
    escolha1 = input("Digite 1 ou 2 para fazer sua escolha: ")

    if escolha1 == '1':
        print("\nVocê escolheu o caminho da esquerda.")
        print("Você encontra uma caverna escura.")
        
        print("\nVocê entra na caverna. Você acende uma tocha ou continua no escuro?")
        print("1. Acender uma tocha")
        print("2. Continuar no escuro")
        escolha2 = input("Digite 1 ou 2 para fazer sua escolha: ")

        if escolha2 == '1':
            print("\nVocê acende uma tocha e ilumina a caverna.")
            print("Você encontra um tesouro escondido!")
        elif escolha2 == '2':
            print("\nVocê continua no escuro e se perde na caverna.")
            print("Infelizmente, você não encontra o tesouro e fica preso na caverna para sempre.")
        else:
            print("Opção inválida. Você tropeçou e caiu em um abismo. Fim da história.")
    elif escolha1 == '2':
        print("\nVocê escolheu o caminho da direita.")
        print("Você encontra uma ponte quebrada sobre um rio.")
        
        print("\nVocê tenta atravessar a ponte quebrada ou procura por outra rota?")
        print("1. Tentar atravessar a ponte")
        print("2. Procurar por outra rota")
        escolha2 = input("Digite 1 ou 2 para fazer sua escolha: ")

        if escolha2 == '1':
            print("\nVocê tenta atravessar a ponte e cai no rio.")
            print("Felizmente, você é resgatado por uma equipe de salvamento.")
        elif escolha2 == '2':
            print("\nVocê procura por outra rota e encontra uma passagem segura.")
            print("Você continua sua jornada com sucesso.")
        else:
            print("Opção inválida. Você foi atacado por um dragão. Fim da história.")
    else:
        print("Opção inválida. Um monstro misterioso apareceu e te devorou. Fim da história.")

def main():
    historia_interativa()

if __name__ == "__main__":
    main()

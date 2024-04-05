def combine_names(username1, username2):
    
    parte1 = username1[:len(username1)//2]
    parte2 = username2[len(username2)//2:]

    
    novo_nome = parte1 + parte2

    return novo_nome

def main():
  
    username1 = input("Digite o primeiro nome de usuário: ")
    username2 = input("Digite o segundo nome de usuário: ")

    
    novo_nome = combine_names(username1, username2)

   
    print("Novo nome criativo combinado:", novo_nome)

if __name__ == "__main__":
    main()

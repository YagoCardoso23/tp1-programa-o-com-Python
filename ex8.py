def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

def main():
   
    idade = int(input("Digite sua idade: "))

    
    resultado = verificar_maioridade(idade)

    
    print(resultado)

if __name__ == "__main__":
    main()

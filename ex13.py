def verificar_palindromo(texto):
    
    texto = texto.replace(" ", "").lower()
    texto = ''.join(e for e in texto if e.isalnum())

    
    return texto == texto[::-1]

def main():
    
    texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

    
    if verificar_palindromo(texto):
        print(f"A palavra ou frase '{texto}' é um palíndromo.")
    else:
        print(f"A palavra ou frase '{texto}' não é um palíndromo.")

if __name__ == "__main__":
    main()

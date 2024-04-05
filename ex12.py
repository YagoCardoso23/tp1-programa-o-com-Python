def classificar_palavras(palavras):
    curtas = []
    longas = []

    for palavra in palavras:
        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)

    return curtas, longas

def main():
    
    entrada = input("Digite algumas palavras separadas por espaços: ")

    
    palavras = entrada.split()

    
    curtas, longas = classificar_palavras(palavras)

   
    print("Palavras curtas:", ", ".join(curtas))
    print("Palavras longas:", ", ".join(longas))

if __name__ == "__main__":
    main()

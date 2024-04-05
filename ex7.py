def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

def main():
    
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    
    imc = calcular_imc(peso, altura)

   
    classificacao = classificar_imc(imc)
    print(f"Seu IMC é {imc:.2f}, o que significa que você está {classificacao}.")

if __name__ == "__main__":
    main()

import random

def lancar_dados(quantidade_dados):
    resultados = []
    for _ in range(quantidade_dados):
        resultado = random.randint(1, 6)  
        resultados.append(resultado)
    return resultados

def main():
  
    quantidade_dados = int(input("Quantos dados você gostaria de lançar? "))

   
    resultados = lancar_dados(quantidade_dados)

   
    print("Resultados do lançamento dos dados:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Dado {i}: {resultado}")

if __name__ == "__main__":
    main()

def aplicar_desconto(valor_compra):
    desconto = 0
    
    if valor_compra > 100:
        desconto = 0.1
    elif valor_compra > 200:
        desconto = 0.15
    
    
    valor_com_desconto = valor_compra - (valor_compra * desconto)
    
    return valor_com_desconto

def main():
   
    valor_compra = float(input("Digite o valor da compra: R$"))

   
    valor_com_desconto = aplicar_desconto(valor_compra)

    
    print(f"O valor da compra com desconto é: R${valor_com_desconto:.2f}")

if __name__ == "__main__":
    main()

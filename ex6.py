import random

def main():
    
    numero_secreto = random.randint(1, 100)

   
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

   
    while True:
       
        palpite = int(input("Digite seu palpite: "))

       
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto.")
            break
        elif palpite < numero_secreto:
            print("Seu palpite está muito baixo. Tente novamente.")
        else:
            print("Seu palpite está muito alto. Tente novamente.")

if __name__ == "__main__":
    main()

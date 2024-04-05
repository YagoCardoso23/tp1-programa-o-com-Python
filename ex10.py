import random

def criar_historia(personagens, acoes, locais):
    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"{personagem} {acao} em {local}."
    return historia

def main():
   
    personagens = ["O gato", "O astronauta", "O mago", "O detetive", "A princesa","O mostro", " O guerreiro "]
    acoes = ["descobriu um tesouro", "viajou no tempo", "resolveu um mistério", "fez um feitiço", "enfrentou um monstro","enfrentou o Guerreiro"]
    locais = ["a floresta", "a lua", "um castelo abandonado", "o fundo do mar", "um planeta distante"]

   
    historia = criar_historia(personagens, acoes, locais)

   
    print("História curiosa:")
    print(historia)

if __name__ == "__main__":
    main()

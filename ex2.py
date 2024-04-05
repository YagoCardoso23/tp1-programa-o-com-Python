def minutos_para_horas_minutos(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos

def horas_minutos_para_minutos(horas, minutos):
    total_minutos = horas * 60 + minutos
    return total_minutos

def main():

    minutos_input = int(input("Digite o número total de minutos: "))
    horas, minutos = minutos_para_horas_minutos(minutos_input)
    print(f"{minutos_input} minutos correspondem a {horas} horas e {minutos} minutos.")

    
    horas_input = int(input("Digite o número de horas: "))
    minutos_input = int(input("Digite o número de minutos: "))
    total_minutos = horas_minutos_para_minutos(horas_input, minutos_input)
    print(f"{horas_input} horas e {minutos_input} minutos correspondem a {total_minutos} minutos.")

if __name__ == "__main__":
    main()

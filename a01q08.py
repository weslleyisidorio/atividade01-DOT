def continuar():
    resposta = input("Deseja continuar? (S-Sim, N-Não): ").upper()
    if resposta not in ['S', 'N']:
        print("Caractere inválido. Digite novamente.")
        continuar()
    else:
        if resposta == 'S':
            main()
        else:
            exit()


def aoCubo(numero):
    print(f"{numero}³ = {pow(numero, 3)}")
    continuar()


def main():
    while True:
        try:
            numero = int(input("Digite um numero para ser elevado ao cubo: "))
            print(aoCubo(numero))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            main()


if __name__ == "__main__":
    main()

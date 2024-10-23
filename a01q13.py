def calculaS(numero):
    s = 0
    for i in range(1, numero + 1):
        s += 1/i

    return f"S = {s}"


def main():
    while True:
        try:
            numero = int(input("Digite um número: "))
            print(calculaS(numero))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
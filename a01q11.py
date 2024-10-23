def divisores(numero):
    divisores = 1
    for i in range(2, int(numero/2)):
        if numero % i == 0:
            divisores += 1
    return numero + 1


def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(f"Quantidade de divisores: {divisores(numero)}")
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()

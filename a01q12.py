def somatorio(numero):
    total = 0
    for i in range(numero+1):
        total += i

    return f"O somatório de {numero} é: {total}"


def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            print(somatorio(numero))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()

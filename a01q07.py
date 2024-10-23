def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def main():
    while True:
        try:
            print("------------------------------------------------------")
            num = int(input("Digite um número inteiro: "))
            if num < 0:
                print("------------------------------------------------------")
                print("Entrada inválida. Número deve ser maior ou igual a 0.")
                print("Tente novamente!")
            else:
                print(f'O fatorial de {num} é: {fatorial(num)}')
                break

        except ValueError:
            print("------------------------------------------------------")
            print("Entrada inválida. Número deve ser um inteiro.")
            print("Tente novamente!")


if __name__ == "__main__":
    main()

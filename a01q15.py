def calcular_s(n):
    s = 0
    for i in range(1, n+1):
        s += (pow(i, 2) + 1) / (i + 3)
    return s


def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        s = calcular_s(numero)
        print(f'O valor de S =  {s:.2f}')

    except ValueError:
        print("Entrada inválida.")
        print("Tente novamente!")
        main()


if __name__ == "__main__":
    main()

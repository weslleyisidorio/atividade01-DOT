def Somatorio(inicio, fim):
    total = 0

    for i in range(inicio, fim + 1):
        print(i)
        total += i

    return total


def Sequencia(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1  # Troca os valores para garantir que n1 <= n2
    soma = Somatorio(n1, n2)
    return soma


def main():
    while True:
        try:
            n1 = int(input("Digite um número inteiro: "))
            n2 = int(input("Digite outro número inteiro: "))
            print(f'A soma entre {n1} e {n2} é: {Sequencia(n1, n2)}')
            break

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()

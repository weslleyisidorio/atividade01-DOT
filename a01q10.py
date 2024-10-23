def max(numero1, numero2, numero3, numero4):
    maior = numero1
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3
    if numero4 > maior:
        maior = numero4

    return maior


def main():
    while True:
        try:
            for i in range(4):
                print("Digite 4 números para saber o maior entre eles.")
                print(f"*****{i+1}ª serie de 4 números********")
                numero1 = float(input("Digite o primeiro numero: "))
                numero2 = float(input("Digite o segundo numero: "))
                numero3 = float(input("Digite o terceiro numero: "))
                numero4 = float(input("Digite o quarto numero: "))
                print(f'Maior: {max(numero1, numero2, numero3, numero4)}')
                print("-------------------------------------------------")
            break

        except ValueError:
            print("*******************************************")
            print("Entrada inválida. Digite um número inteiro.")
            print("*******************************************")


if __name__ == "__main__":
    main()

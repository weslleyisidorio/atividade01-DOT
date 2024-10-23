def fParaC(fahrenheit):
    return ((fahrenheit - 32) / 9) * 5


def main():
    while True:
        try:
            grausF = float(input("Digite a temperatura em Fahrenheit: "))
            if grausF > -459.67:
                print(f'{grausF}ºf equivalem a {fParaC(grausF):.2f}ºC.')
                break
            else:
                print("Temperatura inválida. O valor mínimo é -459.67°F.")
                print("Tente novamente!")
        except ValueError:
            print("Entrada inválida. Temperatura deve ser um número real.")
            print("Tente novamente!")


if __name__ == "__main__":
    main()

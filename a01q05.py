def PesoIdeal(altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    elif sexo == 2:
        return (72.7 * altura) - 58
    else:
        return "Entrada inválida"


def main():
    while True:
        try:
            print("------------------------------------------------------")
            altura = float(input("Digite a sua altura: "))
            sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
            if sexo in [1, 2]:
                print(f'Seu peso ideal é: {PesoIdeal(altura, sexo):.2f}kg.')
                break
            else:
                print("------------------------------------------------------")
                print("Entrada inválida.")
                print("Tente novamente!")
        except ValueError:
            print("------------------------------------------------------")
            print("Entrada inválida.")
            print("Tente novamente!")


if __name__ == "__main__":
    main()

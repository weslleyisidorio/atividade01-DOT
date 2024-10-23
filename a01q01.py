def eh_Par(numero):
    try:
        if (numero % 2) == 0:
            return "Par"
        else:
            return "Impar"
    except ValueError:
        return "Entrada inválida"


def main():
    print(eh_Par(2))
    print(eh_Par(3))
    print(eh_Par('M'))


if __name__ == "__main__":
    main()

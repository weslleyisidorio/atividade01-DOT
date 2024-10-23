def calculaMedia(nota1, nota2):
    return (nota1 + nota2)/2


def situacaoAcademica(nota1, nota2):
    media = calculaMedia(nota1, nota2)
    if media >= 6:
        return f"Média: {media} PARABÉNS! Você foi aprovado."
    else:
        return f'Média: {media}'


def main():
    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            if nota1 < 0 or nota2 < 0 or nota1 > 10 or nota2 > 10:
                print("Nota inválida. Notas devem ser números entre 0 e 10.")
                print("Tente novamente!")
            else:
                print(situacaoAcademica(nota1, nota2))
                break

        except ValueError:
            print("Entrada inválida. Notas devem ser números reais.")
            print("Tente novamente!")


if __name__ == "__main__":
    main()

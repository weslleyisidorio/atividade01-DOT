class Poligono:
    def __init__(self, qtdLados, tamLado):
        self.__qtdLados = qtdLados
        self.__tamLado = tamLado

    @property
    def qtdLados(self):
        return self.__qtdLados

    @property
    def tamLado(self):
        return self.__tamLado

    @tamLado.setter
    def tamLado(self, novoTamanho):
        self.__tamLado = novoTamanho

    def tipoForma(self):
        if self.qtdLados == 3:
            perimetro = 3 * self.tamLado
            return f"TRIÂNGULO. Perimetro = {perimetro}cm"

        elif self.qtdLados == 4:
            area = 4 * self.tamLado
            return f"QUADRADO. Área = {area}cm²"

        elif self.qtdLados == 5:
            return "PENTAGONO."
        else:
            return "Forma não cadastrada."


def main():
    while True:
        try:
            print("------------------------------------------------------")
            qtdLados = int(input("Digite a quantidade de lados: "))
            tamLado = float(input("Digite o tamanho do lado: "))
            if qtdLados < 0 and tamLado < 0:
                print("------------------------------------------------------")
                print("Entrada inválida. Valores devem ser maiores que 0.")
                print("Tente novamente!")
            else:
                o1 = Poligono(qtdLados, tamLado)
                print(o1.tipoForma())
                break

        except ValueError:
            print("------------------------------------------------------")
            print("Entrada inválida. Valores devem ser números reais.")
            print("Tente novamente!")


if __name__ == "__main__":
    main()

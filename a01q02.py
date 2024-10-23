class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novoRaio):
        self.__raio = novoRaio

    def area(self):
        return 3.14 * pow(self.raio, 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio


def main():
    while True:
        try:
            print("--------------------------------------")
            raio = float(input("Digite o valor do raio: "))
            if raio > 0:
                break
            else:
                print('--------------------------------------------')
                print("O raio não pode ser um valor negativo ou 0.")
                print("Tente novamente!")
        except ValueError:
            print('--------------------------------------------------------')
            print("Entrada inválida. Raio deve ser um número real positivo.")
            print("Tente novamente!")

    circulo1 = Circulo(raio)
    print(f'Área: {circulo1.area():.1f}cm²')
    print(f'Perimetro: {circulo1.perimetro():.1f}cm')


if __name__ == "__main__":
    main()

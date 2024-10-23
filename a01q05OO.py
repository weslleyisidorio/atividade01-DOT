class Person:
    def __init__(self, altura, sexo):
        self.__altura = altura
        self.__sexo = sexo

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, novaAltura):
        self.__altura = novaAltura

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, novoSexo):
        self.__sexo = novoSexo

    def pesoIdeal(self):
        if self.__sexo == 1:
            return (62.1 * self.__altura) - 44.7
        elif self.__sexo == 2:
            return (72.7 * self.__altura) - 58
        else:
            print("Sexo inválido")

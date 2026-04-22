class Numero:
    def _init_(self, valor):
        self.valor = valor

    def _add_(self, outro):
        return Numero(self.valor + outro.valor)

    def _str_(self):
        return str(self.valor)


# Entrada de dados
v1 = float(input("Digite o primeiro número: "))
v2 = float(input("Digite o segundo número: "))

n1 = Numero(v1)
n2 = Numero(v2)

resultado = n1 + n2
print("Resultado da soma:", resultado)

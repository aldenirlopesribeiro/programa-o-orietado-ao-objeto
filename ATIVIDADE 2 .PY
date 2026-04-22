class Caixa:
    def _init_(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def _mul_(self, outro):
        return (self.largura * self.altura) * (outro.largura * outro.altura)


# Entrada
print("Caixa 1")
l1 = float(input("Largura: "))
a1 = float(input("Altura: "))

print("\nCaixa 2")
l2 = float(input("Largura: "))
a2 = float(input("Altura: "))

c1 = Caixa(l1, a1)
c2 = Caixa(l2, a2)

print("Resultado da multiplicação (área total):", c1 * c2)

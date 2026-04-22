class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def _gt_(self, outro):
        return self.preco > outro.preco

    def _eq_(self, outro):
        return self.preco == outro.preco


# Entrada
nome1 = input("Nome do produto 1: ")
preco1 = float(input("Preço: "))

nome2 = input("\nNome do produto 2: ")
preco2 = float(input("Preço: "))

p1 = Produto(nome1, preco1)
p2 = Produto(nome2, preco2)

print("\nComparações:")
print(f"{p1.nome} é mais caro que {p2.nome}? ", p1 > p2)
print("Os preços são iguais? ", p1 == p2)

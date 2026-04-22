class Produto:
    def _init_(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def _init_(self):
        self.produtos = []

    def _add_(self, produto):
        self.produtos.append(produto)
        return self

    def total(self):
        return sum(p.preco for p in self.produtos)


# Programa
carrinho = Carrinho()

while True:
    nome = input("\nDigite o nome do produto (ou 'sair'): ")
    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço: "))
    produto = Produto(nome, preco)

    carrinho = carrinho + produto
    print("Produto adicionado!")

print("\nTotal da compra: R$", carrinho.total())

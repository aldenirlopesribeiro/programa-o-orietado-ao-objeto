class ContaBancaria:
    def _init_(self, saldo=0):
        self.saldo = saldo

    def _add_(self, valor):
        self.saldo += valor
        return self

    def _sub_(self, valor):
        self.saldo -= valor
        return self

    def _str_(self):
        return f"Saldo atual: R${self.saldo}"


# Programa
conta = ContaBancaria()

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor para depósito: "))
        conta = conta + valor

    elif opcao == "2":
        valor = float(input("Valor para saque: "))
        conta = conta - valor

    elif opcao == "3":
        print(conta)

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")

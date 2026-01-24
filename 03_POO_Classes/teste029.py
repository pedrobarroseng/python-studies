class Conta():
    def __init__(self):
        self.__saldo = 0
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Esse é o novo valor depositado: {self.__saldo}')
    
    def retirada(self, valor):
        self.__saldo -= valor
        print(f'Esse é o novo valor do saldo, após ter retirado: {self.__saldo}')

    def consultar_saldo(self):
        
        return self.__saldo


minha_conta = Conta()
minha_conta.depositar(100)
minha_conta.depositar(1300)
minha_conta.retirada(400)
print(minha_conta.consultar_saldo())

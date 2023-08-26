from models.cliente import Cliente
from models.conta import Conta
from banco import criar_conta, listar_contas


felicity: Cliente = Cliente(nome='Felicity Jones', email='felicityjones01@gmail.com', cpf='23492323122',
                            data_nascimento='30/08/2000')
angelina: Cliente = Cliente(nome='Angelina Jolie', email='angelina@gmail.com', cpf='28600244871',
                            data_nascimento='18/09/1993')
conta1: Conta = Conta(cliente=felicity)
conta2: Conta = Conta(cliente=angelina)

# print(felicity)
# print()
# print(conta1)
# print()
# print(angelina)
# print()
# print(conta2)



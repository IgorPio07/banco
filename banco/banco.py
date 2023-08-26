from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('==========================')
    print('==========ATM=============')
    print('==========================')
    print('Escolha uma operação a seguir:')
    print("1 - Criar Conta")
    print("2 - Efetuar Saque")
    print("3 - Efetuar Depósito")
    print("4 - Efetuar Transferência")
    print("5 - Listar Contas")
    print("6 - Sair do Sistema")

    opcao: int = int(input())
    match opcao:
        case 1:
            criar_conta()
        case 2:
            efetuar_sacar()
        case 3:
            efetuar_deposito()
        case 4:
            efetuar_transferencia()
        case 5:
            listar_contas()
        case 6:
            print("Volte Sempre!")
            exit(0)
        case _:
            print('opcao_invalida')
            sleep(1)
            menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')
    dicio_dados: dict = dict({'nome': input('Informe seu nome: '),
                              'email': input('Informe seu email: '),
                              'cpf': input('Informe seu cpf: '),
                              'data_nascimento': input('Informe sua data de nascimento: ')})
    cliente: Cliente = Cliente(**dicio_dados)

    nova_conta: Conta = Conta(cliente)

    print('Conta Criada com sucesso!')
    print('-------------------------')
    print(nova_conta)

    contas.append(nova_conta)

    sleep(1)
    menu()


def efetuar_sacar() -> None:
    if len(contas) > 0:
        numero_conta: int = int(input('Informe o número da sua conta'))
        conta: Conta = buscar_conta_por_numero(numero_conta)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
            print('Saque realizado com sucesso!')
        else:
            print(f'Não foi encontrada a conta com número: {numero_conta}')
    else:
        print('Ainda não há contas cadastradas')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero_conta: int = int(input('Informe o número da conta que deseja depositar: '))
        conta: Conta = buscar_conta_por_numero(numero_conta)
        if conta:
            valor: float = float(input('Informe o valor que deseja depositar: '))
            conta.depositar(valor)
        else:
            print(f'Não foi possível encontrar conta de número: {numero_conta}')
    else:
        print(f"Ainda não há contas cadastradas")
    sleep(1)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 1:

        numero_conta_o: int = int(input('Informe o número da sua conta de origem: '))
        conta: Conta = buscar_conta_por_numero(numero_conta_o)

        if conta:
            numero_conta_destino: int = int(input('Informe o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_conta_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))
                conta.transferir(valor,conta_destino)

            else:
                print(f'Não foi possível encontrar a conta de destino. {numero_conta_destino}')

        else:
            print(f'Não foi possível encontrar a conta de origem número: {numero_conta_o}')

    else:
        print('É necessário ter 2 ou mais contas para realizar uma transferência.')

    sleep(1)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        for conta in contas:
            print('------------------')
            print(conta)
            print('------------------')
            sleep(1)
    else:
        print('AInda não há contas cadastradas!')

    sleep(1)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()

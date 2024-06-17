import sys

# As variáveis para armazenar os dados da conta
saldo = 0.0
extrato = []
saques_diarios = 0

# A função depositar o dinheiro
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Deposito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")

# Função sacar dinheiro
def sacar(valor):
    global saldo, saques_diarios
    if saques_diarios >= 3:
        print("Limite diario de saques atingido!")
        return
    if valor > saldo:
        print("Saldo insuficiente!")
        return
    if valor > 500:
        print("Limite maximo por saque e de R$ 500,00")
        return
    if valor <= 0:
        print("Valor de saque invalido!")
        return
    saldo -= valor
    saques_diarios += 1
    extrato.append(f"Saque: R$ {valor:.2f}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Função visualizar extrato
def visualizar_extrato():
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for movimento in extrato:
            print(movimento)
        print(f"Saldo atual: R$ {saldo:.2f}")

# Função sistema bancário
def sistema_bancario():
    while True:
        print("\n==$== Sistema Bancario ==$==")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            valor = float(input("Digite o valor do deposito: "))
            depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            sacar(valor)
        elif opcao == '3':
            visualizar_extrato()
        elif opcao == '4':
            print("Saindo do sistema. Obrigado por utilizar o sistema bancario!")
            break
        else:
            print("Opcao invalida! Tente novamente.")

# sistema bancário v1
sistema_bancario()

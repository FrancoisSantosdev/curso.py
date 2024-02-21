# Menu de operações disponíveis
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis iniciais do sistema bancário
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do sistema
while True:
    
    # Solicita ao usuário que escolha uma operação
    opcao = input(menu)

    # Opção de Depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é válido
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de Saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Verifica diversas condições para garantir a validade do saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de Extrato
    elif opcao == "e":
        print("\n===============EXTRATO===============")
        # Exibe o extrato ou uma mensagem se não houver movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    # Opção de Sair do sistema
    elif opcao == "q":
        break

    # Mensagem para operações inválidas
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



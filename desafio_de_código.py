menu = """
[1] depositar
[2] sacar
[3] extrato
[4] sair
-> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito a ser realizado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação cancelada pois o valor informado é inválido!")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque a ser realizado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação cancelada pois o saldo disponível não é suficiente!")
        elif excedeu_limite:
            print("Operação canceladaa pois o valor do saque desejado excede o limite disponível!")
        elif excedeu_saque:
            print("Operação cancelada pois o número máximo de saques disponível foi atingido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação cancelada pois o valor informado é inválido!")

    elif opcao == "3":
        print("Sem movimentações realziadas recentemente!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print("Operação cancelada. Por gentileza, informe no menu a opção desejada!")

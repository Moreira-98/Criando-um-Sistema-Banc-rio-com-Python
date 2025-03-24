menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = int(input(menu))

    match opcao:

        case 1:
            deposita_valor = float(input("Informe o valor do depósito: "))

            if deposita_valor > 0:
                saldo += deposita_valor
                extrato += f"Depósito: R$ {deposita_valor:.2f}\n"
                print(f"\nSeu saldo atual: R$ {saldo:.2f}")
            else:
                print(
                    f"Operação falhou! O valor de R${deposita_valor:.2f} "
                    f"é inválido."
                )

        case 2:
            saque_valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = saque_valor > saldo
            excedeu_limite = saque_valor > limite
            excedeu_saques = numero_saques >= LIMITE_DE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif saque_valor > 0:
                saldo -= saque_valor
                extrato += f"Saque: R$ {saque_valor:.2f}\n"
                numero_saques += 1
                print(f"\nSeu saldo atual: R$ {saldo:.2f}")

            else:
                print("Operação falhou! O valor informado é inválido.")

        case 3:
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=========================================")

        case 4:
            print("Saindo...")
            break

        case _:
            print(
                "Operação inválida, por favor selecione novamente a "
                "operação desejada."
            )

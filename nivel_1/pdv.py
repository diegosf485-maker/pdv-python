
total_compras = 0
total_descontos = 0
quantidade_compras = 0

while True:
    try:
        valor = float(input("Digite o valor da compra (0 para encerrar): R$ "))

        if valor == 0:
            break

        if valor < 0:
            print("Valor inválido! Digite um valor positivo.")
            continue

        idade = int(input("Digite a idade do cliente: "))

        if idade < 0:
            print("Idade inválida! Digite uma idade positiva.")
            continue

        desconto = 0

        if idade < 18:
            desconto = 0.10
        elif idade >= 60:
            desconto = 0.15

        valor_desconto = valor * desconto
        valor_final = valor - valor_desconto

        print("\n--- Resumo da compra ---")
        print(f"Valor original: R$ {valor:.2f}")
        print(f"Desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {valor_final:.2f}")

        total_compras += valor
        total_descontos += valor_desconto
        quantidade_compras += 1

    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print("\n=== RESUMO GERAL ===")
print(f"Quantidade de compras: {quantidade_compras}")
print(f"Valor total das compras: R$ {total_compras:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total arrecadado: R$ {total_compras - total_descontos:.2f}")
print("Programa encerrado!")

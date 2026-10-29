# PDV com descontos em Python



historico = []

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

        # Primeira regra: desconto por idade
        desconto_idade = 0

        if idade >= 65:
            desconto_idade = valor * 0.20

        valor_apos_idade = valor - desconto_idade

        # Segunda regra: desconto adicional
        desconto_adicional = 0

        if valor_apos_idade > 100:
            desconto_adicional = valor_apos_idade * 0.10

        # Cálculo dos valores finais
        desconto_total = desconto_idade + desconto_adicional
        valor_final = valor - desconto_total

        # Guardar a compra no histórico
        compra = {
            "valor_original": valor,
            "idade": idade,
            "desconto_idade": desconto_idade,
            "desconto_adicional": desconto_adicional,
            "desconto_total": desconto_total,
            "valor_final": valor_final
        }

        historico.append(compra)

        # Mostrar resultado da compra
        print("\n--- Resultado da compra ---")
        print(f"Valor original: R$ {valor:.2f}")
        print(f"Desconto por idade: R$ {desconto_idade:.2f}")
        print(f"Desconto adicional: R$ {desconto_adicional:.2f}")
        print(f"Desconto total: R$ {desconto_total:.2f}")
        print(f"Total a pagar: R$ {valor_final:.2f}")

    except ValueError:
        print("Entrada inválida! Digite um número válido.")

# Resumo geral
print("\n===== RESUMO GERAL =====")

total_original = 0
total_descontos = 0
total_arrecadado = 0

for compra in historico:
    total_original += compra["valor_original"]
    total_descontos += compra["desconto_total"]
    total_arrecadado += compra["valor_final"]

print(f"Quantidade de compras: {len(historico)}")
print(f"Valor total das compras: R$ {total_original:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total arrecadado: R$ {total_arrecadado:.2f}")

print("\nHistórico de compras:")

for numero, compra in enumerate(historico, start=1):
    print(f"\nCompra {numero}")
    print(f"Valor original: R$ {compra['valor_original']:.2f}")
    print(f"Idade: {compra['idade']}")
    print(f"Desconto total: R$ {compra['desconto_total']:.2f}")
    print(f"Valor final: R$ {compra['valor_final']:.2f}")

print("\nPrograma encerrado!")

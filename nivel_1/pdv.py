# PDV com descontos em Python


compras = []

while True:
    try:
        valor = float(input("Valor da compra (0 para encerrar): ").replace(",", "."))
    except ValueError:
        print("Aviso: digite um valor valido.")
        continue

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: valor nao pode ser negativo.")
        continue

    while True:
        try:
            idade = int(input("Idade do cliente: "))
            if idade < 0:
                print("Aviso: idade nao pode ser negativa.")
                continue
            break
        except ValueError:
            print("Aviso: digite uma idade valida.")

    original = valor
    desconto_idade = 0
    desconto_valor = 0

    if idade >= 65:
        desconto_idade = valor * 0.20
        valor -= desconto_idade

    if original >= 200:
        desconto_valor = valor * 0.10
        valor -= desconto_valor

    desconto_total = original - valor

    compras.append({
        "original": original,
        "desconto": desconto_total,
        "final": valor
    })

    print(f"Valor original: R$ {original:.2f}")
    print(f"Desconto idade: R$ {desconto_idade:.2f}")
    print(f"Desconto valor: R$ {desconto_valor:.2f}")
    print(f"Valor final: R$ {valor:.2f}")

print("\n===== RESUMO DAS COMPRAS =====")
print(f"Quantidade: {len(compras)}")
print(f"Total bruto: R$ {sum(c['original'] for c in compras):.2f}")
print(f"Total descontos: R$ {sum(c['desconto'] for c in compras):.2f}")
print(f"Total final: R$ {sum(c['final'] for c in compras):.2f}")


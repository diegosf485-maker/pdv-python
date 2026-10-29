
PDV com Descontos 

O que o código faz

O programa PDV em Python calcula descontos de acordo com a idade do cliente e o valor da compra. Ao final, apresenta um resumo das compras realizadas.

Como funciona

1. Recebe o valor da compra.
2. Encerra quando o usuário digita zero.
3. Rejeita valores negativos e solicita um novo valor.
4. Solicita a idade do cliente e rejeita idades negativas.
5. Aplica 20% de desconto para clientes com 65 anos ou mais.
6. Se o valor após o desconto por idade for maior que R$ 100,00, aplica mais 10%.
7. Guarda os dados das compras em uma lista.
8. Exibe os descontos, o valor final e o resumo de todas as compras.

Como executar

Execute no terminal:

python pdv.py

Tabela de exemplos

Valor original| Idade| Desconto por idade| Desconto por valor| Desconto total| Valor final
R$ 125,00| 70| R$ 25,00| R$ 10,00| R$ 35,00| R$ 90,00
R$ 200,00| 64| R$ 0,00| R$ 20,00| R$ 20,00| R$ 180,00
R$ 101,00| 30| R$ 0,00| R$ 10,10| R$ 10,10| R$ 90,90

Observação: os descontos são aplicados sucessivamente. O desconto por valor é calculado sobre o valor restante após o desconto por idade.

Arquivos do projeto

- "pdv.py": código do sistema.
- "README.md": documentação do projeto.
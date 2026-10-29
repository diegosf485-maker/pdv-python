
PDV com Descontos 

PDV com Descontos

O que o código faz

O PDV (Ponto de Venda) é um programa desenvolvido em Python que calcula descontos com base na idade do cliente e no valor da compra. O sistema registra as compras realizadas, apresenta os valores calculados e gera um resumo geral ao final da execução.

Como funciona

1. Solicita o valor da compra.
2. Encerra o programa quando o usuário digita 0.
3. Verifica se o valor da compra é negativo.
4. Solicita a idade do cliente e verifica se é válida.
5. Calcula o desconto por idade.
6. Calcula o desconto por valor da compra.
7. Exibe o valor original, os descontos aplicados e o total a pagar.
8. Armazena os dados das compras em uma lista.
9. Apresenta o histórico e o resumo geral ao encerrar.

Regras de desconto

- Desconto por idade: aplica 20% para clientes com 65 anos ou mais.
- Desconto por valor da compra: aplica 10% adicional quando o valor após o desconto por idade é superior a R$ 100,00.

Exemplos de teste

Valor da compra| Idade| Desconto por idade| Desconto por valor| Total a pagar

R$ 50,00| 30| R$ 0,00| R$ 0,00| R$ 50,00

R$ 150,00| 30| R$ 0,00| R$ 15,00| R$ 135,00

R$ 200,00| 70| R$ 40,00| R$ 16,00| R$ 144,00

R$ 80,00| 70| R$ 16,00| R$ 0,00| R$ 64,00

Validações

- Rejeita valores negativos.
- Rejeita idades negativas.
- Exibe uma mensagem de erro para entradas não numéricas.
- Continua executando até o usuário digitar 0.

Como executar

É necessário ter o Python instalado.

python pdv.py

Arquivos do projeto

- "pdv.py": código-fonte do programa.
- "README.md": documentação do projeto.

Objetivo

Praticar lógica de programação, condicionais, laços de repetição, listas, validação de dados e cálculos financeiros.
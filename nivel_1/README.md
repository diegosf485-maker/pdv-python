
PDV com Descontos 

O que o código faz

O PDV (Ponto de Venda) é um programa desenvolvido em Python que calcula descontos de acordo com a idade do cliente e o valor da compra. O programa registra as compras em uma lista, apresenta os valores de cada operação e, ao final, exibe um resumo geral.

Como funciona

1. Solicita o valor da compra.
2. Encerra o programa quando o usuário digita 0.
3. Verifica se o valor da compra é negativo. Se for, exibe uma mensagem de erro e solicita uma nova entrada.
4. Solicita a idade do cliente e verifica se ela é válida.
5. Aplica desconto de 20% para clientes com 65 anos ou mais.
6. Aplica um desconto adicional de 10% quando o valor restante após o primeiro desconto é superior a R$ 100,00.
7. Exibe o valor original, os descontos aplicados e o total a pagar.
8. Armazena os dados de cada compra na lista "historico".
9. Ao encerrar, apresenta a quantidade de compras, o valor total das compras, o total de descontos, o total arrecadado e o histórico das operações.

Exemplos de teste

Valor da compra| Idade| Desconto total| Total a pagar
R$ 50,00| 30| R$ 0,00| R$ 50,00
R$ 150,00| 30| R$ 15,00| R$ 135,00
R$ 200,00| 70| R$ 56,00| R$ 144,00
R$ 80,00| 70| R$ 16,00| R$ 64,00

Os exemplos demonstram o funcionamento das regras de desconto implementadas no código.

Validações

- Valores negativos são rejeitados.
- Idades negativas são rejeitadas.
- Entradas não numéricas exibem uma mensagem de erro.
- O programa continua executando até que o usuário digite 0 para encerrar.

Como executar

É necessário ter o Python instalado.

Execute o comando:

python pdv.py

Arquivos do projeto

- "pdv.py": contém o código-fonte do programa.
- "README.md": apresenta a documentação, as regras de funcionamento e os exemplos de teste.

Objetivo

Praticar lógica de programação, estruturas condicionais, laços de repetição, listas, validação de dados e cálculos financeiros.

PDV com Descontos 

O que o código faz

O PDV (Ponto de Venda) é um programa desenvolvido em Python que calcula descontos de acordo com a idade do cliente e o valor da compra. Ao final, apresenta os valores de cada compra e um resumo geral das operações realizadas.

Como funciona

1. Solicita o valor da compra.
2. Encerra o programa quando o usuário digita "0".
3. Rejeita valores negativos e solicita um novo valor.
4. Solicita a idade do cliente e rejeita idades negativas.
5. Aplica 20% de desconto para clientes com 65 anos ou mais.
6. Se o valor restante após o desconto por idade for maior que R$ 100,00, aplica mais 10% de desconto.
7. Armazena os dados de cada compra em uma lista.
8. Exibe o valor original, os descontos e o valor final.
9. Ao encerrar, apresenta o resumo com a quantidade de compras, o total bruto, os descontos totais e o valor final acumulado.


- Desconto por idade: 20% para clientes com idade igual ou superior a 65 anos.
- Desconto adicional: 10% quando o valor após o desconto por idade for maior que R$ 100,00.
- Descontos sucessivos: o desconto adicional é calculado sobre o valor restante, e não sobre o valor original.

Tabela de exemplos

Valor da compra| Idade| Desc. por idade| Desc. adicional| Total de descontos| Valor final 

R$ 125,00 | 70 anos| R$ 25,00| R$ 10,00| R$ 35,00| R$ 90,00

R$ 200,00| 64 anos| R$ 0,00| R$ 20,00| R$ 20,00| R$ 180,00

R$ 101,00| 30 anos| R$ 0,00| R$ 10,10| R$ 10,10| R$ 90,90

Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

python pdv.py

3. Digite o valor da compra e a idade do cliente.
4. Confira os descontos calculados na tela.
5. Digite "0" para encerrar e visualizar o resumo final.

Arquivos do projeto

- "pdv.py" — código-fonte do sistema PDV.
- "README.md" — documentação com as instruções, regras e exemplos de funcionamento.

Objetivo do projeto

Praticar conceitos fundamentais de Python, como variáveis, estruturas condicionais, laços de repetição, tratamento de erros, listas e cálculos matemáticos.
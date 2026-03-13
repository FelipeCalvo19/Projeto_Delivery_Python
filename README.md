# 🍔 Sistema de Delivery - Lógica em Python

Este é um projeto de estudo desenvolvido para simular o backend de um sistema de delivery. O foco principal foi a aplicação de **lógica de programação pura**, sem o uso de frameworks externos, priorizando a modularização e a validação de dados.

## 🛠️ O que eu pratiquei aqui:

* **Modularização com Funções (`def`):** Divisão de responsabilidades para cálculo de preços, taxas e formatação de saída.
* **Lógica Booleana Composta (`and not`):** Implementação de trava de segurança para venda de bebidas alcoólicas baseada na idade do usuário.
* **Condicionais Aninhadas:** Cálculo dinâmico de taxa de entrega baseado em múltiplos fatores (distância e condições climáticas).
* **Manipulação de Variáveis de Escopo:** Gerenciamento de subtotais e aplicação de descontos cumulativos.

## 🚀 Funcionalidades Realistas

* **Menu Dinâmico:** Retorno de preços baseado na seleção de itens.
* **Cálculo de Frete:** Tabela progressiva de frete por KM + adicional por clima chuvoso.
* **Sistema de Desconto:** Gatilho automático de 10% de desconto para pedidos acima de R$ 40,00.
* **Recibo Detalhado:** Exibição do valor bruto vs. valor com desconto (economia gerada).

## 💻 Exemplo de Saída no Terminal
''' Qual seu Nome?Felipe
Quantos Anos voce tem?21
Oi Felipe, tudo bem?
Voce deseja fazer um pedido? (s/n)s
Qual lanche você gostaria de pedir? (hambúrguer, pizza, salada)pizza
Otima escolha! O preço do seu lanche é R$25.00
Você gostaria de Adicionar uma bebida?(s/n)s
Qual Bebida voce gostaria?(refri, suco , cerveja)cerveja
Otima escolha! o preco da sua bebida é R$7.00
você mora a quantos km do local de entrega?15
Como está o clima hoje? (ensolarado, chuvoso, nublado)chuvoso

==============================
        RECIBO DE COMPRA
==============================
Lanche:   Pizza
Bebida:   R$7.00
Entrega:  R$12.00 (incluindo taxa adicional por clima chuvoso)
------------------------------
SUBTOTAL: R$44.00
DESCONTO: R$4.40 (10% OFF)
TOTAL A PAGAR: R$39.60
 Parabens! Voce ganhou um Desconto de 10% Aproveite!
==============================
Obrigado por pedir conosco Felipe! Tenha um ótimo dia!
==============================
'''

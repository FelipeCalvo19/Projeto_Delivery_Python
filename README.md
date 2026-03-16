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
## 🏛️ Organização Profissional
O projeto utiliza o padrão **`def main()`**, seguindo as melhores práticas da indústria:
* **Encapsulamento**: A lógica de execução é isolada das funções de cálculo.
* **Ponto de Entrada**: Uso da estrutura `if __name__ == "__main__":` para garantir que o script seja executado de forma controlada.
* **Escopo de Variáveis**: Melhor gerenciamento de memória e segurança dos dados dentro do fluxo principal.

## 💻 Exemplo de Saída no Terminal
```text █▀█ █▀▀ █▄░█ ▄▀█ ▀█▀ ▄▀█ █▀█   █░░ ▄▀█ █▄░█ █▀▀ █░█ █▀▀ █▀
    █▀▄ ██▄ █░▀█ █▀█ ░█░ █▀█ █▄█   █▄▄ █▀█ █░▀█ █▄▄ █▀█ ██▄ ▄█

Qual seu Nome?Felipe
Quantos Anos voce tem?20
Oi Felipe, tudo bem?
Voce deseja fazer um pedido? (s/n)s
Qual lanche você gostaria de pedir? (hambúrguer, pizza, salada)pizza
Otima escolha! O preço do seu lanche é R$25.00
Você gostaria de Adicionar uma bebida?(s/n)n
você mora a quantos km do local de entrega?15
Como está o clima hoje? (ensolarado, chuvoso, nublado)chuvoso
==============================
        RECIBO DE COMPRA
==============================
Lanche:   Pizza R$25.00
Bebida:   Nenhuma R$0.00
Entrega:  R$10.00 (incluindo taxa adicional por clima chuvoso)
------------------------------
SUBTOTAL: R$35.00
TOTAL A PAGAR: R$35.00
==============================
Obrigado por pedir conosco Felipe Josue! Tenha um ótimo dia!```

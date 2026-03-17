# 🍔 Sistema de Delivery V2 - Lógica Avançada em Python

Este projeto evoluiu de um simulador básico para um backend de delivery estruturado com foco em **Clean Code** (Código Limpo) e **eficiência de dados**. O objetivo foi aplicar padrões de mercado para tornar o sistema resiliente a erros e fácil de manter.

## 🛠️ Evolução Técnica (O que eu dominei aqui):

* **Estruturas de Dados Pro:** Uso de **Listas de Dicionários** para exibir menus ricos (lanches + ingredientes) e **Dicionários Puros** para busca instantânea de preços (O(1)).
* **Fluxo de Controle Otimizado (Early Return):** Substituição de condicionais aninhadas por retornos antecipados, mantendo o código "plano" e legível.
* **Tratamento de Exceções (`try/except`):** Blindagem do sistema contra entradas inválidas do usuário (letras onde se espera números).
* **Operadores Ternários:** Implementação de lógica de decisão em linha para atribuição dinâmica de taxas e mensagens de desconto.
* **Modularização de Responsabilidades:** Separação clara entre funções de interface (Exibição) e funções de lógica (Cálculo).

## 🚀 Funcionalidades Realistas

* **Cardápio Inteligente:** Listagem detalhada de ingredientes e formatação monetária automática.
* **Trava de Segurança (Compliance):** Verificação rigorosa de maioridade para itens restritos (cerveja).
* **Logística Dinâmica:** Cálculo de frete progressivo por KM com gatilho de taxa de conveniência para clima chuvoso.
* **Gatilho de Desconto:** Aplicação de 10% OFF automático para pedidos acima de R$ 40,00, informando a economia gerada ao cliente.
* **UX no Terminal:** Uso de comandos do sistema para limpeza de tela e organização de etapas do pedido.

## 🏛️ Arquitetura do Projeto
O script segue o padrão profissional de execução:
* **Encapsulamento**: Variáveis de escopo local protegidas dentro da `def main()`.
* **Ponto de Entrada**: Estrutura `if __name__ == "__main__":` para execução controlada.
* **Manutenibilidade**: Funções pequenas e especialistas, facilitando a adição de novos produtos ou regras de frete.

## 💻 Exemplo de Execução Atualizada
```text
    █▀█ █▀▀ █▄░█ ▄▀█ ▀█▀ ▄▀█ █▀█   █░░ ▄▀█ █▄░█ █▀▀ █░█ █▀▀ █▀
    █▀▄ ██▄ █░▀█ █▀█ ░█░ █▀█ █▄█   █▄▄ █▀█ █░▀█ █▄▄ █▀█ ██▄ ▄█

Qual seu Nome? Felipe
Quantos Anos voce tem? 20
Oi Felipe, tudo bem?

--- CARDÁPIO DE LANCHES ---
Hambúrguer - R$10.00
 [Pão, Carne, Alface, Tomate, Queijo, Presunto e Molhos da Casa]
--------------------
...

==============================
        RECIBO DE COMPRA
==============================
Lanche:   Hambúrguer (R$10.00)
Bebida:   Cerveja (R$6.00)
Entrega:  R$7.00 (taxa de chuva aplicada)
------------------------------
SUBTOTAL: R$23.00
TOTAL A PAGAR: R$23.00
==============================
<<<<<<< HEAD
Obrigado por pedir conosco Felipe! Tenha um ótimo dia!```
=======
Obrigado por pedir conosco Felipe! Tenha um ótimo dia!
==============================
>>>>>>> b5321de (refactor: finaliza sistema de delivery e atualiza readme)

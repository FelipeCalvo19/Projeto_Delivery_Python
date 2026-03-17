# =============================================================================
# SISTEMA DE DELIVERY - VERSÃO 2.0 (ESTUDO DE ESTRUTURAS DE DADOS)
# Objetivo: Praticar Listas, Dicionários, Tratamento de Erros e Operadores Ternários.
# =============================================================================
import os

# ---------------------------------------------------------
# FUNÇÕES DE INTERFACE E COMUNICAÇÃO
# ---------------------------------------------------------

def Boas_vindas(Nome):
    """Gera saudação personalizada."""
    return f"Oi {Nome}, tudo bem?"

def Despedidas(Nome):
    """Gera mensagem de encerramento amigável."""
    return f"Obrigado por pedir conosco {Nome}! Tenha um ótimo dia!"

def Criar_Linhas(Divisor):
    """Cria separadores visuais para organizar o terminal."""
    return Divisor * 30

def Conversor_Valor(Valor, cifra):
    """Formata números para o padrão monetário R$ 0,00."""
    return f"{cifra}{Valor:.2f}"

# ---------------------------------------------------------
# LÓGICA DE PRODUTOS E PREÇOS (CARDÁPIOS)
# ---------------------------------------------------------

def Cardapio_Lanches():
    """Exibe a lista detalhada de lanches e seus ingredientes (Usa Lista de Dicionários)."""
    cardapio = [
        {"Lanche": "hambúrguer", "Valor": 10.00, "Ingredientes": "Pão, Carne, Alface, Tomate, Queijo, Presunto e Molhos da Casa"},
        {"Lanche": "pizza", "Valor": 20.00, "Ingredientes": "Molho de Tomate, Queijo e Calabresa"},
        {"Lanche": "salada", "Valor": 5.00, "Ingredientes": "Alface, Tomate, Azeitona, Azeite, Pepino e Cebola"}
    ]
    print("\n--- CARDÁPIO DE LANCHES ---")
    for item in cardapio:
        print(f"{item['Lanche'].capitalize()} - {Conversor_Valor(item['Valor'], 'R$')}\n [{item['Ingredientes']}]")
        print("-" * 20)
    print(Criar_Linhas("="))

def Preco_Lanches(Lanche_escolhido):
    """Busca o preço de forma instantânea (Usa Dicionário Puro para performance)."""
    Valores = {"hambúrguer": 10.00, "pizza": 20.00, "salada": 5.00}
    return Valores.get(Lanche_escolhido, 0.00)

def Cardapio_Bebidas():
    """Exibe as opções de bebidas disponíveis."""
    cardapioB = [
        {"Bebida": "refri", "Valor": 5.00},
        {"Bebida": "suco", "Valor": 5.50},
        {"Bebida": "cerveja", "Valor": 6.00}
    ]
    print("\n--- CARDÁPIO DE BEBIDAS ---")
    for item in cardapioB:
        print(f"{item['Bebida'].capitalize()} - {Conversor_Valor(item['Valor'], 'R$')}")
        print("-" * 20)
    print(Criar_Linhas("="))

def Preco_Bebidas(Bebida_escolhida):
    """Retorna o valor da bebida selecionada."""
    Valores = {"refri": 5.00, "suco": 5.50, "cerveja": 6.00}
    return Valores.get(Bebida_escolhida, 0.00)

# ---------------------------------------------------------
# REGRAS DE NEGÓCIO E VALIDAÇÕES
# ---------------------------------------------------------

def DetectorDidade(Idade):
    """Verifica maioridade legal para venda de álcool."""
    return Idade >= 18

def calcular_Desconto(valortotal):
    """Aplica regra de 10% de desconto sobre o valor total."""
    return valortotal * 0.9

# ---------------------------------------------------------
# FLUXO PRINCIPAL DO SISTEMA
# ---------------------------------------------------------

def main():
    # Título do Sistema em ASCII
    print ("""
    █▀█ █▀▀ █▄░█ ▄▀█ ▀█▀ ▄▀█ █▀█   █░░ ▄▀█ █▄░█ █▀▀ █░█ █▀▀ █▀
    █▀▄ ██▄ █░▀█ █▀█ ░█░ █▀█ █▄█   █▄▄ █▀█ █░▀█ █▄▄ █▀█ ██▄ ▄█""")
    
    Nome = input("\nQual seu Nome? ")
    
    # Loop de validação de entrada numérica (Idade)
    while True:
        try:
            idade = int(input("Quantos Anos voce tem? "))
            if 0 < idade < 100: break
            print("Digite uma Idade Valida!! (1 a 99)")
        except ValueError:
            print("Erro! Digite apenas números para a idade.")

    print(Boas_vindas(Nome))

    if input("Voce deseja fazer um pedido? (s/n) ").lower().strip() == "n":
        print("Entendido, se precisar de algo é só chamar!")
        return

    # --- PROCESSO DE COMPRA: LANCHE ---
    os.system("cls" if os.name == "nt" else "clear")
    Cardapio_Lanches()
    lanche = input("Qual lanche você gostaria de pedir? ").lower().strip()
    preco = Preco_Lanches(lanche)

    if preco == 0.00:
        print("Lanche inválido. Pedido cancelado.")
        return
    
    print(f"Otima escolha! Preço: {Conversor_Valor(preco, 'R$')}")

    # --- PROCESSO DE COMPRA: BEBIDA ---
    precoB = 0.00
    bebida = "nenhuma"
    if input("Você gostaria de Adicionar uma bebida? (s/n) ").lower().strip() == "s":
        os.system("cls" if os.name == "nt" else "clear")
        Cardapio_Bebidas()
        bebida = input("Qual Bebida voce gostaria? ").lower().strip()
        precoB = Preco_Bebidas(bebida)
        
        # Validação de idade para Cerveja
        if bebida == "cerveja" and not DetectorDidade(idade):
            print("Sinto muito, você não tem idade para comprar bebidas alcoólicas!")
            precoB = 0.00
            bebida = "cancelada (menor de idade)"
        elif precoB == 0.00:
            print("Bebida não encontrada!")
        else:
            print(f"Bebida adicionada! Preço: {Conversor_Valor(precoB, 'R$')}")

    # --- LOGÍSTICA DE ENTREGA ---
    while True:
        try:
            distancia = float(input("Distância para entrega (km): "))
            if distancia >= 0: break
            print("Distância inválida!")
        except ValueError:
            print("Digite apenas números!")

    clima = input("Clima (ensolarado/chuvoso/nublado): ").lower().strip()

    # Cálculo da taxa baseada em distância
    if distancia <= 5: taxa = 5.00
    elif distancia <= 10: taxa = 8.00
    else: taxa = 10.00
            
    # Ajustes dinâmicos usando OPERADORES TERNÁRIOS
    taxa += 2.00 if clima == "chuvoso" else 0.00
    msg_clima = " (taxa de chuva aplicada)" if clima == "chuvoso" else ""
    
    # --- FECHAMENTO DA CONTA ---
    subtotal = preco + precoB + taxa
    # Aplica desconto se a compra for acima de R$ 40
    total_final = calcular_Desconto(subtotal) if subtotal >= 40 else subtotal
    msg_desc = " Parabens! Você ganhou 10% de desconto!" if subtotal >= 40 else ""

    # --- EMISSÃO DO RECIBO FINAL ---
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + Criar_Linhas("="))
    print("         RECIBO DE COMPRA")
    print(Criar_Linhas("="))
    print(f"Lanche:   {lanche.capitalize()} ({Conversor_Valor(preco, 'R$')})")
    print(f"Bebida:   {bebida.capitalize()} ({Conversor_Valor(precoB, 'R$')})")
    print(f"Entrega:  {Conversor_Valor(taxa, 'R$')}{msg_clima}")
    print(Criar_Linhas("-"))
    print(f"SUBTOTAL: {Conversor_Valor(subtotal, 'R$')}")
    
    if subtotal >= 40:
        print(f"ECONOMIA: {Conversor_Valor(subtotal - total_final, 'R$')}")
        print(msg_desc)
        
    print(f"TOTAL A PAGAR: {Conversor_Valor(total_final, 'R$')}")
    print(Criar_Linhas("="))
    print(Despedidas(Nome))
    print(Criar_Linhas("="))

if __name__ == "__main__":
    main()
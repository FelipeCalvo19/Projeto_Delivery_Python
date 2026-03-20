# =============================================================================
# SISTEMA DE DELIVERY - VERSÃO 2.0 (ESTUDO DE ESTRUTURAS DE DADOS)
# Objetivo: Praticar Listas, Dicionários, Tratamento de Erros e Operadores Ternários.
# =============================================================================
import os
from datetime import datetime
# ---------------------------------------------------------
# VARIÁVEIS GLOBAIS (ESTADO DO SISTEMA)
# ---------------------------------------------------------
# Armazena apenas os números (floats) de cada venda finalizada
historico_faturamento = [] 
horas = datetime.now().hour
# Dicionário para o Ranking: Chave = Nome do Cliente | Valor = Total acumulado
# Escolhemos dicionário pela busca rápida O(1) e facilidade de somar valores por chave
rank_gastos = {}

# ---------------------------------------------------------
# FUNÇÕES DE INTERFACE E AUXILIARES
# ---------------------------------------------------------
def saudaçao_horario (Horas):
    horario = datetime.now().hour
    momento = "nenhum"
    if 6.00 <= horario < 12:
        momento = "Dia"
    elif 12.00 <= horario < 18:
        momento = "Tarde"
    elif 19.00 <= horario < 23:
        momento = "Noite"
    else: 
        momento = "madrugada"

    return momento
     
def Boas_vindas(Nome):
    """Retorna saudação. Exemplo de uso de f-strings para interpolação."""
    return f"Bom {saudaçao_horario(horas)} {Nome}!! tudo bem?"

def Despedidas(Nome):
    return f"Obrigado por pedir conosco {Nome}! Tenha um ótimo {saudaçao_horario(horas)}!"

def Criar_Linhas(Divisor):
    """Multiplicação de strings para criar separadores visuais dinâmicos."""
    return Divisor * 30

def Conversor_Valor(Valor, cifra):
    """Formatação de moeda usando .2f para garantir duas casas decimais."""
    return f"{cifra}{Valor:.2f}"

       

# ---------------------------------------------------------
# LÓGICA DE PRODUTOS (CARDÁPIOS)
# ---------------------------------------------------------

def Cardapio_Lanches():
    """
    Usa uma Lista de Dicionários. Ideal quando cada item tem múltiplas 
    propriedades (Nome, Valor, Ingredientes).
    """
    cardapio = [
        {"Lanche": "hambúrguer", "Valor": 10.00, "Ingredientes": "Pão, Carne, Alface..."},
        {"Lanche": "pizza", "Valor": 20.00, "Ingredientes": "Molho de Tomate, Queijo..."},
        {"Lanche": "salada", "Valor": 5.00, "Ingredientes": "Alface, Tomate..."}
    ]
    print("\n--- CARDÁPIO DE LANCHES ---")
    for item in cardapio:
        print(f"{item['Lanche'].capitalize()} - {Conversor_Valor(item['Valor'], 'R$')}\n [{item['Ingredientes']}]")
        print("-" * 20)
    print(Criar_Linhas("="))

def Preco_Lanches(Lanche_escolhido):
    """
    Usa Dicionário Simples para busca direta. 
    O método .get() evita erros caso o lanche não exista (retorna 0.00).
    """
    Valores = {"hambúrguer": 10.00, "pizza": 20.00, "salada": 5.00}
    return Valores.get(Lanche_escolhido, 0.00)

def Cardapio_Bebidas():
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
    Valores = {"refri": 5.00, "suco": 5.50, "cerveja": 6.00}
    return Valores.get(Bebida_escolhida, 0.00)

# ---------------------------------------------------------
# REGRAS DE NEGÓCIO E VALIDAÇÕES
# ---------------------------------------------------------

def DetectorDidade(Idade):
    """Retorna um Booleano (True/False)."""
    return Idade >= 18

def calcular_Desconto(porcentagem):
    """
    Exemplo de 'Closure': Uma função que fabrica outra função.
    Útil para fixar uma taxa de desconto e reutilizá-la depois.
    """
    def aplicar(valor_total):
        return valor_total * porcentagem
    return aplicar

# Criando as instâncias de desconto (80% do valor e 90% do valor)
desconto_membro_clube = calcular_Desconto(0.8)
desconto_membro_comum = calcular_Desconto(0.9)

def exibir_relatorio():
    """Processa e exibe os dados acumulados durante a execução."""
    print("\n" + Criar_Linhas("="))
    print("       RELATÓRIO DO DIA")
    print(Criar_Linhas("="))
    
    # sum() percorre a lista historico_faturamento e soma tudo
    total = sum(historico_faturamento)
    print(f"Faturamento total: {Conversor_Valor(total, 'R$')}")
    print(f"Total de vendas:   {len(historico_faturamento)}")
    
    print(Criar_Linhas("="))
    print("-----RANK-----")
    
    # ORDENAÇÃO: sorted() transforma o dicionário em uma lista de tuplas ordenada.
    # key=lambda item: item[1] diz para ordenar pelo VALOR (gasto), não pela CHAVE (nome).
    # reverse=True coloca do maior para o menor.
    rankcliente = sorted(rank_gastos.items(), key=lambda item: item[1], reverse=True)
    
    # len() no dicionário conta quantos Nomes únicos existem.
    QuantCliente = len(rank_gastos)
    print(f"Quantidade de Clientes Únicos: {QuantCliente}")
    
    # Desempacotamento de Tuplas (cliente, gasto) vindo da lista ordenada
    for cliente, gasto in rankcliente:
        print(f"Cliente: {cliente.capitalize()}  | Total: {Conversor_Valor(gasto, 'R$')}")
        
    print(Criar_Linhas("="))   

# ---------------------------------------------------------
# FLUXO PRINCIPAL DO SISTEMA
# ---------------------------------------------------------

def main():
    print ("""
    █▀█ █▀▀ █▄░█ ▄▀█ ▀█▀ ▄▀█ █▀█   █░░ ▄▀█ █▄░█ █▀▀ █░█ █▀▀ █▀
    █▀▄ ██▄ █░▀█ █▀█ ░█░ █▀█ █▄█   █▄▄ █▀█ █░▀█ █▄▄ █▀█ ██▄ ▄█""")
    
    Nome = input("\nQual seu Nome? ")
    membro = input("\nVocê é um membro do clube? (s/n) ")
    
    # TRATAMENTO DE ERROS: Garante que o programa não trave se o usuário digitar letras na idade.
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

    # --- LANCHES ---
    os.system("cls" if os.name == "nt" else "clear")
    Cardapio_Lanches()
    total_lanches = 0.00
    lanches_pedidos = []
    
    while True:
        lanche = input("Qual lanche você gostaria de pedir? ").lower().strip()
        preco_atual = Preco_Lanches(lanche)
        
        if preco_atual > 0:
            total_lanches += preco_atual
            lanches_pedidos.append(lanche.capitalize())
            print(f"Adicionado! Subtotal lanches: {Conversor_Valor(total_lanches, 'R$')}")
        else: 
            print("Lanche inválido!")

        if input("Deseja pedir outro lanche? (s/n): ").lower().strip() == "n":
            break
            
    # .join() transforma a lista ['Pizza', 'Suco'] em uma string "Pizza, Suco"
    lanche_final = ", ".join(lanches_pedidos) if lanches_pedidos else "Nenhum"          

    # --- BEBIDAS ---
    bebidas_pedidas = []
    preco_total_bebidas = 0.00
    if input("Você gostaria de adicionar uma bebida? (s/n) ").lower().strip() == "s":
        os.system("cls" if os.name == "nt" else "clear")
        Cardapio_Bebidas()
        while True:
            item_b = input("Qual bebida você gostaria? ").lower().strip()
            valor_b = Preco_Bebidas(item_b)
            
            # Validação lógica para restrição de idade
            if item_b == "cerveja" and not DetectorDidade(idade):
                print("🚫 Venda proibida para menores!")
            elif valor_b > 0:
                preco_total_bebidas += valor_b
                bebidas_pedidas.append(item_b.capitalize())
                print(f"Adicionado! Subtotal bebidas: {Conversor_Valor(preco_total_bebidas, 'R$')}")
            else:
                print("Bebida não encontrada!")
                
            if input("Deseja pedir outra bebida? (s/n): ").lower().strip() == "n":
                break
    
    bebida_final = ", ".join(bebidas_pedidas) if bebidas_pedidas else "Nenhuma"
      
    # --- LOGÍSTICA ---
    while True:
        try:
            distancia = float(input("Distância para entrega (km): "))
            if distancia >= 0: break
            print("Distância inválida!")
        except ValueError:
            print("Digite apenas números!")

    clima = input("Clima (ensolarado/chuvoso/nublado): ").lower().strip()

    # Estrutura de decisão para frete
    if distancia <= 5: taxa = 5.00
    elif distancia <= 10: taxa = 8.00
    else: taxa = 10.00
            
    # OPERADOR TERNÁRIO: Forma compacta de IF/ELSE para atribuição simples
    taxa += 2.00 if clima == "chuvoso" else 0.00
    msg_clima = " (taxa de chuva aplicada)" if clima == "chuvoso" else ""
    
    # --- FECHAMENTO ---
    subtotal = total_lanches + preco_total_bebidas + taxa
    
    # Lógica de Desconto (Corrigida para checar 's')
    if membro.lower().strip() == "s":
        total_final = desconto_membro_clube(subtotal)
    else:
        total_final = desconto_membro_comum(subtotal)    

    # --- RECIBO ---
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + Criar_Linhas("="))
    print("         RECIBO DE COMPRA")
    print(Criar_Linhas("="))
    print(f"Itens: {lanche_final} | Valor Lanches: {Conversor_Valor(total_lanches, 'R$')}")
    print(f"Bebidas: {bebida_final} | Valor Bebidas: {Conversor_Valor(preco_total_bebidas, 'R$')}")
    print(f"Entrega:  {Conversor_Valor(taxa, 'R$')}{msg_clima}")
    print(Criar_Linhas("-"))
    print(f"TOTAL A PAGAR: {Conversor_Valor(total_final, 'R$')}")
    print(Criar_Linhas("="))
    print(Despedidas(Nome))
    
    # ATUALIZAÇÃO DO RANKING (Lógica de Acúmulo no Dicionário)
    historico_faturamento.append(total_final)
    if Nome in rank_gastos:
        rank_gastos[Nome] += total_final # Soma se já existe
    else:
        rank_gastos[Nome] = total_final  # Cria se for novo

# ---------------------------------------------------------
# EXECUÇÃO DO PROGRAMA
# ---------------------------------------------------------
if __name__ == "__main__":
    while True:
        main()
        if input("\nRegistrar novo cliente? (s/n) " ).lower().strip() == "n":
            break
    
    # Limpa a tela e mostra o resumo final antes de fechar
    os.system("cls" if os.name == "nt" else "clear")
    exibir_relatorio()
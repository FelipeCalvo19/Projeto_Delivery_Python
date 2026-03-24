# =============================================================================
# SISTEMA DE DELIVERY - VERSÃO 2.0 (ESTUDO DE ESTRUTURAS DE DADOS)
# Objetivo: Praticar Listas, Dicionários, Tratamento de Erros e Operadores Ternários.
# =============================================================================
import os
from datetime import datetime
from utils import saudaçao_horario
from utils import Boas_vindas
from utils import Despedidas
from utils import Criar_Linhas
from utils import Conversor_Valor
from utils import calcular_Desconto
from utils import DetectorDidade
from utils import exibir_relatorio
from models.bebida import Cardapio_Bebidas
from models.lanche import Cardapio

historico_faturamento = [] 
rank_gastos = {}


# Criando as instâncias de desconto (80% do valor e 90% do valor)
desconto_membro_clube = calcular_Desconto(0.8)
desconto_membro_comum = calcular_Desconto(0.9)
 

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
    exibir_relatorio(historico_faturamento, rank_gastos)
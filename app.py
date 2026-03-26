# =============================================================================
# SISTEMA DE DELIVERY 
# =============================================================================

#Imports

import os
from utils import calcular_desconto, detector_de_idade, exibir_relatorio
from views import boas_vindas, saudaçao_horario, criar_linhas, conversor_valor, despedidas
from dados_temp import lanches, bebidas
from services import busca_preco, exibir_itens

historico_faturamento = [] 
rank_gastos = {}


# Criando as instâncias de desconto (80% do valor e 90% do valor)
desconto_membro_clube = calcular_desconto(0.8)
desconto_membro_comum = calcular_desconto(0.9)
 


# FLUXO PRINCIPAL DO SISTEMA


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

    print(boas_vindas(Nome))

    if input("Voce deseja fazer um pedido? (s/n) ").lower().strip() == "n":
        print("Entendido, se precisar de algo é só chamar!")
        return

    # --- LANCHES ---
    os.system("cls" if os.name == "nt" else "clear")
    exibir_itens(lanches)
    total_lanches = 0.00
    lanches_pedidos = []
    
    while True:
        lanche = input("Qual lanche você gostaria de pedir? ").lower().strip()
        preco_atual = busca_preco(lanche, lanches)
        
        if preco_atual > 0:
            total_lanches += preco_atual
            lanches_pedidos.append(lanche.capitalize())
            print(f"Adicionado! Subtotal lanches: {conversor_valor(total_lanches, 'R$')}")
        else: 
            print("Lanche inválido!")

        if input("Deseja pedir outro lanche? (s/n): ").lower().strip() == "n":
            break
            
    lanche_final = ", ".join(lanches_pedidos) if lanches_pedidos else "Nenhum"          

    # --- BEBIDAS ---
    bebidas_pedidas = []
    preco_total_bebidas = 0.00
    if input("Você gostaria de adicionar uma bebida? (s/n) ").lower().strip() == "s":
        os.system("cls" if os.name == "nt" else "clear")
        exibir_itens(bebidas)
        while True:
            item_b = input("Qual bebida você gostaria? ").lower().strip()
            valor_b = busca_preco(item_b, bebidas)
            
            # Validação lógica para restrição de idade
            if item_b == "cerveja" and not detector_de_idade(idade):
                print("🚫 Venda proibida para menores!")
            elif valor_b > 0:
                preco_total_bebidas += valor_b
                bebidas_pedidas.append(item_b.capitalize())
                print(f"Adicionado! Subtotal bebidas: {conversor_valor(preco_total_bebidas, 'R$')}")
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
            
    taxa += 2.00 if clima == "chuvoso" else 0.00
    msg_clima = " (taxa de chuva aplicada)" if clima == "chuvoso" else ""
    
    # --- FECHAMENTO ---
    subtotal = total_lanches + preco_total_bebidas + taxa
    
    # Lógica de Desconto
    if membro.lower().strip() == "s":
        total_final = desconto_membro_clube(subtotal)
    else:
        total_final = desconto_membro_comum(subtotal)    

    # --- RECIBO ---
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + criar_linhas("="))
    print("         RECIBO DE COMPRA")
    print(criar_linhas("="))
    print(f"Itens: {lanche_final} | Valor Lanches: {conversor_valor(total_lanches, 'R$')}")
    print(f"Bebidas: {bebida_final} | Valor Bebidas: {conversor_valor(preco_total_bebidas, 'R$')}")
    print(f"Entrega:  {conversor_valor(taxa, 'R$')}{msg_clima}")
    print(criar_linhas("-"))
    print(f"TOTAL A PAGAR: {conversor_valor(total_final, 'R$')}")
    print(criar_linhas("="))
    print(despedidas(Nome))
    
    # ATUALIZAÇÃO DO RANKING 
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
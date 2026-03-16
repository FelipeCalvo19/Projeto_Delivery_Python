# Sistema de Delivery: Calcula preço do lanche + taxa de entrega dinâmica
# Desenvolvido para praticar condicionais aninhadas e validação de dados
import os

# Função que cria a saudação usando o nome do usuário
def Boas_vindas(Nome):
    saudacao = f"Oi {Nome}, tudo bem?"
    return saudacao

# Função que cria a mensagem de despedida
def Despedidas(Nome):
    adeus = f"Obrigado por pedir conosco {Nome}! Tenha um ótimo dia!"
    return adeus

# Função que define o preço do lanche com base no texto digitado
def Preco_lanche(nome_do_lanche):
    if nome_do_lanche == "hambúrguer":
        return 15.00
    elif nome_do_lanche == "pizza":
        return 25.00
    elif nome_do_lanche == "salada":
        return 10.00
    else:
        return 0.00

# Função que define o preço da bebida
def Preco_Bebidas(nome_da_bebida):
    if nome_da_bebida == "refri":
        return 5.00
    elif nome_da_bebida =="suco":
        return 5.50
    elif nome_da_bebida =="cerveja":
        return 7.00
    else:
        return 0.00

# Função que verifica se é maior de idade (retorna True ou False)
def DetectorDidade(Idade):
    if Idade >= 18:
        return True
    else:
        return False

# Função que calcula 10% de desconto
def calcular_Desconto(valortotal):
   desconto = valortotal * 0.9
   return desconto

# Função que gera uma linha visual multiplicando o caractere por 30
def Criar_Linhas(Divisor):
   QtdLinhas = Divisor * 30
   return QtdLinhas

# Função que formata o valor para exibir com duas casas decimais e o símbolo R$
def Conversor_Valor(Valor,cifra):
   Simbolo = f"{cifra}{Valor:.2f}"
   return Simbolo

def main ():
    # Arte ASCII do título
    print ("""
    █▀█ █▀▀ █▄░█ ▄▀█ ▀█▀ ▄▀█ █▀█   █░░ ▄▀█ █▄░█ █▀▀ █░█ █▀▀ █▀
    █▀▄ ██▄ █░▀█ █▀█ ░█░ █▀█ █▄█   █▄▄ █▀█ █░▀█ █▄▄ █▀█ ██▄ ▄█""")
    
    Nome = input("\nQual seu Nome?")
    
    # --- VALIDAÇÃO DE IDADE ---
    # O loop 'while True' repete a pergunta até que um valor válido seja digitado
    while True:
        try:
            idade = int (input ("Quantos Anos voce tem?"))
            # Verifica se a idade faz sentido (regra de negócio)
            if idade <=0 or idade >=100 :
                print("Digite uma Idade Valida!! (0 a 100)")
                continue # Volta para o início do while
            break # Sai do loop se o número for válido e inteiro
        except ValueError:
            # Captura erro caso o usuário digite letras onde se espera um número (int)
            print("Error! Digite apenas números.")

    print(Boas_vindas(Nome))

    pedido = input("Voce deseja fazer um pedido? (s/n)") 
    # Se o usuário digitar 'n', o programa encerra a parte do pedido
    if pedido.lower().strip() == "n":
        print ("Entendido, se precisar de algo é só chamar!")
    else:

        # ---SELEÇÃO DO LANCHE---
        lanche = input("Qual lanche você gostaria de pedir? (hambúrguer, pizza, salada)").lower().strip()
        preco = Preco_lanche(lanche)

        # Validação: se o preço for 0, o lanche digitado não existe na função Preco_lanche
        if preco == 0.00:
            print("Lanche inválido. Por favor, escolha entre hambúrguer, pizza ou salada.")
        else:   
            print(f"Otima escolha! O preço do seu lanche é {Conversor_Valor(preco, 'R$')}")

        precoB = 0.00
        pedidoB = input("Você gostaria de Adicionar uma bebida?(s/n)")
        
        # ---SELEÇÃO DE BEBIDA---
        bebida = "nenhuma"
        if pedidoB == "s".lower().strip():
            bebida = input("Qual Bebida voce gostaria?(refri, suco , cerveja)").lower().strip()
            precoB = Preco_Bebidas(bebida)
            
            # Verifica se é cerveja e se o usuário tem idade para beber
            if bebida == "cerveja" and not (DetectorDidade(idade)):
                print("voce nao tem idade para beber!!")
                precoB = 0.00
                
            elif precoB == 0.00:
                print("Não temos essa bebida!!")
            else:
                print(f"Otima escolha! o preco da sua bebida é {Conversor_Valor(precoB, 'R$')}")
                    
        # ---CÁLCULO DA TAXA DE ENTREGA---
        # Outro loop de validação, agora para números decimais (float)
        while True:
            try:
                distancia = float(input ("você mora a quantos km do local de entrega?"))
                # Garante que a distância não seja negativa
                if distancia < 0:
                    print("Distância inválida. Por favor, insira um valor positivo.")
                    continue
                break # Distância válida, encerra o loop
            except ValueError:
                # Captura erro se o usuário digitar letras no campo de km
                print("Digite Apenas Números!!!")
        
        # Coleta a informação do clima para o cálculo da taxa
        clima = input("Como está o clima hoje? (ensolarado, chuvoso, nublado)").lower().strip()

        # Define a taxa baseada na distância
        if distancia <= 5:
            taxa = 5.00
        elif distancia <= 10:
            taxa = 8.00
        else:
            taxa = 10.00
            
        # Adicional de R$ 2.00 se o clima estiver chuvoso
        if clima == "chuvoso":
                taxa += 2.00
                msg = " (incluindo taxa adicional por clima chuvoso)"
        else:
                msg = ""
        
        # Soma todos os valores para chegar no total
        valortotal = preco + precoB + taxa
        valortotal2 = preco + precoB + taxa # Cópia do valor para mostrar o subtotal antes do desconto
                 
        # ---APLICAÇÃO DE DESCONTO---
        # Se o pedido passar de R$ 40.00, aplica 10% de desconto
        if valortotal >= 40:
                valortotal = calcular_Desconto(valortotal)
                msgD = " Parabens! Voce ganhou um Desconto de 10% Aproveite!"
        else:
                msgD = ""   
        
        # Limpa o terminal antes de mostrar o recibo final
        os.system("cls" if os.name == "nt" else "clear")
        
        # --- RESUMO DO PEDIDO (RECIBO) ---
        print("\n" + Criar_Linhas("="))
        print("        RECIBO DE COMPRA")
        print(Criar_Linhas("="))
        print(f"Lanche:   {lanche.capitalize()} {Conversor_Valor(preco, 'R$')} ")
        print(f"Bebida:   {bebida. capitalize()} {Conversor_Valor(precoB, 'R$')}")
        print(f"Entrega:  {Conversor_Valor(taxa, 'R$')}{msg}")
        print(Criar_Linhas("-"))

        # Mostra o valor sem o desconto primeiro
        print(f"SUBTOTAL: {Conversor_Valor(valortotal2, 'R$')}")

        # Se houve desconto, mostra quanto foi economizado
        if valortotal < valortotal2: 
            economia = valortotal2 - valortotal
            print(f"DESCONTO: {Conversor_Valor(economia, 'R$')} (10% OFF)")
            print(f"TOTAL A PAGAR: {Conversor_Valor(valortotal, 'R$')}")
            print(msgD)
        else:
            print(f"TOTAL A PAGAR: {Conversor_Valor(valortotal, 'R$')}")

        print(Criar_Linhas("="))
        print(Despedidas(Nome))
        print(Criar_Linhas("="))

# Início do programa
if __name__ == "__main__":
    main()
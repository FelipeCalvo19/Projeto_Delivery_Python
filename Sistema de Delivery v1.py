# Sistema de Delivery: Calcula preço do lanche + taxa de entrega dinâmica
# Desenvolvido para praticar condicionais aninhadas e validação de dados
def Boas_vindas(Nome):
    saudacao = f"Oi {Nome}, tudo bem?"
    return saudacao

def Despedidas(Nome):
    adeus = f"Obrigado por pedir conosco {Nome}! Tenha um ótimo dia!"
    return adeus

def Preco_lanche(nome_do_lanche):
    if nome_do_lanche == "hambúrguer":
        return 15.00
    elif nome_do_lanche == "pizza":
        return 25.00
    elif nome_do_lanche == "salada":
        return 10.00
    else:
        return 0.00

def Preco_Bebidas(nome_da_bebida):
    if nome_da_bebida == "refri":
        return 5.00
    elif nome_da_bebida =="suco":
        return 5.50
    elif nome_da_bebida =="cerveja":
        return 7.00
    else:
        return 0.00

def DetectorDidade(Idade):
    if Idade >= 18:
        return True
    else:
        return False

def calcular_Desconto(valortotal):
   desconto = valortotal * 0.9
   return desconto

def Criar_Linhas(Divisor):
   QtdLinhas = Divisor * 30
   return QtdLinhas

def Conversor_Valor(Valor,cifra):
   Simbolo = f"{cifra}{Valor:.2f}"
   return Simbolo


Nome = input("Qual seu Nome?")
idade = int (input ("Quantos Anos voce tem?"))

print(Boas_vindas(Nome))

pedido = input("Voce deseja fazer um pedido? (s/n)") 
if pedido.lower().strip() == "n":
    print ("Entendido, se precisar de algo é só chamar!")
else:

   # ---SELEÇÃO DO LANCHE---
    lanche = input("Qual lanche você gostaria de pedir? (hambúrguer, pizza, salada)").lower().strip()
    preco = Preco_lanche(lanche)

# o codigo so continua se o lanche for válido, caso contrário, exibe mensagem de erro
    if preco == 0.00:
      print("Lanche inválido. Por favor, escolha entre hambúrguer, pizza ou salada.")
    else:   
      print(f"Otima escolha! O preço do seu lanche é {Conversor_Valor(preco, 'R$')}")

      precoB = 0.00
      pedidoB = input("Você gostaria de Adicionar uma bebida?(s/n)")
      
         # ---SELEÇÃO DE BEBIDA---
      if pedidoB == "s".lower().strip():
          bebida = input("Qual Bebida voce gostaria?(refri, suco , cerveja)").lower().strip()
          precoB = Preco_Bebidas(bebida)
          if bebida == "cerveja" and not (DetectorDidade(idade)):
              print("voce nao tem idade para beber!!")
              precoB = 0.00
              
          elif precoB == 0.00:
              print("Não temos essa bebida!!")
          else:
              print(f"Otima escolha! o preco da sua bebida é {Conversor_Valor(precoB, 'R$')}")
                   
      # ---CÁLCULO DA TAXA DE ENTREGA---
      distancia = float(input ("você mora a quantos km do local de entrega?"))
         
         #implementação de validação para distância negativa
      if distancia < 0:
            print("Distância inválida. Por favor, insira um valor positivo.")
      else:
         clima = input("Como está o clima hoje? (ensolarado, chuvoso, nublado)").lower().strip()

         #taxa de entrega baseada na distância e clima usando condicionais aninhadas
         if distancia <= 5:
               taxa = 5.00
         elif distancia <= 10:
               taxa = 8.00
         else:
               taxa = 10.00
               #adicional de taxa para clima chuvoso
         if clima == "chuvoso":
                  taxa += 2.00
                  msg = " (incluindo taxa adicional por clima chuvoso)"
         else:
                  msg = ""
         valortotal = preco + precoB + taxa
         valortotal2 = preco + precoB + taxa         
            #---APLICAÇÃO DE DESCONTO---
         if valortotal >= 40:
                  valortotal = calcular_Desconto(valortotal)
                  msgD = " Parabens! Voce ganhou um Desconto de 10% Aproveite!"
         else:
                  msgD = ""   
            
         # --- RESUMO DO PEDIDO ---
         print("\n" + Criar_Linhas("="))
         print("        RECIBO DE COMPRA")
         print(Criar_Linhas("="))
         print(f"Lanche:   {lanche.capitalize()}")
         print(f"Bebida:   {Conversor_Valor(precoB, 'R$')}")
         print(f"Entrega:  {Conversor_Valor(taxa, 'R$')}{msg}")
         print(Criar_Linhas("-"))

         # Mostra o Subtotal (o valortotal2 que você criou)
         print(f"SUBTOTAL: {Conversor_Valor(valortotal2, 'R$')}")

         if valortotal < valortotal2: # Se o valor com desconto for menor que o original
            economia = valortotal2 - valortotal
            print(f"DESCONTO: {Conversor_Valor(economia, 'R$')} (10% OFF)")
            print(f"TOTAL A PAGAR: {Conversor_Valor(valortotal, 'R$')}")
            print(msgD)
         else:
            print(f"TOTAL A PAGAR: {Conversor_Valor(valortotal, 'R$')}")

         print(Criar_Linhas("="))
         print(Despedidas(Nome))
         print(Criar_Linhas("="))
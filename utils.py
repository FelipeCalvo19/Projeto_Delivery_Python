from datetime import datetime

horas = datetime.now().hour

def saudaçao_horario (Horas):
    horario = datetime.now().hour
    momento = "nenhum"
    if 6 <= horario < 12:
        momento = "Dia"
    elif 12 <= horario < 18:
        momento = "Tarde"
    elif 19 <= horario < 23:
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


def exibir_relatorio(historico_faturamento, rank_gastos):
    """Processa e exibe os dados acumulados durante a execução."""
    print("\n" + Criar_Linhas("="))
    print("       RELATÓRIO DO DIA")
    print(Criar_Linhas("="))
    
    
    total = sum(historico_faturamento)
    print(f"Faturamento total: {Conversor_Valor(total, 'R$')}")
    print(f"Total de vendas:   {len(historico_faturamento)}")
    
    print(Criar_Linhas("="))
    print("-----RANK-----")
    
  
    rankcliente = sorted(rank_gastos.items(), key=lambda item: item[1], reverse=True)
    
    
    QuantCliente = len(rank_gastos)
    print(f"Quantidade de Clientes Únicos: {QuantCliente}")
    
    for cliente, gasto in rankcliente:
        print(f"Cliente: {cliente.capitalize()}  | Total: {Conversor_Valor(gasto, 'R$')}")
        
    print(Criar_Linhas("="))   
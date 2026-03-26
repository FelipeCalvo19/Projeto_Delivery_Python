from views import criar_linhas, conversor_valor

def detector_de_idade(Idade):
    """Retorna um Booleano (True/False)."""
    return Idade >= 18

def calcular_desconto(porcentagem):
    """
    Exemplo de 'Closure': Uma função que fabrica outra função.
    Útil para fixar uma taxa de desconto e reutilizá-la depois.
    """
    def aplicar(valor_total):
        return valor_total * porcentagem
    return aplicar


def exibir_relatorio(historico_faturamento, rank_gastos):
    """Processa e exibe os dados acumulados durante a execução."""
    print("\n" + criar_linhas("="))
    print("       RELATÓRIO DO DIA")
    print(criar_linhas("="))
    
    
    total = sum(historico_faturamento)
    print(f"Faturamento total: {conversor_valor(total, 'R$')}")
    print(f"Total de vendas:   {len(historico_faturamento)}")
    
    print(criar_linhas("="))
    print("-----RANK-----")
    
  
    rankcliente = sorted(rank_gastos.items(), key=lambda item: item[1], reverse=True)
    
    
    QuantCliente = len(rank_gastos)
    print(f"Quantidade de Clientes Únicos: {QuantCliente}")
    
    for cliente, gasto in rankcliente:
        print(f"Cliente: {cliente.capitalize()}  | Total: {conversor_valor(gasto, 'R$')}")
        
    print(criar_linhas("="))   



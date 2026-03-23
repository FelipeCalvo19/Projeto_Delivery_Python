from utils import Criar_Linhas
from utils import Conversor_Valor


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
    
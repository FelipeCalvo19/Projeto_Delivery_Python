from utils import Conversor_Valor

class Cardapio:
    lanches = []

    def __init__(self, nome = "", tipo = "", ingredientes = "", preco = 0.0):
        self._nome = nome
        self._tipo = tipo
        self._ingredientes = ingredientes
        self._preco = preco

    def __str__(self):
        return f"{self._nome} | {self._tipo} | {self._ingredientes} | {self._preco}"
    
    @classmethod
    def mostra_cardapio(cls):
        preco_formatado = Conversor_Valor(Cardapio._preco, 'R$')
        print(f"{"Nome do Lanche".ljust(25)} | {"Tipo do Lanche".ljust(25)} | {"Preço"}")
        for lanche in cls.lanches:
            print(f"{Cardapio._nome.ljust(25)} | {Cardapio._tipo.ljust(25)} | {preco_formatado}")

    @classmethod
    def adicionar_lanche(cls):
        nome_lanche = input("Qual o nome do lanche? ")
        tipo_lanche = input("Qual o tipo do lanche? ")
        ingredientes_lanche = input("Qual os ingredientes do lanche? ")
        preco_lanche = float(input("Qual o preco do lanche? "))
        
        novo_lanche = cls(nome_lanche, tipo_lanche, ingredientes_lanche, preco_lanche)
        cls.lanches.append(novo_lanche)

        print(f"Lanche Adicionado com sucesso!!")

    @property
    def busca_precos(self):
        return round(self._preco, 2)

    @busca_precos.setter
    def busca_precos(self, valor_alterado):

        if not isinstance (valor_alterado, (int, float)):
            print(f"Erro!! o valor {valor_alterado} não pode ser contabilizado")
            return
        
    
        self._preco = valor_alterado 
        print("O preço foi alterado com sucesso!!") if valor_alterado > 0 else "O preço dever ser maior quer zero!!"
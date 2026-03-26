from models.cardapio import Cardapio

class Lanches(Cardapio):
    lista_lanches = []

    def __init__(self, nome = "", tipo = "", ingredientes = "", preco = 0.0):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._ingredientes = ingredientes


    def __str__(self):
        return f"{self._nome} | {self._tipo} | {self._ingredientes} | {self._preco}"
    
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
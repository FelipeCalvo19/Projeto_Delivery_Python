from models.cardapio import Cardapio

class Bebidas(Cardapio):
    lista_bebidas = []
    
    def __init__(self, nome = "", tamanho = "", preco = 0.0, alcoólica = False):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._alcoólica = alcoólica

    def __str__(self):
        return f"{self._nome} | {self._tamanho} | {self._preco} | {self._alcoólica}"

    @property    
    def alcoólicas(self):
        return "✅" if self._alcoólica else "❌"
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
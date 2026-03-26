

class Cardapio:
    cardapio = []
    def __init__(self, nome = "", preco = 0.0):
        self._nome = nome
        self. _preco = preco
    def __str__(self):
        return f"Nome: {self._nome} | preco: {self._preco}"
    
    @classmethod
    def adicionar_item(cls, item):
        if isinstance(item, Cardapio):
            Cardapio.cardapio.append(item)

    # def exibir_cardapio(self):
    #     for i,item in enumerate(self._itens, start= 1):
    #         if hasattr(item,"tipo"):
    #             mensagem_lanche = f"{i}. Nome: {item._nome} | Tipo: {item._tipo} | Preço: {item._preco}"
    #             print(mensagem_lanche)
    #         return f"{i}. Nome: {item._nome} | Tamanho: {item._tamanho} | Preço: {item._preco}"    


        

        
        
    

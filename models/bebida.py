from utils import Conversor_Valor

class Cardapio_Bebidas:
    bebidas = []

    def __init__(self, nome = "", tamanho = "", preco = 0.0, alcoólica = False):
        self._nome = nome
        self._tamanho = tamanho
        self._preco = preco
        self._alcoólica = alcoólica

    def __str__(self):
        return f"{self._nome} | {self._tamanho} | {self._preco} | {self._alcoólica}"

    @property    
    def alcoólicas(self):
        return "✅" if self._alcoólica else "❌"

    @classmethod
    def exibir(cls):
        valor_convertido = Conversor_Valor(Cardapio_Bebidas._preco, 'R$')
        tamanho_convertido = Conversor_Valor(Cardapio_Bebidas._tamanho, 'ml')
        print(f"{"Bebida".ljust(25)} | {"Tamanho".ljust(25)} | {"Preço".ljust(25)} | {"Alcoólica"}")
        for bebida in Cardapio_Bebidas.bebidas:
            print(f"{Cardapio_Bebidas._nome.ljust(25)} | {tamanho_convertido.ljust(25)} | {valor_convertido.ljust(25)} | {Cardapio_Bebidas._alcoólica}")

    @classmethod
    def adicionar_bebida(cls):
        nome_bebida = input("Qual nome da bebida? ")
        tamanho_bebida = int(input("Quantos ml tem a bebida? "))
        preco_bebida = float(input("Qual o preço da bebida? "))
        alcoólica = input("A bebida é a alcoólica? (s/n)").lower.strip()

        if alcoólica == "s":
            return True 
            
        nova_bebida = cls(nome_bebida, tamanho_bebida, preco_bebida, alcoólica)
        cls.bebidas.append(nova_bebida)
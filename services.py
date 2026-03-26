def exibir_itens(lista):
    for item in lista:
        print(item)


def busca_preco(nome, lista):
    for item in lista:
        if item._nome.lower().strip() == nome:
            return item.busca_precos
    return 0        


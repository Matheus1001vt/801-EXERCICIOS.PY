def lista_de_compras(pessoa, *args):
    print('Lista de compras de ' + pessoa)
    for item in args:
        print(item)


lista_de_compras('João', 'frango congelado', 'pães', 'sal de cozinha', 'leite')
lista_de_compras('Maria', 'sacos de lixo', 'frango')
lista_de_compras('Groger', 'cenouras', 'abacate')

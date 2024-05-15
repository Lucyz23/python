# # produtos = ['tv','celular','mouse','teclado','tablet']
# # print(produtos[1])

# # vendas = [1500, 1000, 350, 270, 900]
# # print(vendas[1])


# # produtos = ['tv','celular','mouse','teclado','tablet']
# # vendas = [1500, 1000, 350, 270, 900]

# # vendas[3] = 300

# # print('Vendas do produto {} foram de {} unidades'.format(produtos[3], vendas[3])) 

# #Quando quiser mudar o valor de algum objeto, antes do Print coloque a mudança que deseja. Nesse caso, mudou o valor do indice 3.

# # Adicionar e Remover itens de uma lista. 

# # Digamos que você está construindo o controle de produtos da Apple e a Appel lançou o Iphone 11 e irá tirar dos seus estoques o IphoneX

# # produtos = ['appleTv', 'mac', 'iphoneX', 'ipad', 'apple Watch', 'mac book', 'airpods']

# # # iphoneX_removido = produtos.pop(2)
# # # # produtos.remove('iphoneX')
# # # print(produtos)

# # produtos.append('iphone11')
# # print(produtos)


# # Use o if para verificar se o item que deseja retirar está na lista:
# produtos = ['appleTv', 'mac', 'iphoneX', 'ipad', 'apple Watch', 'mac book', 'airpods']
# produto_remover = 'iphone x'
# # if produto_remover in produtos:
# #     produtos.remove('iphone x')
# # else:
# #     print('{} nao existe na lista de produtos'.format(produto_remover))

# #  O try é voce tentar tirar da lista e caso nao esteja avisar:
# produtos = ['appleTv', 'mac', 'iphoneX', 'ipad', 'apple Watch', 'mac book', 'airpods']
# try:
#     produtos.remove('iphone x')
#     print(produtos)
# except:
#     print('{} nao existe na lista de produtos'.format(produto_remover))

#        TAMANHO DA LISTA

# Quantos produtos temos a venda

# produtos = ['appleTv', 'mac', 'iphoneX', 'ipad', 'apple Watch', 'mac book', 'airpods']

# tamanho = len(produtos)
# print('Temos {} produtos'.format(tamanho))

# MAIOR E MENOR VALOR

# vendas = [100, 1500, 15000, 270, 900, 100, 1200]

# # maior = max(vendas)
# # menor = min(vendas)
# # print('O maior item vendido é {} '.format(maior))
# # print('Menor item vendido é {} '.format(menor))

# mais_vendido = max(vendas)
# menos_vendido = min(vendas)
# # print('O maior item vendido é {} e o item menos vendido é {}'.format(mais_vendido, menos_vendido))

# i = vendas.index(mais_vendido)
# produto_mais_vendido = produtos[i]
# print(produto_mais_vendido)

# i = vendas.index(menos_vendido)
# produto_menos_vendido = produtos[i]
# print(produto_menos_vendido)

# produtos = ['appleTv', 'mac', 'iphoneX', 'ipad', 'apple Watch', 'mac book', 'airpods']
# novos_produtos = ['iphone 12', 'ioculos']
# lista_nova = produtos + novos_produtos
# print(lista_nova)

# acrescentando strings e numero numa lista
# lista = ['mac', 'iphone']
# lista = lista + ['Ipad']
# vendas = [100, 200]
# vendas = vendas + [500]

# print(lista, vendas)

# somando numeros na lista
# soma_vendas = 300
# soma_vendas = soma_vendas + 500
# print(soma_vendas)


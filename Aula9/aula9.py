precos = "Jan: 25, Fev: 27, Mar: 29"

preco_jan = precos[5:7] #[5:7] Voce vai dizer quais numeros voce quer que apareça, dizendo a posiçao dos numeros 
print(preco_jan)

preco_mar = precos[-2:] #O negativo é para contar de trás pra frente
print(preco_mar)

preco_fev = precos[-11: -9]
print(preco_fev)

# -----------------------------------------------//--------------------------------

# Posiçao Inicial e Final com step

codigo = "1.2.3.4,5,1,2.3.4,7.9"

pedaco_cod = codigo[2:10:2] #Pega o caracter do indice 2, até o caracter de indice 10, andando de 2 em 2.
# resultado: 2345. 
print(pedaco_cod)
faturamento = 2000
custo = 100
lucro = faturamento - custo

# print("O faturamento da loja foi" + " " + str(faturamento))
# print("O custo da loja foi" + " " + str(custo))
# print("O lucro da loja foi" + " " + str(lucro))

# .format é uma forma de concatenar um texto de uma forma mais organizada e limpa. Exemplo de como usar o .format logo abaixo: 
print("O faturamento da loja foi {}. O custo da loja foi {} e o lucro da loja foi {}".format(faturamento, custo, lucro))

# com f-string é uma outra forma de deixar organizado. Colocando o F antes da string, exemplo:

print(f"O faturamento da loja foi {faturamento} e o lucro da loja foi {lucro}")



# 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

# numero = int(input("Escreva um número "))

# print(f"O numero informado foi :{numero}")

# 3. Faça um Programa que peça dois números e imprima a soma.

# numeroOne = int(input("Digite um numero "))
# numeroTwo = int(input("Digite um numero "))

# soma = numeroOne + numeroTwo

# print(f"O resultado é {soma}")

# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

# notaOne = float(input("Digite a primeira nota bimestral :"))
# notaTwo = float(input("Digite a segunda nota bimestral :"))
# notaThree = float(input("Digite a terceira nota bimestral :"))
# notaFour = float(input("Digite a quarta nota bimestral :"))

# resultado = notaOne + notaTwo + notaThree + notaFour

# print(f"O resultado é {resultado}")

#### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

# metro = float(input("Digite o metro que deseja converter")) 

# conversor = metro * 100

# print(f"O valor convertido é : {conversor}")

#### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

# largura = float(input("Digite a largura: "))

# comprimento = float(input("Digite comprimento: "))

# resultado = largura * comprimento

# print(f"A area da sala é : {resultado}m²")

#### 7. Faça um Programa que: 

# pergunte quanto você ganha por hora 

# valorHora = float(input("Quanto você ganha/hora ?"))

# e o número de horas trabalhadas no mês.

# horasTrabalhadas = float(input("Horas trabalhadas no mês: "))

#  Calcule e mostre o total do seu salário no referido mês.

# print(f"Seu salário neste mês é {horasTrabalhadas / valorHora}")

#### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# temperaturaFahrenheit = float(input("Temperatura desejada em Fahrenheit: "))
# temperaturaCelsius = (temperaturaFahrenheit - 32) / 1.8

# print(f"Temperatura de Celsius é: {temperaturaCelsius: .2f}")

#### 9. Faça um Programa que:
#  peça a temperatura em graus Celsius, 
 
temperatuCelsius = float(input("Temperatura desejada em Celsius: "))
temperatuFarenheit = (temperatuCelsius * 1.8) + 32
# transforme e mostre em graus Fahrenheit.

print(f"Temperatura de Fahrenheit: {temperatuFarenheit: .2f}")



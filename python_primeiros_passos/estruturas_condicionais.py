#Com a prática dos exercícios a seguir obtive os seguintes conhecimentos:

#- Construir blocos condicionais com if, else e elif.
#- Diferenciar as estruturas condicionais.
#- Selecionar a estrutura condicional que melhor satisfaz o problema.
#- Utilizar diferentes operadores para construir expressões condicionais.

#1. Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))

if n1 > n2:
    print(f'O primeiro número ({n1}) é o maior.')
elif n2 > n1:
    print(f'O segundo número ({n2}) é o maior.')
else:
    print('Os dois números são iguais.')

#2. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

perc_cresc = (float(input('Insira o percentual de crescimento da empresa: ')))

if perc_cresc > 0:
    print('Houve um crescimento com porcentagem positiva no percentual de produção da empresa.')
elif perc_cresc < 0:
    print('Houve um decrescimento com porcentagem negativa')
else:
    print('Não houve crescimento ou decrescimento.')

#3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = input('Insira uma letra: ')

if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print(f'A letra escolhida ({letra}) é uma vogal.')
elif letra != 'a' or 'e' or 'i' or 'o' or 'u':
    print(f'A letra escolhida ({letra}) é uma consoante.')
else:
    print('Letra não reconhecida, tente novamente.')

#4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

a1 = float(input('Insira o preço do primeiro ano: '))
a2 = float(input('Insira o preço do segundo ano: '))
a3 = float(input('Insira o preço do terceiro ano: '))

mais_alto = a1

if a2 > a1:
    mais_alto = a2
if a3 > a1:
    mais_alto = a3

mais_baixo = a1

if a2 < a1:
    mais_baixo = a2
if a3 < a1:
    mais_baixo = a3

print(f'O valor mais baixo entre esses três anos foi de R${mais_baixo}')
print(f'O valor mais alto entre esses três anos foi de R${mais_alto}')

#5.  Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

p1 = input('Insira o preço do primeiro produto: ')
p2 = input('Insira o preço do segundo produto: ')
p3 = input('Insira o preço do terceiro produto: ')

if p1< p2 and p1 < p3:
    print('O primeiro produto é o mais barato.')
elif p2 < p1 and p2 < p3:
    print('O segundo produto é o mais barato.')
elif p3 < p1 and p3 < p2:
    print('O terceiro produto é o mais barato.')
else:
    if p1 == p2:
        print('O primeiro e segundo produto são os mais baratos.')
    elif p1 == p3:
        print('O primeiro e o segundo produto são os mais baratos.')
    elif p2 == p3:
        print('O segundo e terceiro produto são os mais baratos.')

#6. Escreva um programa que leia três números e os exiba em ordem decrescente.

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if (n1 >= n2) and (n1 >= n3):
    print(n1)
    if n2 >= n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif (n2 >= n1) and (n2 >= n3):
    print(n2)
    if n1 >= n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
else:
    print(n3)
    if n1 >= n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)

#7. Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = input('Em qual turno você estuda? (Escolha entre: manhã, tarde ou noite) ').lower()

if turno == 'manhã':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else:
    print('Valor inválido, tente novamente.')

#8. Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

n_inteiro = int(input('Insira um número inteiro: '))

if n_inteiro % 2 == 0:
    print(f'O número {n_inteiro} é par.')
else:
    print(f'O número {n_inteiro} é ímpar.')

#9. Podemos usar o operador de módulo % para determinar se um número é inteiro ou decimal. Se o operador de módulo % retornar zero da divisão inteira de um número por 1, então ele é inteiro. Se não for, ele é decimal.

n = float(input('Insira um número: '))

if n % 1 == 0:
    print(f'O número {n} é um número inteiro.')
else:
    print(f'O número {n} é um número decimal.')

#Momento dos projetos

#10. Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

n1 = (float(input('Insira o primeiro número: ')))
n2 = (float(input('Insira o segundo número: ')))

operacao = input('Qual operação você deseja utilizar? (Escolha entre: +, -, * ou /) ')

if operacao == '+':
    print('Resultado = ', n1 + n2)
elif operacao == '-':
    print('Resultado = ', n1 - n2)
elif operacao == '*':
    print('Resultado = ', n1 * n2)
elif operacao == '/':
    print('Resultado = ', n1 / n2)

#11. Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes.

l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    print('Os valores podem formar um triângulo.')
    if (l1 == l2) and (l2 == l3):
        print('O triângulo é equilátero.')
    elif (l1 != l2) and (l2 != l3) and (l1 != l3):
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isósceles.')
else:
    print('Os valores não podem formar um triângulo!')

#12. Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# - O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# - O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

combustivel = input('Insira qual o tipo de combustível desejado (gasolina, etanol ou diesel): ')
quantidade_litros = float(input('Insira a quantidade de litros desejada: '))

if combustivel == 'etanol':
    preco_litro = 1.70
    if quantidade_litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04

if combustivel == 'diesel':
    preco_litro = 2.00
    if quantidade_litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    print('Valores inválidos')
    preco_litro = 0
    desconto = 0

valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

print(f'O valor que deve ser pago pelo cliente é: R${valor_pago}')

#13. Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# - Para variação acima de 20%: bonificação para o time de vendas.
# - Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# - Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# - Para variação abaixo de -10%: corte de gastos.

venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

var_percentual = 100 * (venda_2023 - venda_2022) / venda_2022

if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')
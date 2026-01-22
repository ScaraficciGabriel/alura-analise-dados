#Com a prática dos exercícios a seguir obtive os seguintes conhecimentos:



#1. Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

qtd_compras = len(gastos)
total_gastos = sum(gastos)
media_gastos = total_gastos / qtd_compras
print(f'A média de gastos da empresa é de R${media_gastos}.')

#2. Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

total_compras = len(gastos)
contador_acima_3000 = 0
porcentagem_acima_3000 = 100 * (contador_acima_3000) / (total_compras)

if gastos > 3000:
    contador_acima_3000 += 1

print(f'Foram realizadas {contador_acima_3000} compras acima de R$3000.')
print(f'Quanto ao total de compras, houve um total de {porcentagem_acima_3000}% de compras acima de R$3000.')

#3. Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

lista_n = []

for i in range (0, 5):
    n = int(input('Insira um número inteiro: '))
    lista_n.append(n)

print(f'A lista de 5 números inteiros ficou da seguinte maneira: {lista_n}')

#4. Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista_n = []

for i in range (0, 5):
    n = int(input('Insira um número inteiro: '))
    lista_n.append(n)

print(f'A lista de 5 números inteiros invertida ficou da seguinte maneira: {lista_n[::-1]}')

#5. Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

numero = int(input('Digite um número inteiro: '))
lista_primos = []

for n in range(2, numero):

  primo = True

  for teste_divisiveis in range(2, n):
    if n % teste_divisiveis == 0:
      primo = False
      break
  if primo:
    lista_primos.append(n)

print(f'Lista de números primos: {lista_primos}')

#6. Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

# Coletamos a data
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2:
  if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    dias_fevereiro = 29
  else:
    dias_fevereiro = 28
  if dia >= 1 and dia <= dias_fevereiro:
    print('Data válida')
  else:
    print('Data inválida')
elif mes in [1, 3, 5, 7, 8, 10, 12]:
  if dia >= 1 and dia <= 31:
    print('Data válida')
  else:
    print('Data inválida')
elif mes in [4, 6, 9, 11]:
  if dia >= 1 and dia <= 30:
    print('Data válida')
  else:
    print('Data inválida')
else:
  print('Data inválida')

  #Momento dos projetos

  #7.  Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

  bac_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
  p_crescimento = []

  for i in range(1, len(bac_colonia)):
      porcentagem = 100 * (bac_colonia[i] - bac_colonia[i - 1]) / (bac_colonia[i - 1])
      p_crescimento.append(p_crescimento)

  print(f'Porcentagens de crescimento:\n{p_crescimento}')

#8. Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

ids = []
doce = 0
amargo = 0

for i in range(0,10):
  ids.append(int(input(f'Digite o {i+1}° ID: ')))

for id in ids:
  if id % 2 == 0:
    doce += 1
  else:
    amargo += 1

print(f'Quantidade de produtos doces: {doce}')
print(f'Quantidade de produtos amargos: {amargo}')

#9. Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

#Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

respostas = []
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0

for i in range(0, 10):
  respostas.append(input(f'Insira a resposta da questão {i + 1}: ').upper())

for i in range(0,10):
  if respostas[i] == gabarito[i]:
    nota += 1

print(f'Nota final: {nota}')

#10. Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

temperaturas_mensais = []
for i in range(0,12):
  temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

print('Temperaturas acima da média em: ')
for i in range(0,12):
  if temperaturas_mensais[i] > media_anual:
    print(meses[i])

#11. Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

#{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 #'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

#Escreva um código que calcule o total de vendas e o produto mais vendido.

dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total_vendas = 0
produto_mais_vendido = ''
unidades_produto_mais_vendido = 0

for produto in dados_vendas.keys():
  total_vendas += dados_vendas[produto]

  if dados_vendas[produto] > unidades_produto_mais_vendido:
    unidades_produto_mais_vendido = dados_vendas[produto]
    produto_mais_vendido = produto

print(f'Total de vendas é {total_vendas}')
print(f'{produto_mais_vendido} é o mais vendido')

#12. Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

# '''
# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos
# '''

# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}
total_votos = 0
vencedor = ''
voto_vencedor = 0


for design, voto_design in votos.items():
    total_votos += voto_design
    if voto_design > voto_vencedor:
        voto_vencedor = voto_design
        vencedor = design

porcentagem = 100 * (voto_vencedor) / (total_votos)

print(f'{vencedor} é o vencedor')
print(f'Porcentagem de votos: {porcentagem}%')

#13. As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

dic_abonos = {}
total_abono = 0
abonos_minimo = 0
maior_abono = 0

for salario in salarios:
  abono = salario * 0.1

  if abono < 200:
    abono = 200
  dic_abonos[salario] = abono

for abono in dic_abonos.values():
  if abono == 200:
    abonos_minimo += 1
  if abono > maior_abono:
    maior_abono = abono
  total_abono += abono

print(f'Abonos: {dic_abonos}')
print(f'Total de gasto com abonos: {total_abono}')
print(f'Número de funcionários que receberam o abono mínimo: {abonos_minimo}')
print(f'Maior valor de abono: {maior_abono}')


#14. Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

# {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}

# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().

dados = {'Área Norte': [2819, 7236],
         'Área Leste': [1440, 9492],
         'Área Sul': [5969, 7496],
         'Área Oeste': [14446, 49688],
         'Área Centro': [22558, 45148]}

soma_media = 0
maior_diversidade = ''
maior_soma = 0

for area, especies in dados.items():
  soma_especies = sum(especies)
  media = soma_especies / len(especies)
  print(f'A {area} tem a média de {media} espécies')
  if soma_especies > maior_soma:
      maior_soma = soma_especies
      maior_diversidade = area
  soma_media += media

media_total = soma_media / len(dados)

print(f'Média geral de espécies: {media_total}')
print(f'Área com a maior diversidade biológica: {maior_diversidade}')

#15. O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

# Especificamos os dados para um dicionário
dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

total_idades = 0

for setor, idades in dados.items():
  media_idade = sum(idades) / len(idades)
  print(f'O {setor} tem a média de {media_idade}')
  total_idades += sum(idades)

media_total = total_idades / (len(idades) * len(dados))
print(f'A média de idade geral é {media_total}')

acima_media = 0

for setor, idades in dados.items():
  for id in idades:
    if id > media_total:
      acima_media += 1
print(f'{acima_media} pessoas estão acima da idade média geral')
#Com a prática dos exercícios a seguir obtive os seguintes conhecimentos:

#- Criar variáveis
#- Distinguir diferentes tipos de dados
#- Realizar operações com variáveis numéricas
#- Manipular variáveis de texto (strings)
#- Coletar dados de uma pessoa usuária com input

#Coleta e amostra de dados

#1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

nome = input('Digite o seu nome: ')

print(f'Olá, {nome}!')

#2 Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

print(f'Olá, {nome}, você tem {idade} anos.')

#3 Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura (em metros): '))

print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!')

#Calculadora com operadores

#1. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

v1 = float(input('Insira o primeiro valor desejado: '))
v2 = float(input('Insira o segundo valor desejado: '))

soma = v1 + v2

print(f'A soma entre os dois valores escolhidos resulta em {soma}.')

#2. Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.

v1 = float(input('Insira o primeiro valor desejado: '))
v2 = float(input('Insira o segundo valor desejado: '))
v3 = float(input('Insira o terceiro valor desejado: '))

soma = v1 + v2 + v3

print(f'A soma entre os três valores escolhidos resulta em {soma}.')

#3. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

v1 = float(input('Insira o primeiro valor desejado: '))
v2 = float(input('Insira o segundo valor desejado: '))

subtracao = v1 - v2

print(f'A subtracao entre os dois valores escolhidos resulta em {subtracao}.')

#4. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.

v1 = float(input('Insira o primeiro valor desejado: '))
v2 = float(input('Insira o segundo valor desejado: '))

multiplicacao = v1 * v2

print(f'A mutiplicacao entre os dois valores escolhidos resulta em {multiplicacao}.')

#5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numerador = float(input('Insira o valor desejado para o denominador (o valor não pode ser 0): '))
denominador = float(input('Insira o valor desejado para o numerador: '))

divisao = numerador / denominador

print(f'A divisão entre o numerador e denominador escolhidos resulta em: {divisao}')

#6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

operador = float(input('Insira o valor desejado para o operador: '))
potencia = float(input('Insira o valor desejado para a potencia: '))

exponenciacao = operador**potencia

print(f'A exponenciação entre o operador e a potência escolhida resulta em {exponenciacao}')

#7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

v1 = float(input('Insira o numerador desejado: '))
v2 = float(input('Insira o denominador desejado (o valor não pode ser 0): '))

div_inteira = v1 // v2

print(f'A divisão inteira entre o numerador e denominador escolhidos resulta em {div_inteira}')

#8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

v1 = float(input('Insira o numerador desejado: '))
v2 = float(input('Insira o denominador desejado (o valor não pode ser 0): '))

resto_div = v1 % v2

print(f'O resto da divisão entre o numerador e denominador escolhidos resulta em {resto_div}')

#9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

n1 = float(input('Insira a primeira nota do estudante: '))
n2 = float(input('Insira a segunda nota do estudante: '))
n3 = float(input('Insira a terceira nota do estudante: '))

media = n1 + n2 + n3 / 3

print(f'A média resulta em {media}.')

#10. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

media_ponderada = ((5*1) + (12*2) + (20*3) + (15*4)) / (1 + 2 + 3 + 4)

print(f'A média ponderada entre os números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4 resulta emn{media_ponderada}.')

#Editando textos

#1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

frase = 'Praticando Python para dados.'
print(frase)

#2. Crie um código que solicite uma frase e depois imprima a frase na tela.

frase = input('Insira uma frase: ')

print(f'Frase escolhida: {frase} ')

#3. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

frase = 'Estudando dados'

print(frase.upper())

#4. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

frase = 'A prática leva à perfeição'

print(frase.lower())

#5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase = '   Eu gosto de estudar Python.   '

print(frase.strip())

#6. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

frase = input('Insira uma frase: ')

print(frase.strip())

#7. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

frase = input('Insira uma frase: ')

print(frase.strip().lower())

#8. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.

frase = input('Insira uma frase: ')

print(frase.replace('e', 'f'))

#9. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.

frase = input('Insira uma frase: ')

print(frase.replace('a', chr(64)))

#10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.

frase = input('Insira uma frase: ')

print(frase.replace('s', chr(36)))
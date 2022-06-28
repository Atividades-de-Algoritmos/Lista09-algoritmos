#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022

# 2 - Solicite ao usuário três valores inteiros, sendo o primeiro (a) e segundo (b) o intervalo que será
# usado para gerar valores aleatórios a partir da função randint(a,b), o terceiro (c) valor será o
# tamanho da lista.
# imprimir o maior, o menor, a lista em ordem crescente e decrescente, e conte a repetição do maior número.
#

# importando a biblioteca random para gerar números aleatórios entre um intervalo definido pelo usuário
from random import randint

# entrada de dados
# criando uma lista vazia
lista = []

a = int(input("informe o valor de A, no intervalor de -100 a 0: ")) # entrada do valor de A no intervalo de -100 a 0
b = int(input("informe o valor de B, no intervalor de 0 a 100: ")) # entrada do valor de B no intervalo de 0 a 100
c = int(input("informe o tamanho da lista (C): ")) # entrada do tamanho da lista
contador = 0 # inicialização do contador com 0 para que o contador não seja nulo ao iniciar o loop

# processamento de dados
# gerando números aleatórios entre o intervalo definido pelo usuário e adicionando na lista criada anteriormente
if not(((a < -100) and (a > 0)) and ((b <  0) and (b > 100))): # verifica se o intervalo definido pelo usuário é válido
  while contador < c: # enquanto o contador for menor que o tamanho da lista
    numeroSorteado = randint(a,b) # gera um número aleatório entre o intervalo definido pelo usuário
    lista.append(numeroSorteado) # adiciona o número aleatório na lista criada anteriormente
    contador = contador + 1 # incrementa o contador para que o loop continue
else:
  print("O intervalo definido pelo usuário não é válido!")

# saída de dados
# imprimindo o maior número da lista
print(f"O maior número da lista é: {max(lista)}")
# imprimindo o menor número da lista
print(f"O menor número da lista é: {min(lista)}")
# imprimindo a lista em ordem crescente
print(f"A lista em ordem crescente é: {sorted(lista)}")
# imprimindo a lista em ordem decrescente
print(f"A lista em ordem decrescente é: {sorted(lista, reverse=True)}")
# imprimindo o número de vezes que o maior número aparece na lista
print(f"O maior número '{max(lista)}' aparece {lista.count(max(lista))},  vezes na lista")
# imprimindo o número de vezes que o menor número aparece na lista
print(f"O menor número '{min(lista)}' aparece {lista.count(min(lista))},  vezes na lista")
# imprimindo a lista
print(f"A lista é: {lista}")

print("Fim do programa!")

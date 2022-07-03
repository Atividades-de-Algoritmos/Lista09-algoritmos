#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 02/07/2022

# 2 - Solicite ao usuário três valores inteiros, sendo o primeiro (a) e segundo (b) o intervalo que será
# usado para gerar valores aleatórios a partir da função randint(a,b), o terceiro (c) valor será o
# tamanho da lista.
# imprimir o maior, o menor, a lista em ordem crescente e decrescente, e conte a repetição do maior número.
#

# Importando a biblioteca random para gerar números aleatórios entre um intervalo definido pelo usuário
from random import randint

# Entrada de dados

lista = [] # Criando uma lista vazia

a = int(input("Informe o valor de A, no intervalor de -100 a 0: ")) # Entrada do valor de A no intervalo de -100 a 0
b = int(input("Informe o valor de B, no intervalor de 0 a 100: ")) # Entrada do valor de B no intervalo de 0 a 100
c = int(input("Informe o tamanho da lista (C): ")) # Entrada do tamanho da lista
contador = 0 # Inicialização do contador com 0 para que o contador não seja nulo ao iniciar o loop

# Processamento de dados

# Gerando números aleatórios entre o intervalo definido pelo usuário e adicionando na lista criada anteriormente

if not(((a < -100) and (a > 0)) and ((b <  0) and (b > 100))): # Verifica se o intervalo definido pelo usuário é válido
  
  while contador < c: # Enquanto o contador for menor que o tamanho da lista
    numeroSorteado = randint(a,b) # Gera um número aleatório entre o intervalo definido pelo usuário
    lista.append(numeroSorteado) # Adiciona o número aleatório na lista criada anteriormente
    contador = contador + 1 # Incrementa o contador para que o loop continue

else:
  print("O intervalo definido pelo usuário não é válido!")

# Saída de dados

print(f"O maior número da lista é: {max(lista)}") # Imprimindo o maior número da lista
print(f"O menor número da lista é: {min(lista)}") # Imprimindo o menor número da lista
print(f"A lista em ordem crescente é: {sorted(lista)}") # Imprimindo a lista em ordem crescente
print(f"A lista em ordem decrescente é: {sorted(lista, reverse=True)}") # Imprimindo a lista em ordem decrescente
print(f"O maior número '{max(lista)}' aparece {lista.count(max(lista))},  vezes na lista") # Imprimindo o número de vezes que o maior número aparece na lista
print(f"O menor número '{min(lista)}' aparece {lista.count(min(lista))},  vezes na lista") # Imprimindo o número de vezes que o menor número aparece na lista

print(f"A lista é: {lista}") # Imprimindo a lista

print("Fim do programa!") # Informando ao usuário que o programa terminou

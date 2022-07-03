#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 02/07/2022
#
#  1.	 Faça um programa que calcule em uma matriz 3x3 e escreva o valor das seguintes somas:
# a.	 da linha 2;
# b.	 da coluna 3;
# c.	 da diagonal principal;
# d.	 da diagonal secundária;
# e.	 acima da diagonal secundária;
# f.	 abaixo da diagonal secundária;
# g.	 acima da diagonal principal;
# h.	 abaixo da diagonal principal;
# i.	 de todos os elementos da matriz.
#
# +-----+-----+-----+-----+
# | i,j |  1  |  2  |  3  |
# +-----+-----+-----+-----+
# |   1 | 1,1 | 1,2 | 1,3 |
# |   2 | 2,1 | 2,2 | 2,3 |
# |   3 | 3,1 | 3,2 | 3,2 |
# +-----+-----+-----+-----+

# Ordem da matriz:
ordem = 3

# matriz m1
m1 = [[1,2,3], [4,5,6], [7,8,9]]

# ou
# obs: os indices das listas sempre começam em 0 e não em 1 como no caso da matriz m1
#                      #ij ij ij
m2 = [[1,2,3],       #1 00 01 02
      [4,5,6],       #2 10 11 12
      [7,8,9]]       #3 20 21 22


# a)	da linha 2 (linha 2 o indice i é igual a 1); # 10 11 12
somaLinha2 = 0   #  inicialização da variável somaLinha2 com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):  # i: 0 1 2
  for j in range(ordem): # j: 0 1 2
    if i == 1: # i igual a j, indica que estamos na linha 2
      somaLinha2 = somaLinha2 + m1[i][j]

print(f"soma da linha 2: {somaLinha2}") # imprime a soma da linha 2 da matriz m1


# b)	da coluna 3 (coluna 3 o indice j é igual a 2); # 02 12 22
somaColuna3 = 0 #  inicialização da variável somaColuna3 com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem): # i: 0 1 2
  for j in range(ordem): # j: 0 1 2
    if j == 2: # j igual a 2, indica que estamos na coluna 3
      somaColuna3 += m1[i][j]
print(f"soma da coluna 3: {somaColuna3}") # imprime a soma da coluna 3 da matriz m1


#c)	da diagonal principal (diagonal principal o indice i é igual a j); # 00 11 22
somaDP = 0 #  inicialização da variável somaDP com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i == j: # i igual a j, indica que estamos na diagonal principal
      somaDP += m1[i][j]
print(f"soma da diagonal principal: {somaDP}") # imprime a soma da diagonal principal da matriz m1


# d) da diagonal secundária (diagonal secundária o indice i mais o indice j é menor ou igual do que a ordem - 1); # 20 11 02
somaDS = 0 #  inicialização da variável somaDS com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i + j <= ordem - 1: # i + j menor ou igual a ordem -1, indica que estamos na diagonal secundária
      somaDS += m1[i][j]
print(f"soma da diagonal secundária: {somaDS}") # imprime a soma da diagonal secundária da matriz m1


#e)	acima da diagonal secundária (acima da diagonal secundária o indice i mais o indice j é meno do que a ordem - 1); # 00 10 10
somaAcimaDS = 0 #  inicialização da variável somaAcimaDS com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i+j < ordem -1:  # i + j menor do que ordem - 1, indica que estamos acima da diagonal secundária
      somaAcimaDS += m1[i][j]
print(f"soma Acima Diagonal Secundaria: {somaAcimaDS}") # imprime a soma acima da diagonal secundária da matriz m1


#f)	abaixo da diagonal secundária (abaixo da diagonal secundária o indice i mais o indice j é maior do que a ordem - 1); # 21 12 22
somaAbaixoDS = 0 #  inicialização da variável somaAbaixoDS com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i+j >= ordem: # i + j maior do que ordem, indica que estamos abaixo da diagonal secundária (i + j = ordem)
      somaAbaixoDS += m1[i][j]
print(f"soma Abaixo Diagonal Secundaria: {somaAbaixoDS}") # imprime a soma abaixo da diagonal secundária da matriz m1


#g)	acima da diagonal principal (acima da diagonal principal o indice i é menor do que j); # 01 12 02
somaAcimaDP = 0 #  inicialização da variável somaAcimaDP com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i < j: # i menor do que j, indica que estamos acima da diagonal principal
      somaAcimaDP += m1[i][j]
print(f"soma Acima Diagonal Principal: {somaAcimaDP}") # imprime a soma acima da diagonal principal da matriz m1


#h)	abaixo da diagonal principal (abaixo da diagonal principal o indice i é maior do que j); # 10 20 21
somaAbaixoDP = 0 #  inicialização da variável somaAbaixoDP com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    if i > j: # i maior do que j, indica que estamos abaixo da diagonal principal (i > j)
      somaAbaixoDP += m1[i][j]
print(f"soma Abaixo Diagonal Principal: {somaAbaixoDP}") # imprime a soma abaixo da diagonal principal da matriz m1


#i)	de todos os elementos da matriz.
somaTodos = 0 #  inicialização da variável somaTodos com 0 para que a soma não seja nula ao iniciar o loop
for i in range(ordem):
  for j in range(ordem):
    somaTodos += m1[i][j] # soma todos os elementos da matriz m1
print(f"soma todos os elementos: {somaTodos}") # imprime a soma todos os elementos da matriz m1


# Versão 2.0 do código

# ---------------------------------------------------------------- #

# By: Carlos Eduardo

# print('''
#          Matriz
# +-----+-----+-----+-----+
# | i,j |  0  |  1  |  2  |
# +-----+-----+-----+-----+
# |  0  |  1  |  2  |  3  |
# |  1  |  4  |  5  |  6  |
# |  2  |  7  |  8  |  9  |
# +-----+-----+-----+-----+''')  # Imprimindo a matriz no terminal


# m1 = [
#     [0o1, 0o2, 0o3],
#     [4, 5, 6],        # Criando uma matriz 3x3, utilizando listas para isso
#     [7, 8, 9]
#     ]

# somavrtc1 = 0
# somavrtc2 = 0   # Variáveis para armazenar os valores das somas verticais
# somavrtc3 = 0

# for i in m1: # Não utilizei range no for, ou seja, em vez de pegar índices estou buscando logo as listas
#     somavrtc1 += i[0]
#     somavrtc2 += i[1] # O índice foi usado para representar a coluna e o 'i' a linha
#     somavrtc3 += i[2]

# print('\nSOMA DAS VERTICAIS DA MATRIZ')
# print(f'\nSoma vertical primeira linha: {somavrtc1}')
# print(f'Soma vertical segunda linha: {somavrtc2}') # Imprimindo informações das somas na vertical +
# print(f'Soma vertical terceira linha: {somavrtc3}')

# somahorizontal1 = 0
# somahorizontal2 = 0 # Variáveis para armazenar os valores das somas horizontais
# somahorizontal3 = 0

# indice = 0 # Variável representando índice
# for i in m1: # Para cada item em lista m1, ou seja, toda a matriz.
    
#     if indice == 0: # Se o índice for igual a 0, ou seja, se for a primeira linha
#         somahorizontal1 = sum(i) # Função sum() está somando todos os valores da primeira linha
    
#     elif indice == 1: # Se o índice for igual a 1, ou seja, se for a segunda linha
#         somahorizontal2 = sum(i) # Função sum() está somando todos os valores da segunda linha
    
#     elif indice == 2: # Se o índice for igual a 2, ou seje, se for a terceira linha
#         somahorizontal3 = sum(i) # Função sum() está somando todos os valores da terceira linha

#    indice += 1 # Sempre acabar um ciclo do loop adiciono mais um valor a variável indice para ir pra próxima linha

# print('\nSOMA DAS HORIZONTAIS DA MATRIZ')
# print(f'\nSoma horizontal primeira linha: {somahorizontal1}')
# print(f'Soma horizontal segunda linha: {somahorizontal2}')  # Imprimindo informações das somas na horizontal +
# print(f'Soma horizontal terceira linha: {somahorizontal3}')

# indice = 0 # Variável de indice que vai representar as linhas da nossa matriz
# soma_first_diagonal = 0  # Variável armazenando as somas dos valores em diagonal primária
# soma_second_diagonal = 0 # Variável armazenando as somas dos valores em diagonal secundária

# for i in m1: # Para cada item na em m1, ou seja, quero acessar todas as listas
    
#    for j in i: # Para cada item nas listas citadas acima, o 'j' será os valores e o 'i' as listas
    
#         if indice == m1[indice].index(j): # Se a linha for igual ao índice do nosso valor, estamos na diagonal primária
#            soma_first_diagonal += j # Pego o valor e adiciono a variável de somaDiagonal
        
#        elif indice == 2 and m1[indice].index(j) == 0 or indice == 0 and m1[indice].index(j) == 2: # Se a linha 2 e o indíce do valor igual a 0 ou a linha for igual a 0 e o indíce do valor igual a 2 estamos na diagonal secundária
#            soma_second_diagonal += j # Pego o valor e adiciono a variável de somaDiagonal
        
#       if indice == 1 and m1[indice].index(j) == 1: # Se a linha for igual a 1 e o indice do valor executa a identação
#            soma_second_diagonal += j # Pego o valor e adiciono a variável de somaDiagonal

#    indice += 1

# print('\nSOMA DAS DIAGONAIS DA MATRIZ')
# print(f'\nSoma da diagonal principal: {soma_first_diagonal}') # Informando as somas ao user
# print(f'Soma da diagonal secundária: {soma_second_diagonal}')


# ---------------------------------------------------------------- #
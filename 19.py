'''Implemente uma função que receba uma lista de palavras e retorne a palavra mais longa presente na lista.'''

def palavra_mais_longa(lista):
    palavraLonga = ""
    for palavra in lista:
        if len(palavra) > len(palavraLonga):
            palavraLonga = palavra
    return palavraLonga

lista = []

print('Retornar a palavra mais longa presente na lista')
quantidade = int(input('Quantas palavras você deseja digitar? '))

for i in range(quantidade):
    palavra = input(f'Digite a {i+1}ª palavra: ')
    lista.append(palavra)

palavraGrande = palavra_mais_longa(lista)
print('A palavra mais longa que tem na lista é:', palavraGrande)
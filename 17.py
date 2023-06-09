'''Implemente uma função que receba uma lista de strings e retorne uma nova lista
contendo apenas as strings que possuem mais de 5 caracteres.'''

def reduzir_string(lista):
    nova_lista = []
    for string in lista:
        if len(string) > 5:
            nova_lista.append(string)
    return nova_lista
   
lista = []

for i in range(1,5):
    palavra = str(input('Digite as strings: '))
    lista.append(palavra)
    
r = reduzir_string(lista)
print('As strings que possuem mais de 5 caracteres são: ', r)
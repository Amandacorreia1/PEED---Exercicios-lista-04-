'''Crie uma função que receba duas listas de números e retorne uma nova lista contendo
apenas os elementos que estão presentes em ambas as listas.'''

def presentes_em_ambas_listas(lista_a, lista_b):
    return list(set (lista_a) & set(lista_b))
   
lista_a = []
lista_b = []

print('\t\t\t\t\tComparar os numeros comuns de duas listas.')
print('\t\t Lista-1')
for i in range(1,6):
    numA = int(input('Digite os números que você deseja: '))
    lista_a.append(numA)
 
print('\t\tlista -2')   
for j in range(1,6):
    numB = int(input('Digite os números que você deseja: '))
    lista_b.append(numB)
    
numerosComuns = presentes_em_ambas_listas(lista_a, lista_b)
print('Os numeros comuns nas duas listas são: ', numerosComuns)
    
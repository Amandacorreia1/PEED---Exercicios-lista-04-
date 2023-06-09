'''Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.'''

def soma_num(lista):
    soma = sum(lista)
    return soma

lista = []

quantidade = int(input('Com quantos números você deseja preencher a lista para somá-los: '))

for i in range(quantidade):
    num = int(input('Digite o número: '))
    lista.append(num)

resultado = soma_num(lista)
print('A soma dos números da lista é:', resultado)
'''Escreva um programa que leia uma sequência de números inteiros e 
insira-os em uma fila até que um número negativo seja digitado.
Em seguida, remova todos os elementos da fila e exiba-os na ordem em que foram inseridos.'''

class Item:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None 
class Fila:
    def __init__(self):
        self.inicio = None 
        self.fim = None 
        self.tamanho = 0 
    
    def vazia(self):
        return self.inicio is None
    
    def tam(self):
        return self.tamanho
    
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item 
            self.fim = novo_item 
        self.tamanho += 1 
        
    def desenfileirar(self):
        if self.vazia():
            raise IndexError('A fila está vazia!')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -=1
        return valor
        
def sequenciaNumeros():
    fila = Fila()

    while True:
        numero = int(input('Informe o número para adicionar a fila: '))
        if numero < 0:
            break
        fila.enfileirar(numero)
    print('Numeros adiconados!\n\n')
        
    print('Ordem que os numeros foram inseridos: ')
    while not fila.vazia():
        r = fila.desenfileirar()
        print(r)

sequenciaNumeros()    
'''
Implemente uma fila simples e as operações básicas: inserir, remover e mostrar o elemento da frente.
'''

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    def vazio(self):
        return self.inicio is None
    def tam(self):
        return self.tamanho
      
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.vazio():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho += 1 
        
    def desenfileirar(self):
        if self.vazio():
            raise IndexError('A fila está vazia')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
            
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor 
        
def enfileira_num():
    f = Fila()

    quantidade = int(input('Quantos números você deseja adicionar na fila?: '))
    for i in range(quantidade): 
        num = int(input('Digite o número: '))
        f.enfileirar(num)
    print('Os números foram adicionados na fila.')

    while not f.vazio():
        remover = f.desenfileirar()
        print('Removendo número:', remover)

enfileira_num()
    
        
        
    
        
    
        
    
    
            
            
        
            
        
        
        
    

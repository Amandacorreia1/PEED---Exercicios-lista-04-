'''Implemente uma lista encadeada simples e as operações básicas: inserir no início,
 inserir no final, remover do início, remover do final e exibir a lista.'''
 
class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None #o ponteiro que vai apontar para o próximo

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None
    
    def tam(self):
        return self.tamanho
    
    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.inicio
        self.inicio = novo_item
        self.tamanho +=1
    
    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item
        self.tamanho += 1
        
    def remover_inicio(self):
        if self.inicio is None: #se a lista esta vazia informa a exceção
            raise Exception('A lista está vazia!')
        else:
            self.inicio = self.inicio.proximo
        self.tamanho -=1
        
    def remover_final(self):
        if self.vazia(): #se a lista esta vazia informa a exceção
            raise Exception('A lista está vazia!')
        
        if self.inicio.proximo is None:
            self.inicio = None
        self.tamanho -= 1
        
        atual = self.inicio
        anterior = None
        while atual.proximo is not None:
            anterior = atual
            atual = atual.proximo
        anterior.proximo = None
        self.tamanho -=1
        
    def listar(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        atual = self.inicio
        
        while atual is not None:
            print(atual.dado, end= '\n')
            atual = atual.proximo
        
    def buscar(self, valor):
        if self.inicio is None:
            raise Exception('A lista está vazia!')
        atual = self.inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False    
    
def listaEncadeadaSimples():
    l = ListaEncadeada()
    
    while True:
        print('\nMENU')
        print('''
        [1] - Inserir numero no inicio
        [2] - Inserir numero no final
        [3] - Remover numero no inicio
        [4] - Remover numero no final
        [5] - Mostrar a lista
        [6] - Sair''')

        op = int(input('Informe a opção que você deseja realizar: '))
        
        if op == 1:
            num = int(input('Digite o numero que você quer adicionar no início da lista: '))
            l.inserir_inicio(num)
            print('Número adicionado no início!')
        
        elif op == 2:
            num = int(input('Informe o número que você quer adicionar no final da lista: '))
            l.inserir_final(num)
            print('Número adicionado no final!')
        
        elif op == 3:
            if l.vazia():
                print('A lista está vazia!')
            else: 
                l.remover_inicio()
                print('Número removido do inicio!')
        
        elif op == 4:
            if l.vazia():
                print('A lista está vazia!')
            else: 
                l.remover_final()
                print('Número removido do final!')
                
        elif op == 5:
            print('Os números que contem na lista: ')
            l.listar()
        
        elif op == 6:
            print('Programa foi Encerrado!')
            break
        else:
            print('Opção inválida!')
            
listaEncadeadaSimples()    
'''Crie um programa que exibe ao usuário um menu com as seguintes opções: adicionar número na fila;  
remover número da fila; tamanho da fila; mostrar fila. Todas as opções devem funcionar conforme a ação que ela descreve.'''

class Item:#Cada elemento da fila
    def __init__(self, valor):
        self.valor = valor #para armazenar o valor do elemento
        self.proximo = None #armazenar o endereço do próximo elemento da fila

class Fila:
    def __init__(self):
        self.inicio = None #primeiro elemento da fila
        self.fim = None #último elemento da fila
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
        self.tamanho +=1
    
    def desenfileirar(self):
        if self.vazia():
            raise IndexError("A fila está vazia!")
        valor = self.inicio.valor #armazena o valor do elemento no início da fila e  com isso pode retornar o valor removido posteriormente.
        self.inicio = self.inicio.proximo
        if self.inicio is None: #se NOne, a fila está vazia apos remover a remoção. se sim,
            self.fim = None #atualiza tambem o self.fim pra None pois nao vai ter mais nenhum numero na fila
        self.tamanho -=1
        return valor #retorna o valor que foi removido
    
def menu():
    f = Fila()
    
    while True:
        print('MENU')
        print('''
        [1] - ADICIONAR NÚMERO NA FILA
        [2] - REMOVER NÚMERO DA FILA
        [3] - MOSTRAR TAMANHO DA FILA
        [4] - MOSTRAR FILA
        [5] - SAIR''')

        op = int(input('Informa a opção que você deseja realizar: '))
                       
        if op == 1:
            num = int(input('Digite o número que voccê quer adicionar na fila: '))
            f.enfileirar(num)
            print('Número adicionado!')
            
        elif op == 2:
            if f.vazia():
                print('A fila está vazia!')
            else: 
                f.desenfileirar()
                print('Número removido!')
            
                    
        elif op == 3:
            print('Tamanho da fila é: ', f.tam())
            
        
        elif op == 4:
            print('Números que estão na fila: ')
            if f.vazia():
                print('A fila está vazia!')
            else:
                atual = f.inicio
                while atual is not None:
                    print(atual.valor)    
                    atual = atual.proximo   
        elif op == 5:
            print(' O programa foi Encerrado!')
            break
        else:
            print('Opção inválida!')

menu()
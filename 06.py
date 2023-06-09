'''Considere um supermercado que atende a inúmeros clientes. Cada cliente possui um número
de identificação único e chega ao supermercado em momentos distintos. Implemente um 
sistema que receba a chegada de clientes e mantenha uma fila para o atendimento. 
A cada hora*, o sistema deve atender o próximo cliente da fila e imprimir o número de
identificação desse cliente. (*) Para este exercício, use a biblioteca time conforme exemplo
(ver vídeo https://youtu.be/_smE7WdhCSk?t=59) e espere apenas 5 segundos.'''

import time 
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
            raise IndexError("A fila está vazia!")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor

def chegadaDeClientes():
    fila = Fila()
    
    iddocliente = 1
    quantidade = int(input('Quantos clientes estão na fila para o atendimento? '))
    
    print('Atendimento iniciado!')
    cliente = 0
    while cliente < quantidade:
        fila.enfileirar(iddocliente)
        print(f'Cliente {iddocliente} na fila para atendimento!')
        iddocliente += 1
    
        if not fila.vazia():
            time.sleep(5) 
            cliente = fila.desenfileirar()
            print(f'Cliente {cliente} foi atendido.')
    print('Atendimento foi finalizado!')
chegadaDeClientes()

'''Crie uma agenda telefônica utilizando uma lista encadeada dupla. Cada entrada 
na agenda deve conter o nome e o número de telefone de uma pessoa. 
Implemente as operações de inserir, remover e buscar uma pessoa na agenda.'''

class Item:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None

    def tam(self):
        return self.tamanho

    def inserir_inicio(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.proximo = self.inicio
            self.inicio.anterior = novo_item
            self.inicio = novo_item
        self.tamanho += 1

    def inserir_final(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            novo_item.anterior = self.fim
            self.fim.proximo = novo_item
            self.fim = novo_item
        self.tamanho += 1

    def remover_inicio(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        self.tamanho -= 1

    def remover_final(self):
        if self.vazia():
            raise Exception("A lista está vazia!")
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        self.tamanho -= 1

    def buscar(self, elemento):
        if self.inicio is None:
            raise Exception("A lista está vazia!")
        atual = self.inicio
        while atual is not None:
            if atual.dado[0]== elemento:
                return atual.dado[1]
            atual = atual.proximo
        return False

    def listar(self):
        if self.inicio is None:
            raise Exception("Agenda está vazia!")
        atual = self.inicio
        while atual is not None:
            nome, tel = atual.dado
            print(f'{nome:10}\t\t{tel:11}')
            atual = atual.proximo

def agenda_telefonica():
    lista = ListaDuplamenteEncadeada ()
    
    print('''MENU
    1 - Inserir contato
    2 - Remover contato
    3 - Buscar contato
    4 - Listar contatos
    0 - Sair''')
    
    while True:
        op = int(input('Informe a opção que você deseja realizar: '))
        
        if op == 0:
            print('Agenda foi encerrada!')
            break
        
        elif op == 1:
            nome = input("digite o nome do contato para salvar:")
            tel = int(input("Digite o telefone desse contato: "))
            contato = ((nome, tel))
            lista.inserir_final(contato)
            print("Contato salvo!")
        
        elif op == 2:
            nome = input("digte o nome do contato para apagar: ")
            remover = lista.buscar(nome)
            if remover:
                lista.remover_inicio()
                print("Contato apagado!")
            else:
                print("Contato não foi encontrado na agenda!")


        elif op == 3:
            if lista.vazia():
                raise Exception("Agenda telefônica está vazia!")

            nome = input("Qual contato deseja buscar: ")
            encontrar = lista.buscar(nome)
            
            if encontrar:
               print("Nome:", nome, "Telefone:", tel)
            else:
                print("Contato não foi encontrado na agenda.")

        elif op == 4:
            print('\tAgenda telefônica ')
            lista.listar()
        else:
            print('Opção inválida!')
            
agenda_telefonica()
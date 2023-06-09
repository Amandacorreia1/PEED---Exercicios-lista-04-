'''Escreva uma função que receba uma lista de dicionários, onde cada 
dicionário representa um aluno com as chaves "nome" e "nota".
A função deve retornar o nome do aluno com a maior nota.'''

def aluno_maior_nota():
    alunos = []
    
    qnt = int(input('Quantos alunos deseja adicionar? '))
    
    for i in range(qnt):
        nome = input('Informe o nome do aluno: ')
        nota = float(input('Informe a nota desse aluno: '))
        aluno = {'nome': nome, 'nota': nota}
        alunos.append(aluno)
    
    maiornota = alunos[0]
    
    for aluno in alunos:
        valor = aluno['nota']
        if valor > maiornota['nota']:
            maiornota = aluno
    
    return maiornota['nome'], maiornota['nota']

maiorNota = aluno_maior_nota()
print('O aluno que possui maior nota é: ', maiorNota)  
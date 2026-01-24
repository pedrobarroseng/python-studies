dados_nome_matricula = []
dados_retirada = []

def saudacoes(nome, matricula):
    
    identificaçao = {
        'nome': nome,
        'matricula': matricula
    }
    return identificaçao

def retirada(nome_livro):
    print(f'Houve a retirada do livro {nome_livro}.')

print('----------------------------------------------------------')
print('Boa tarde. Bem-Vindo a nossa biblioteca do colegio Barros.')
print('----------------------------------------------------------')

while True:
    
    
    identificacao = input('Tu seria nosso aluno? (sim ou nao) ').strip().lower()

    if (identificacao == 'sim'):

        print('olá estudante!')
        nome = input('Qual o teu nome? ')
        matricula = input('Qual a tua matricula? ')
        indentificacao_aluno = saudacoes(nome, matricula)
        dados_nome_matricula.append(indentificacao_aluno)

        livro = input('Tu gostaria de realizar a retirada de algum livro? (sim ou nao) ').strip().lower()
        
        if (livro == 'sim'):
    
            nome_do_livro_retirado = input('Qual o livro que tu pegou? ')
            
            observacao = input('Gostarias de ver teu registro? (sim ou nao) ').strip().lower()
            
            if (observacao == 'sim'):
                for i, observacao_registro in enumerate(dados_nome_matricula, 1):
                    print('---------------------------------------------------')
                    print(f'{i}. Nome: {observacao_registro['nome']}  |  Matricula: {observacao_registro['matricula']}')
                    print('---------------------------------------------------')
                    retirada(nome_do_livro_retirado)
                    print('---------------------------------------------------')
                    print('Boa leitura')
                    print('---------------------------------------------------')

                    break
            else:
                print('Sem problema, boa leitura!')
                break
    
        else:
            print('Tudo bem, sinta-se a vontade para poder estudar aqui ')
            break
            
            

            
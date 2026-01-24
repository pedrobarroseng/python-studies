dados_nome_matricula = []
#dados_retirada = [], ache uma maneira de utilizar!

def saudacoes(nome, matricula):
    
    identificaçao = {
        'nome': nome,
        'matricula': matricula
    }
    return identificaçao

def retirada(nome_livro, nome_do_aluno):
    print(f'Houve a retirada do livro {nome_livro} por você, {nome_do_aluno}.')

tupla = ('matemática', 'física', 'química', 'biologia')

print('----------------------------------------------------------')
print('Boa tarde. Bem-Vindo a nossa biblioteca do colegio Barros.')
print('----------------------------------------------------------')


while True:
    
    
    identificacao = input('Tu seria nosso aluno? (sim ou nao) ').strip().lower()

    if (identificacao == 'sim'):

        print('olá estudante!')
        nome = input('Qual o teu nome? ')
        while True:
            try:
                matricula = int(input('Qual a tua matricula? '))
                break
            
            except ValueError:
                print('Digite apenas números!')
            
        
        indentificacao_aluno = saudacoes(nome, matricula)
        dados_nome_matricula.append(indentificacao_aluno)

        livro = input('Tu gostaria de realizar a retirada de algum livro? (sim ou nao) ').strip().lower()
        
        if (livro == 'sim'):
            
            print('------------------------------------------------------------------------')
            print('Esses são os livros disponíveis: matemática, física, química, biologia. ')
            print('------------------------------------------------------------------------')
            print('IMPORTANTE: Escreva o nome dos livros com acento e letra minúscula.')
            print('------------------------------------------------------------------------')
           
            while True:
                
                nome_do_livro_retirado = input('Qual o livro que tu gostaria de pegar? ')
                
                if nome_do_livro_retirado in tupla:
                    print('Retirada com sucesso!')
                    break

                else:
                    print('Não temos esse livros disponível ou verifique a acentuação.')

            
            observacao = input('Gostarias de ver teu registro? (sim ou nao) ').strip().lower()
            
            if (observacao == 'sim'):
                for i, observacao_registro in enumerate(dados_nome_matricula, 1):
                    print('---------------------------------------------------')
                    print(f'{i}. Nome: {observacao_registro['nome']}  |  Matricula: {observacao_registro['matricula']}')
                    print('---------------------------------------------------')
                    retirada(nome_do_livro_retirado, nome)
                    print('---------------------------------------------------')
                    print('Boa leitura')
                    print('---------------------------------------------------')

            else:
                print('Sem problema, boa leitura!')
                break
           
            break
    
        else:
            print('Tudo bem, sinta-se a vontade para poder estudar aqui ')
            break
            
            

            
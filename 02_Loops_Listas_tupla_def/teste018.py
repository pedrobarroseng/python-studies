# --- ÁREA DE DADOS E FUNÇÕES (MANTENHA IGUAL) ---
dados_nome_matricula = []
tupla = ('matemática', 'física', 'química', 'biologia')

def saudacoes(nome, matricula):
    identificacao = {
        'nome': nome,
        'matricula': matricula,
        'nome do livro': 'nenhum'
    }
    return identificacao

def retirada(nome_livro, nome_do_aluno):
    print(f'Houve a retirada do livro {nome_livro} por você, {nome_do_aluno}.')

print('----------------------------------------------------------')
print('   SISTEMA DE BIBLIOTECA - COLÉGIO BARROS (V2.0)   ')
print('----------------------------------------------------------')

# --- O GRANDE LOOP (CENTRAL DE COMANDO) ---
while True:
    print("\nO que deseja fazer?")
    print("1 - Cadastrar Aluno e Retirar Livro")
    print("2 - Ver Relatório Geral (Todos os alunos)")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()

    # --- OPÇÃO 1: CADASTRO ---
    if opcao == '1':
        print("\n--- NOVO CADASTRO ---")
        
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

                    indentificacao_aluno['nome do livro'] = nome_do_livro_retirado
                    break

                else:
                    print('Não temos esse livros disponível ou verifique a acentuação.')
            
            print("\n✅ Cadastro realizado!")
            retirada(nome_do_livro_retirado, nome)
            print('Boa leitura')

        elif(livro == 'nao'):
            print('Tudo bem, seu cadastro foi feito. sinta-se a vontade para estudar em nosso ambiente')
        
       
        print("\n✅ Cadastro realizado!")
     

    # --- OPÇÃO 2: RELATÓRIO ---
    elif opcao == '2':
        print("\n--- RELATÓRIO GERAL DA BIBLIOTECA ---")
        
        if len(dados_nome_matricula) > 0:
              
              for i, observacao_registro in enumerate(dados_nome_matricula, 1):
                    print('---------------------------------------------------')
                    print(f'{i}. Nome: {observacao_registro['nome']}  |  Matricula: {observacao_registro['matricula']}  |  Livro: {observacao_registro['nome do livro']}')
                    print('---------------------------------------------------')
                    
                    if observacao_registro['nome do livro'] != 'Nenhum':
                        retirada(observacao_registro['nome do livro'], observacao_registro['nome'])
                    
                    print('---------------------------------------------------')
                    print('---------------------------------------------------')
                    
        else:
            print("Nenhum aluno cadastrado ainda.")

    # --- OPÇÃO 3: SAIR ---
    elif opcao == '3':
        print("Fechando o sistema... Até amanhã!")
        break # ESSE é o único break que mata o programa.

    else:
        print("Opção inválida! Digite 1, 2 ou 3.")
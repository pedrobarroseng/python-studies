#Crie um sistema que cadastra funcionários

banco_dados = []

while True:
    
    funcionario = input('tu é funcionario? (Sim ou Não)  ').strip().lower()

    if (funcionario == 'sim'):
        
        nome = input('Qual o teu nome? ')
        cargo = input('Qual o teu cargo? ')
        Registro_do_funcionario = {
            'nome': nome,
            'cargo': cargo
        }
        banco_dados.append(Registro_do_funcionario)
        
        ver_banco_de_dados = input('tu gostaria de ver o nosso banco de dados? (Sim ou Nao) ').strip().lower()

        if (ver_banco_de_dados == 'sim'):

            for i, funcionario_do_dic in enumerate(banco_dados, 1):
                print('--------------------')
                print('sistema de cadatros:')
                print(f'{i}. Nome: {funcionario_do_dic['nome']}  |  Cargo: {funcionario_do_dic['cargo']}')
                print('--------------------')
        else:
            print('tudo bem, tu não irá ver!')
    
    elif(funcionario == 'nao'):

        print('tu não irá participar da lista!')

        break
        
#estetica: # Note as aspas duplas " fora e as simples ' dentro
#print(f"{i}. Nome: {funcionario_do_dic['nome']} | Cargo: {funcionario_do_dic['cargo']}")


import os


nome_arquivo = 'Tabela.csv'

if os.path.exists(nome_arquivo) == False:
    
    arquivo = open(nome_arquivo,'w')
    arquivo.write('Nome, Idade, Nº \n')
    arquivo.close

while True:

    print('Escolha uma das opções: ')
    print("1. Novo registro")
    print("2. Ver os registros")
    print("3. Sair")

    while True:
        try:
            reposta = input('Digite o um dos três números (1, 2 ou 3): ')
            break

        except ValueError:
            print('Digite apenas um dos três números.')
    
    if reposta == '1':
        
        arquivo = open(nome_arquivo,'a')
        
        nome = input('Informe teu nome: ')
        idade = input('Informe tua idade: ')
        cpf = input('Informe teu Nº: ')

        arquivo.write(f'{nome}, {idade}, {cpf}\n')
        arquivo.close()

        print('Informações registradas.')

    elif reposta == '2':
        
        try:
            arquivo = open(nome_arquivo,'r')
            conteudo = arquivo.read()
            print('------------------------')
            print('Esses são os registros: ')
            
            print(conteudo)
            arquivo.close()
            
        
        except FileNotFoundError:
            print('Arquivo ainda não existente')
    
    elif reposta == '3':

        print('Saindo')
        break 
    

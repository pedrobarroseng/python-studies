banco_de_dados = []

def criar_ficha(nome, cargo):
   
    dicionario = {
        'Nome': nome,
        'Cargo': cargo
    }
    
    return dicionario

while True:

    funcionarios = input('tu é um funcinário? (Sim ou Nao)').strip().lower()

    if (funcionarios == 'sim'):

        nome = input('Digite o teu nome: ')
        cargo = input('Digite o teu cargo: ')

        ficha_dos_funcionarios = criar_ficha(nome, cargo)
        banco_de_dados.append(ficha_dos_funcionarios)

        ver_registros = input('Gostarias de ver os registros? (Sim ou Nao) ').strip().lower()
        
        if(ver_registros == 'sim'):

            print('abaixo digite seus dados, pois esse sera teu resistro!')
        
            for i, Registro_dos_funcionarios in enumerate(banco_de_dados, 1):
                print(f'{i}. Nome: {Registro_dos_funcionarios['Nome']} | Cargo: {Registro_dos_funcionarios['Cargo']}')

        else:
            print('Tudo bem, tu não irá acessar.')

    elif (funcionarios == 'nao'):

        print('Tu não pertence a empresa!')
        break
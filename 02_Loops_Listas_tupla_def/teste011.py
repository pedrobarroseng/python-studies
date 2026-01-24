tupla = ("admin", "tiago", "convidado")

while True:

    nome_de_acesso = input('digite o nome de acesso: ').strip().lower()

    if nome_de_acesso in tupla:
        print(f'Acesso Liberado! Bem-vindo: {nome_de_acesso}')
        break

    else:

        print('acesso negado!')
        
    
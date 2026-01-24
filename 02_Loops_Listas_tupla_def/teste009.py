lista = []


while True:

    resposta = str(input('Queres participar da lista? (sim ou nao) ')).strip().lower()

    if (resposta == 'sim'):
       
        nome = str(input('Qual teu nome? '))
        print(f'olá,{nome}. tu esta participando da lista.')
        lista.append(nome)
        

    elif (resposta == 'nao'):
        
        tamanho = len(lista)
        
        if(tamanho > 0):

       
            print('---RELATORIO---')
            print('-----------------')
            print('Lista de presença: ')

            for i, nome in enumerate(lista, 1):
                print(f'{i}.{nome} ')
            print('-----------------')
            print(f'o tamanho da lista: {tamanho}')
            print('-----------------')
            print(f'chegamos ao fim. o primeiro da lista: {lista[0]}')
            print('-----------------')
            print(f'o ultimo da lista: {lista[-1]}')
        
            break
        
        else:
            
            print('lista vazia!')
            
            break

tupla = ('ram', 'monitor','ssd')

while True:
    
    peça_nova = input('o nome da peça nova: ')

    if peça_nova in tupla:
        print('essa peça sera comprada!')
        break

    else:
       print('sai fora, essa peça não sera comprada!')

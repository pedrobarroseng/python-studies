fila_pizzaria = []

def pizzaria_barros(cliente, sabor):
    
    atendimento = {
        'cliente': cliente,
        'sabor': sabor,
        'pronto': False
    }
    return atendimento

def Pegou_a_pizza(nome):
    print(f'Obrigado pela preferência. Espero que tu aproveite a nossa pizza, {nome}')

tupla = ('Calabresa', 'Marguerita', 'Quatro queijos', 'Portuguesa', 'Frango com catupiry')

while True:

    print('1) Novo pedido')
    print('2) Ver fila')
    print('3) Entregar pizza ')
    print('4) Cancelar pedido')
    print('5) Sair do sistema')

    while True:
        
        try:
            opcao = input('Escolha uma opção: ')
            break
        except ValueError:
            print('Digite apenas números do 1 ao 4')
    
    if (opcao == '1'):
        
        print('Inicialmente, precisamos de algumas informações.')
        
        nome_cliente = input('Qual o teu nome? ')
        print('----------------------------------------------')
        print('Esses são os sabores: ')
        print('\n'.join(tupla))
        sabor_pizza = input('Qual da nossa casa tu gostaria? ')
        print('----------------------------------------------')

        pizza = pizzaria_barros(nome_cliente, sabor_pizza)
        fila_pizzaria.append(pizza)
        print('Pedido feito!')

    elif (opcao == '2'):
        
        print('Ver fila: ')
        for i, pedido in enumerate(fila_pizzaria, 1):
            
            if pedido['pronto'] == True:
                status = '[x]'
            else:
                status = '[ ]'
            
            print(f'{i}) {status}. Nome do cliente: {pedido['cliente']} - Pizza de sabor: {pedido['sabor']}' )

    elif (opcao == '3'):

        indice = int(input('Qual o teu número do pedido para concluir? '))

        if (1 <= indice <= len(fila_pizzaria)):

            fila_pizzaria[indice - 1]['pronto'] = True
            print('Pedido concluido!')
            nome_da_vez = fila_pizzaria[indice - 1]['cliente']
            Pegou_a_pizza(nome_da_vez)
        else:
            print('Número inválido! ')

    elif (opcao == '4'):

        indice = int(input('Qual o teu número do pedido para concluir? '))


        if (1 <= indice <= len(fila_pizzaria)):

            fila_pizzaria.pop(indice - 1)
            print('Pedido deletado com sucesso')

        else:
            print('numero inválido')
    
    elif (opcao == '5'):

        print('Tchau, espero que tenha gostado da experiência!')
        break






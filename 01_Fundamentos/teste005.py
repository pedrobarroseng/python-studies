n = 1

# Removemos as variáveis fixas do topo. Elas não servem pra nada aqui.
p = input('Qual o nome? ')
print('Ola, {}'.format(p))

while (n > 0):

    # 1. Pergunta inicial
    Resposta = input('Gostaria de conversar (Sim ou Nao)? ').strip().lower()
    
    if (Resposta == 'sim'):
          # ERRADO ANTES: print(..., Estado)
          # CORRETO AGORA: Pedimos o input AQUI e guardamos na variável Estado
          Estado = input('Como vai, {} (Bem ou Mal)? '.format(p)).strip().lower()

          if (Estado == 'bem'):
               print('Que bom, {}. Eu fico feliz'.format(p))
               break
          elif (Estado == 'mal'):
                # Aqui assumimos que se não é 'Bem', pode ser 'Mal'
                # 2. Pedimos o input da Emergencia AQUI dentro
                print('Eu sinto muito, {}.'.format(p))
                Emergencia = input('Gostaria de ligar para emergencia (Sim ou Nao)? ').strip().lower()

                if (Emergencia == 'sim'):
                    print('O numero da emergencia é: 53991776601')
                    break
                elif (Emergencia == 'nao'):
                    print('Tu quer papinho que dure, tchau')
                    break
          
    elif (Resposta == 'nao'):
        print(f'Desculpa o incomodo, {p}')     
        break
p = input('qual o nome? ')
print('Ola, {}'.format(p))

while True:
   
    Resposta = input('Gostaria de conversar (Sim ou Nao)? ').strip().lower()
    
    if (Resposta == 'sim'):
          Estado = input(f'Como vai, {p} (Bem ou Mal)? ').strip().lower()
          
          if (Estado == 'bem'):
               print(f'Que bom, {p}. Eu fico feliz')
               break
          
          elif(Estado == 'mal'):
                print(f'Eu sinto muito, {p}.')
                Emergencia = input(f'Gostaria de ligar para emergencia, {p} (Sim ou Nao)? ').strip().lower()
                
                if (Emergencia == 'sim'):
                    print('O numero da emergencia é: 53991776601')
                    break


                elif (Emergencia == 'nao'):
                    print('tu quer papinho que dure, thau')
                    break
          
    elif (Resposta == 'nao'):
        print(f'Desculpa o incomodo, {p}')     
        break




   
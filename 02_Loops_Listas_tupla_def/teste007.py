
historico = [] 

while True:

    p = input('Qual o nome? ').strip() 
    
    historico.append(p)

    
    print(f'Ola, {p}')

  
    resposta = input('deseja continuar (Sim ou Nao)').strip().lower()
    if (resposta == 'sim'):
        continue
    elif(resposta == 'nao'):
        print("Fim do dia! Pessoas atendidas:", historico)
        break

  
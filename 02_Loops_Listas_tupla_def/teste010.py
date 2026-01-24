listas_de_compras = ['ovos', 'frango', 'arroz']

while True:
   
    equivoco = input('Esqueceu algum alimento? (sim ou nao) ').strip().lower()

    if (equivoco == 'sim'):
        Alimento_novo = input('Qual seria o alimento? ')
        listas_de_compras.append(Alimento_novo)

    elif(equivoco == 'nao'):
        print('-----------------------------')
        print('Essa sera a lista de compras:')
        for i, Alimento_da_lista in enumerate(listas_de_compras,1):
           print(f'{i}.{Alimento_da_lista}') 
        
        break
        

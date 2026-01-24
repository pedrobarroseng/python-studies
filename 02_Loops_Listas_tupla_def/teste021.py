lista_de_comprantes = []
linha_de_producao = []


def indentificacao_do_cliente(nome_completo, cpf):
  informações_cliente = {
  'nome completo': nome_completo,
  'cpf': cpf

  }
  return informações_cliente

def informações_da_montagem(marca_do_carro, modelo, cor):
  informacoes_montagem = {
  'marca do carro': marca_do_carro,
  'modelo': modelo,
  'cor': cor
  }
  return informacoes_montagem

def mostrar_carros():
    carros = {
        "Volkswagen": ["Gol", "Polo", "Virtus", "Jetta", "T-Cross", "Nivus"],
        "Chevrolet": ["Onix", "Onix Plus", "Cruze", "Tracker", "S10", "Spin"],
        "Fiat": ["Uno", "Argo", "Cronos", "Pulse", "Toro", "Strada"],
        "Ford": ["Ka", "Fiesta", "Focus", "EcoSport", "Ranger", "Mustang"],
        "Toyota": ["Etios", "Corolla", "Yaris", "Hilux", "SW4", "RAV4"],
        "Honda": ["Fit", "City", "Civic", "HR-V", "CR-V"]
    }
    return carros
def comprou_carro(nome_comprador):
  print(f'Parabéns {nome_comprador}, você comprou o carro!')
  print('----------------------------------------------------------')

def nao_comprou_carro():
  print(f'Pena que não foi dessa vez, volte quando quiser.')
  print('----------------------------------------------------------')

def compra(marca, modelo):
   print(f'Parabens pela compra do {marca}, modelo {modelo}')


tupla = ['Pedro', 'Jorge', 'Rafael']

while True:

  print('Seja bem-vindo ao nosso atendimento automatizado')
  print('O que deseja fazer: ')
  print('1. Analisar catalogo de carro ')
  print('2. Realizar a compra do carro ')
  print('3. Relatório de Vendas')
  print('4. Sair do sistema')

  while True:
    try:
      opcao = input('Escolha uma das opções: ')
      break
    except ValueError:
      print('Digite apenas números. As opções são 1,2 e 3.')

  if (opcao == '1'):

    print('Sobre o catálogos, nós temos alguns modelos de marcas diferente')
    print('Marcas disponiveis e modelos disponiveis a seguir: ')


    meu_catalogo = mostrar_carros()
    for i,(marca, lista_de_carros) in enumerate(meu_catalogo.items(), 1):

      print('------------------------------------------------------')
      print(f'Marcas:{i}.{marca}')
      carros_texto = ", ".join(lista_de_carros)

      print(f'     Modelos:{carros_texto}')
      print('------------------------------------------------------')

  elif (opcao == '2'):

    prosseguir_compra = input('Gostarias de prosseguir a compra? (sim ou nao) ').strip().lower()

    if (prosseguir_compra == 'sim'):

       print('inicialmente precisamos de alguns dados.')

       nome = input('Qual o teu nome completo? ')
       cpf = input('Qual o teu cpf? ')

       info_do_cliente = indentificacao_do_cliente(nome, cpf)

       marca_do_carro = input('Qual marca tu gostaria de pegar? ').strip().title()
       seu_futuro_carro = mostrar_carros()
       
       if marca_do_carro in seu_futuro_carro:
          print(f'Otima escolha de marca, muito boa a {marca_do_carro}!')

          lista_de_modelos = seu_futuro_carro[marca_do_carro]
          
          modelos_texto = ', '.join(lista_de_modelos)
          print(f'modelos disponíveis: {modelos_texto}')

          carro_escolhido = input('Qual carro foi o escolhido? ').strip().title()

          if carro_escolhido in lista_de_modelos:
             
             cor_escolhida = input(f'Qual cor tu gostaria de colocar no teu {carro_escolhido}? ')
             
             info_do_carro = informações_da_montagem(marca_do_carro, carro_escolhido, cor_escolhida)
             
             venda_completa = {
                 'Cliente': info_do_cliente, 
                 'Carro': info_do_carro
             }
            
             linha_de_producao.append(venda_completa)
             
             compra(marca_do_carro, carro_escolhido)
             comprou_carro(info_do_cliente['nome completo'])
             
          
          else:
                print('Nao temos esse modelo.')
        
        
       else:
            print('Não temos essa marca!')
             
    else:

        nao_comprou_carro()

  elif (opcao == '3'):
     
     print('Você entrou numa área restrita. Somente gerentes podem prosseguir por cuidado aos nossos clientes')
     
     fun_nome = input('Qual o teu nome? ')

     if fun_nome in tupla:
        
        print('Podemos prosseguir agora.')  
        print('\n--- 📊 RELATÓRIO DO GERENTE ---')

        if len(linha_de_producao) > 0:
           
           for i, venda in enumerate(linha_de_producao, 1):
              
              nome_cli = venda['Cliente']['nome completo']
              cpf_cli = venda['Cliente']['cpf']
              nome_car = venda['Carro']['modelo']
              cor_car = venda['Carro']['cor']

              print(f'{i}. Cliente: {nome_cli}, CPF: {cpf_cli}  |  Levou: {nome_car} {cor_car} ')
           
        else:
            print('Tu não faz parte do grupo de pessoas que pode visualizar')
            break



















  elif (opcao == '4'):

    print('Espero que tua experiência tenha sido boa, volte sempre!')
    break


  else:

    print('Opção inválida, digite 1, 2 ou 3.')


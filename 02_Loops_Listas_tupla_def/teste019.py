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


while True:

  print('Seja bem-vindo ao nosso atendimento automatizado')
  print('O que deseja fazer: ')
  print('1. Analisar catalogo de carro ')
  print('2. Realizar a compra do carro ')
  print('3. Sair do sistema ')

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

       marca_do_carro = input('Qual marca tu gostaria de pegar? ')
       modelo = input('Qual seria o modelo? ')
       cor = input('Qual seria a cor do carro? ')

       info_do_carro = informações_da_montagem(marca_do_carro, modelo, cor)

       venda = {'Cliente': info_do_cliente, 'carro': info_do_carro}
       linha_de_producao.append(venda)

       print(f'Parabens,{info_do_cliente['nome completo']} do CPF: {info_do_cliente['cpf']}')
       print(f'Informamos a tua compra do {info_do_carro['modelo']} {info_do_carro['cor']} da marca {info_do_carro['marca do carro']}')

       comprou_carro(info_do_cliente['nome completo'])

    else:

       nao_comprou_carro()

  elif (opcao == '3'):

    print('Espero que tua experiência tenha sido boa, volte sempre!')
    break

  else:

    print('Opção inválida, digite 1, 2 ou 3.')


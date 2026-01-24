#1
#ano = int(input('Qual o teu ano de nascimento? '))

#if ano <= 2026:
 #idade_atual = 2026 - ano
  #  print(f'A idade desse idividuo é {idade_atual}.')

#else:
#    print('Irmão não faz sentido esse ano!')

#2

#TAXA_IMPOSTO = 0.10
#nome = input('Qual o teu nome? ')
#salario = float(input('Qual o teu salário? '))

#print(f'Esse é o descontos do terá no teu salário, {nome}')
#salario_descontos = salario * TAXA_IMPOSTO
#print(salario_descontos)

#print(f'Esse é teu salario líquido, {nome}')
#salario_liquido = salario - salario_descontos
#print('-----------------------------------')
#print(f'Olá {nome} , seu salário líquido é R$ {salario_liquido}.')

#velocidade_car = float(input('Qual é a velocidade do carro? '))
#velocidade_max_via = float(input('Qual é a vellocidade da via? '))
#velocidade_acima20 =  velocidade_max_via * 1.20
#velocidade_acima50 =  velocidade_max_via * 1.50

#if (velocidade_car > velocidade_max_via) and (velocidade_car <= velocidade_acima20):
 #   print('Isso dá uma multa média ')

#elif (velocidade_car > velocidade_acima20) and (velocidade_car <= velocidade_acima50):
#    print('Multa Grave')

#elif (velocidade_car > velocidade_acima50):
#    print('Multa Gravíssima')

#else: 
#    print('Boa Viagem')

#Crie um código que pede usuario e senha. O acesso só é permitido se: usuario == "admin" E senha == "1234". Caso contrário, exiba "Acesso Negado"

#usuario = input('Qual o teu usuario? ')
#senha = input('Digite sua senha (são 4 digitos): ')

#if (usuario == 'adm') and (senha == '1234'):
 #   print('Acesso permitido')

#else:
 #   print('Acesso negado! ')

#Altura_mínima = 1.50 
#Idade_mínima = 12 

#print('Seja bem vindo ao park')

#while True:
 #   nome = input('Qual o teu nome? ')
  #  altura = float(input(f'Qual a tua altura, {nome}? '))
   # idade = int(input(f'Qual a tua idade, {nome}? '))

#    pode_entrar = (altura >= Altura_mínima) and (idade >= Idade_mínima)
   
#    if pode_entrar:
#        print('Seja bem vindo e se divirta')
#        print(pode_entrar)
 #       print(f'{altura}m')
 #       print(idade)
    
  #  else:
   #     print('não pode brincar')
    #    break



#while True:
 #   numero1 = float(input('Digite um número para realizar as operações: '))
  ###if operador == '+':
     #   resultado = numero1 + numero2
      #  print(f'Esse é o resultado: {resultado}')
       # break
    #elif operador == '-':
     #   resultado = numero1 - numero2
     #   print(f'Esse é o resultado: {resultado}')
     #   break
    #elif operador == '*':
     #   resultado = numero1 * numero2
     #   print(f'Esse é o resultado: {resultado}')
      #  break
    #elif operador == '/':
     #   resultado = numero1 / numero2
      #  print(f'Esse é o resultado: {resultado}') 
       # break  

    #else: 
     #   print('operador não existente, tente novamente. Essas são as opções: (+, -, *, /) ') 

#numero = float(input('Digite um número: '))
#
#if numero % 2 == 0: 
 #   print(f'O numero {numero} é par')

#else:
#    print(f'O numero {numero} é ímpar')

#class Carro:
 #   # Método construtor para inicializar o objeto
  ###    self.modelo = modelo # Atributo
     #   self.cor = cor       # Atributo

    # Método (comportamento)
    #def ligar(self):
     #   print(f"O {self.marca} {self.modelo} está ligando...")

# Criando objetos (instâncias) da classe Carro
#meu_carro = Carro("Toyota", "Corolla", "Prata")
#carro_vizinho = Carro("Honda", "Civic", "Preto")

# Acessando atributos e chamando métodos
#print(f"Meu carro é um {meu_carro.marca} {meu_carro.modelo}.")
#meu_carro.ligar()
# Lista de frutas (veremos Listas a fundo amanhã, mas o conceito é esse)

#frutas = ["maçã", "banana", "laranja"]

#for fruta in frutas:
 #   print(fruta)

#contador = 0

#while contador < 5:                 # Enquanto contador for menor que 5
 #   print(f"Contagem: {contador}")
  #  contador += 1                   # Soma 1 ao contador (contador = contador + 1)

#convidados = ["Ana", "Pedro", "João"]
#nome = input("Qual o teu nome? ").title()

#if nome in convidados:
   
 #   print(f"seja bem vindo, {nome}")
  #  print("Essa é a lista de convidados:")
   # for pessoas_convidadas in convidados:

    #    print(pessoas_convidadas)

#else: 
 #   print(f"Tu não esta na lista, {nome}")

#lista = [10, 15, 20, 23]

#or numeros in lista:
#    print(numeros)

  #  if numeros % 2 == 0:
   #     print(f'números pare: {numeros}')

   # else:
    #    print(f'número ímpar: {numeros}')

#tarefas = []
#tarefas.append('Estudar')
#tarefas.append('Dormir')
#tarefas.append('Comer')

#print('tarefas da semana')
#for i, compras in enumerate(tarefas, 1):
 #   print(f'{i}. Tarefas: {compras}')


#Nome = input('Qual teu nome? ')
#ota = float(input('Qual foi a tua nota? '))

#aluno = {
    #'nome': Nome, 
   # 'nota': Nota, 
  #  'aprovado': True 
 #   }

#aluno['aprovado'] = Nota >= 7

#if aluno['aprovado']:
 #  print(f'O aluno {aluno['nome']} tirou {aluno['nota']}. Status aprovado: {aluno['aprovado']}')

#else: 
#   print(f'O aluno {aluno['nome']} tirou {aluno['nota']}. Status aprovado: {aluno['aprovado']}')#

#cores_semaforo = ('Vermelho', 'Amarelo', 'Verde')
#print(cores_semaforo[1])

#class Pessoa:
    
   #def __init__(self, nome, peso):
    #    self.nome = nome
     #   self.peso = peso
   
  #def mostrar_peso(self):
   #    print(f'Teu peso é: {self.peso}')
   
   #def comer(self):
    #   peso_anterior = self.peso
     #  self.peso += 1
      # print(f'Estou comendo, meu peso anterior era {peso_anterior}, agora é {self.peso} Kg')

#nome_individuo = input('Qual o teu nome? ')
#peso_individuo = float(input('Qual o teu peso? '))
#individuo = Pessoa(nome_individuo, peso_individuo) 
        
#vontade = input('Tu deseja comer? (Sim ou Não) ').strip().lower()

#if vontade == 'sim':
 #   individuo.comer()

#else:
 #   individuo.mostrar_peso()
    
#class Animal: 
 #   def falar(self):
  #      print('Som genético')


#class Gato(Animal):
 #   def falar(self):
  #    print('miau')

#animalzinho = Gato()
#animalzinho.falar()

#estoque = ["Teclado", "Mouse", "Monitor"]

#while True:

 # produto = input('Qual produto tu deseja buscar? ').title()

 # if produto in estoque:
  #    print(f'Temos o {produto} em estoque')
   #   pedido = input('Queres continuar o pedido? (sim ou não) ')
    #  break

  #else:
   #   print(f'O produto {produto} está indiponível, mas vou encomendar para a loja.')
    #  estoque.append(produto)
     # print('------------------------------------------------------------')
      #print('Produto encomendado, faça teu pedido novemante')
      #print('Esses são os produtos atuais: ')
      #for i in estoque:
      #   print(i)

#📝 Exercício 1 — Classe simples

#Crie uma classe Pessoa que tenha:

#atributo nome

#método cumprimentar() que imprime:
#"Olá, meu nome é <nome>"

#class Pessoa:
   
 #  def __init__(self, nome):
        
  #    self.nome = nome
   
  # def cumprimentar(self):
   #    print(f'Olá, meu nome é {self.nome}')

#identificacao = Pessoa('Pedro')
#identificacao.cumprimentar()
        

#📝 Exercício 2 — Classe com números
#Crie uma classe Conta que tenha:
#atributo saldo
#método mostrar_saldo()
#método depositar(valor)

#class Conta: 
    
    #def __init__(self, saldo):
     #   self.saldo = saldo
    
    #ef mostrar_saldo(self):
     #   print(f'Esse é teu saldo {self.saldo}')
    
    #def depositar_saldo(self, valor):
     #   self.saldo = self.saldo + valor 
      #  print(f'Esse é o novo saldo da conta {self.saldo}')

#saldo = Conta(1000)
#saldo.mostrar_saldo()
#saldo.depositar_saldo(100)


#Exercício 3 — Decisão
#Crie uma classe Aluno com:
#nome
#nota
#étodo verificar_aprovacao() que imprime se o aluno está aprovado (nota ≥ 7)        

#class Aluno:
   
 #  def __init__(self, nome, nota):
  #    self.nome = nome
   #   self.nota = nota

   #def verificacao(self):
    #  if self.nota >= 7:
     #    print(f'Parabens, {self.nome}. Tu passou!')
      
     # else:
      #   print(f'Nota insuficiente, {self.nome} ')

#nome = input('Degite teu nome: ')
#Nota = float(input('Digite a tua nota: '))

#individuo = Aluno(nome, Nota)
#individuo.verificacao()



#📝 Exercício 4 — Herança
#Crie:
#classe Animal com método falar() → "Som genérico"
#classe Cachorro que herda de Animal e fala "Au au"

#class Animal:
 #  def falar(self):
  #    print('Som genérico')

#class Cachorro(Animal):
 #  def falar(self):
  #    return 'AUAU'
   

#totó = Cachorro()
#print(totó.falar())

#def uniao():
 #   a=[7,4,1,5]
  #  b=[1,8,7,3,6]
   # return a + b

#calculo = uniao()
#list.sort(calculo)
#print(calculo)

#soma = 0
#for numero in calculo: 
#  soma += numero
#print(soma)
#print(f'A média seria: {soma/len(calculo)} ')


import random

def e_anagrama():
    
    primeiro_nome = input('Digite a primeira palavra: ')
    segundo = input('Segunda palavra: ')

    if  len(primeiro_nome) == len(segundo):
        for letra in primeiro_nome:
            print(letra)
        print('---------------------------')
        for letra2 in segundo:
           print(letra2)
        print('---------------------------')

        if sorted(primeiro_nome) == sorted(segundo):
            
            print('vou reorganizar')
            
            p_numero1 = list(primeiro_nome)
            random.shuffle(p_numero1)
            p_numero2 = list(segundo)
            random.shuffle(p_numero2)
            resultado1 = "".join(p_numero1)
            print(resultado1)
            resultado2 = "".join(p_numero2)
            print(resultado2)
            
            return 'São anagramas'
        

        else:
            print('Não são anagramas, pois possuem letras diferentes')
            return(False)
    
    else:
        print('Não tem como ser um anagrama, tem quantidades diferentes de letras.')
        return(False)

mostrar_letras = e_anagrama()
print(mostrar_letras)    
          


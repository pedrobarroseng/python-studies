import os
import random

def numero_aleatório():
    numero = random.randint(1,1000)
    return numero
    
nome_arquivo = '04_Manipulacao_Arquivos/Tabela.csv'

def obter_id_ja_usados(nome_arquivo):
    
    lista = []
    
    if os.path.exists(nome_arquivo) == False:
        return lista
    
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines() 
    arquivo.close()

    for linha in linhas[1:]:
        partes = linha.strip().split(',')
        
        id_encontrado = int(partes[2]) 
        lista.append(id_encontrado)
        
        
    return lista

if os.path.exists(nome_arquivo) == False:
    
    arquivo = open(nome_arquivo,'w')
    arquivo.write('Nome, Idade, Nº \n')
    arquivo.close()

while True:

    print('Escolha uma das opções: ')
    print("1. Novo registro")
    print("2. Ver os registros")
    print("3. Sair")

    while True:
        try:
            reposta = int(input('Digite o um dos três números (1, 2 ou 3): '))
            
            if reposta == 1 or reposta == 2 or reposta == 3:
                break  
            
            else:
                print('Erro: O número deve ser 1, 2 ou 3.')
            
        except :
            print('Digite apenas um dos três números.')
    
    if reposta == 1:
        
        arquivo = open(nome_arquivo,'a')
        
        nome = input('Informe teu nome: ')
        idade = input('Informe tua idade: ')

        ids_ocupados = obter_id_ja_usados(nome_arquivo)
        
        while True:
        
            novo_id = numero_aleatório()
            
            if novo_id not in ids_ocupados:
                break 
        
            print(f"⚠️ O número {novo_id} já existia! Sorteando outro...")

        arquivo.write(f'{nome}, {idade}, {novo_id}\n')
        arquivo.close()
        
        print('------------------------')
        print('Informações registradas.')
        print(f'Esse é o teu numero de identificação: {novo_id}')
        print('------------------------')

    elif reposta == 2:
        
        try:
            arquivo = open(nome_arquivo,'r')
            conteudo = arquivo.read()
            print('------------------------')
            print('Esses são os registros: ')
            
            print(conteudo)
            arquivo.close()
            
        
        except FileNotFoundError:
            print('Arquivo ainda não existente')
    
    elif reposta == 3:

        print('Saindo')
        break 
    
   
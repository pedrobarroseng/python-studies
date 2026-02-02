import random
import os

print('⚡ Gerenciador de Estoque de Laboratório ⚡')

def numero_aleatório():
    return random.randint(1,1000)

nome_arquivo = 'Estoque_Lab.csv'

def obter_id_usado(nome_arquivo):
    lista = []
    if not os.path.exists(nome_arquivo):
        return lista
    
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas[1:]:
        partes = linha.strip().split(',')
        try:
            id_encontrado = int(partes[0]) 
            lista.append(id_encontrado)
        except (ValueError, IndexError):
            continue
    return lista

# Garante o cabeçalho
if not os.path.exists(nome_arquivo):
    arquivo = open(nome_arquivo,'w')
    arquivo.write('ID,Componente,Quantidade\n')
    arquivo.close()

while True:
    print('\n--- MENU DO LABORATÓRIO ---')
    print("1. Cadastrar Novo Item")
    print("2. Comprar Componente (Dar Baixa)")
    print("3. Sair")

    # Validação
    while True:
        try:
            reposta = int(input('Opção: '))
            if reposta in [1, 2, 3]:
                break  
            else:
                print('Erro: Escolha 1, 2 ou 3.')
        except ValueError:
            print('Digite apenas números.')

    if reposta == 1:
        nome_componente = input('Nome do componente: ')
        qtd = input('Quantidade inicial: ')
        
        ids_ocupados = obter_id_usado(nome_arquivo)

        while True:
            novo_id = numero_aleatório()
            if novo_id not in ids_ocupados:
                break 
        
        arquivo = open(nome_arquivo, 'a')
        arquivo.write(f'{novo_id},{nome_componente},{qtd}\n')
        arquivo.close()
        
        print(f'✅ Cadastrado! ID: {novo_id}')
    
    # --- A MÁGICA ACONTECE AQUI ---
    elif reposta == 2:
        # 1. Mostrar o Estoque
        print('\n --- ITENS DISPONÍVEIS ---')
        if not os.path.exists(nome_arquivo):
            print("Estoque vazio!")
            continue

        arquivo = open(nome_arquivo, 'r')
        linhas = arquivo.readlines() # Lemos tudo para a memória
        arquivo.close()

        for linha in linhas:
            print(linha.strip().replace(',', ' | ')) # Visual bonito
        print('---------------------------')

        # 2. Escolher o ID
        try:
            id_compra = int(input('Digite o ID do item que deseja comprar: '))
        except ValueError:
            print("ID inválido!")
            continue

        # 3. Processo de Reescrita (A "Borracha")
        nova_lista_para_salvar = []
        encontrou_item = False

        for linha in linhas:
            partes = linha.strip().split(',')
            
            # Se for o cabeçalho ("ID,Nome..."), só copia e passa pro próximo
            if partes[0] == "ID":
                nova_lista_para_salvar.append(linha)
                continue

            # Pega o ID da linha atual
            id_atual = int(partes[0])
            nome_atual = partes[1]
            qtd_atual = int(partes[2])

            # SE FOR O ID QUE O CLIENTE QUER:
            if id_atual == id_compra:
                encontrou_item = True
                if qtd_atual > 0:
                    qtd_nova = qtd_atual - 1
                    print(f"✅ Compra realizada! Você levou um {nome_atual}.")
                    print(f"Estoque restante: {qtd_nova}")
                    # Cria a linha atualizada
                    nova_linha = f"{id_atual},{nome_atual},{qtd_nova}\n"
                    nova_lista_para_salvar.append(nova_linha)
                else:
                    print(f"❌ Erro: O item {nome_atual} está esgotado (Zero estoque)!")
                    # Mantém a linha como estava (com zero)
                    nova_lista_para_salvar.append(linha)
            
            # SE NÃO FOR O ID, SÓ COPIA IGUAL
            else:
                nova_lista_para_salvar.append(linha)

        # 4. Salvar o arquivo novo (Sobrescrevendo o antigo)
        if encontrou_item:
            arquivo = open(nome_arquivo, 'w') # O modo 'w' apaga tudo e escreve do zero
            for linha in nova_lista_para_salvar:
                arquivo.write(linha)
            arquivo.close()
        else:
            print("⚠️ ID não encontrado na lista.")

    elif reposta == 3:
        print('Saindo...')
        break
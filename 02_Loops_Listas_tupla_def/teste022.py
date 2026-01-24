lista_tarefas = []

def adicionar_tarefa(descricao, prioridade):
  
    nova_tarefa = {
        'descricao': descricao,
        'prioridade': prioridade,
        'concluida': False 
    }
    return nova_tarefa

while True:
    print('\n=== ✅ GERENCIADOR DE TAREFAS ===')
    print('1. Nova Tarefa')
    print('2. Listar Tarefas')
    print('3. Marcar como Concluída (UPDATE)')
    print('4. Remover Tarefa (DELETE)')
    print('5. Sair')
    
    while True:
        try:
            
            opcao = input('Escolha: ').strip()
            break
        
        except ValueError:
        
            print('Quero que tu digite um dos cinco números: 1, 2, 3, 4 ou 5')

    if opcao == '1':
        desc = input('O que precisa ser feito? ').strip().capitalize()
        prio = input('Prioridade (Alta/Média/Baixa): ').strip().capitalize()
        
        tarefa_pronta = adicionar_tarefa(desc, prio)
        lista_tarefas.append(tarefa_pronta)
        print('Tarefas adicionada!')

    elif opcao == '2':
        print('\n--- SUAS TAREFAS ---')
        for i, tarefa in enumerate(lista_tarefas, 1):
            
            status = "[x]" if tarefa['concluida'] else "[ ]"
            
            print(f"{i}. {status} {tarefa['descricao']} - Prioridade: {tarefa['prioridade']}")

    elif opcao == '3':
      
        indice = int(input('Qual o número da tarefa para concluir? '))
   
        if 1 <= indice <= len(lista_tarefas):
            
            lista_tarefas[indice - 1]['concluida'] = True
            
            print("Tarefa marcada como feita! ✅")
        else:
            print("Número inválido.")

    elif opcao == '4':

        indice = int(input('Qual o número da tarefa para apagar? '))

        if 1 <= indice <= len(lista_tarefas):
            
            lista_tarefas.pop(indice - 1)
           
            print("Tarefa removida com sucesso! 🗑️")
        else:
            print("Número inválido.")

    elif opcao == '5':
        break
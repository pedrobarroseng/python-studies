import os # Biblioteca para coisas do sistema (opcional, mas bom conhecer)


NOME_ARQUIVO = "segredos.txt"

print("--- 📓 MEU DIÁRIO SECRETO ---")

while True:
    print("\nO que você deseja fazer?")
    print("1. ✍️  Escrever nova página")
    print("2. 👀 Ler páginas antigas")
    print("3. ❌ Sair")
    
    opcao = input("Escolha: ")

    if opcao == '1':
       
        texto = input("Digite seu pensamento: ")
        
        with open(NOME_ARQUIVO, "a") as arquivo:
            arquivo.write(f"- {texto}\n") 
        
        print("✅ Salvo no diário!")

    elif opcao == '2':
        try:
            
            with open(NOME_ARQUIVO, "r") as arquivo:
                conteudo = arquivo.read()
                print("\n--- 📜 PÁGINAS DO PASSADO ---")
                print(conteudo)
                print("-----------------------------")
        except FileNotFoundError:
            print("⚠️  Você ainda não escreveu nada no diário!")

    elif opcao == '3':
        print("Fechando o diário... Até mais! 👋")
        break
    
    else:
        print("Opção inválida!")
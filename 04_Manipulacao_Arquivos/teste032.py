#while True:
 #   print("--- LOJA DO RPG ---")
  #  # SE EU DIGITAR "dez" AQUI, O PROGRAMA EXPLODE!
   # try:
    #    quantidade = int(input("Quantas poções você quer comprar? "))
     #   break    
    #except ValueError:
     #   print('Digite números (ex: 1, 2, ...), não digite o número por extenso (com letras)')

#print(f"Você comprou {quantidade} poções.")

 # 1. ABRIR (Modo 'w' significa Write/Escrever)
# Se o arquivo não existir, o Python CRIA ele pra você.
arquivo = open("save.txt", "w")

# 2. ESCREVER
# Importante: O .write() só aceita STRING (Texto)
arquivo.write("Nome: Batman\n")
arquivo.write("Vida: 100\n")
arquivo.write("Nivel: 5")

# 3. FECHAR (Salvar de verdade)
arquivo.close()

print("✅ Jogo salvo com sucesso! Verifique o arquivo save.txt")   
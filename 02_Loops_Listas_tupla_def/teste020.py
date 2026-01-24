# BANCO DE DADOS

def catalogo_filmes():
    # Dicionário com Listas (Gênero -> Lista de Filmes)
    filmes = {
        "Terror": ["Pânico", "It", "Hereditário"],
        "Comédia": ["As Branquelas", "O Máscara"],
        "Ação": ["Vingadores", "Batman", "Matrix"]
    }
    return filmes

def boas_vindas(nome_usuario):
    print(f"Olá {nome_usuario}, prepare a pipoca!")

def boa_sessao(nome_filme, nome):
    print(f'Aproveite nosso filme {nome_filme}, {nome}.')


tupla = ('terror', 'comédia', 'ação')
# --- PROGRAMA ---
cliente = input("Qual seu nome? ")


# ERRO 1: A variável aqui fora chama 'cliente', mas a função pede 'nome_usuario'. 
# Como você chama a função corretamente passando o cliente?

boas_vindas(cliente) 

print("Filmes disponíveis:")

# ERRO 2: O loop para ler Dicionário com Lista.
# Complete os espaços 
# ___
meu_streaming = catalogo_filmes()

for genero, lista_de_filmes in meu_streaming.items():
    print(f"Gênero: {genero}")
    
    # Quero imprimir os filmes bonitinhos na mesma linha
    # Use o join que aprendemos
    filmes_texto = ", ".join(lista_de_filmes) 
    print(f"      Assista: {filmes_texto}")
    print("---")

while True:

    print(tupla)
    tipo_genero = input('Qual o genero do filme que gostaria de assistir? ')

    if tipo_genero in meu_streaming:
        
        print(f'✅ Ótima escolha! Abrindo a sessão de {tipo_genero}...')
        
        # MÁGICA: Pegamos a lista direto do dicionário, sem if/elif!
        lista_do_genero = meu_streaming[tipo_genero]
     
        filmes_texto = ", ".join(lista_do_genero)
        print(f'Filmes em cartaz: {filmes_texto}')
        
        # Agora o cliente escolhe
        filme_escolhido = input('Qual o filme escolhido? ').strip()
        
        # Validamos se o filme existe nessa lista específica
        if filme_escolhido in lista_do_genero:
            boa_sessao(filme_escolhido, cliente)
            break # Encerra o programa
        else:
            print("❌ Ops, esse filme não está na lista desse gênero. Tente novamente.")
            
    else:
        print('❌ Gênero não encontrado. Tente: Terror, Comédia ou Ação.')

   
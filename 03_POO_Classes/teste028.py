import random

class Criatura:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
        self.vida = random.randint(80, 100) 
    
    def atacar(self, inimigo):
        dano = random.randint(10, 25)
        inimigo.vida -= dano
        print(f"⚔️ {self.nome} atacou {inimigo.nome} causando {dano} de dano!")

class Heroi(Criatura):
    def curar(self):
       
        recuperacao =  random.randint(10,30) 
        self.vida == 100
        self.vida += recuperacao
        print(f"✨ {self.nome} usou uma poção e recuperou {recuperacao} de vida, agora está com {self.vida}!")

class Monstro(Criatura):
    pass 

print("--- 🏰 BEM-VINDO AO LABIRINTO ---")
nome_heroi = input("Qual o nome do seu herói? ")
jogador = Heroi(nome_heroi, "Espada Lendária")

orc = Monstro("Ogro Fedorento", "Clava Gigante")

print(f"\nUm {orc.nome} selvagem apareceu com {orc.vida} de vida!")


while jogador.vida > 0 and orc.vida > 0:
    print(f"\nSua Vida: {jogador.vida} | Vida do Inimigo: {orc.vida}")
    print("1. Atacar ⚔️")
    print("2. Beber Poção 🧪")
    
    escolha = input("O que você faz? ")

    if escolha == '1':
        jogador.atacar(orc)
        print(f'Essa é a vida atual do orc {orc.vida}')
        
    elif escolha == '2':
        jogador.curar()
    else:
        print("Você tropeçou e perdeu a vez!")

    if orc.vida > 0:
        print("--- Vez do Inimigo ---")
        orc.atacar(jogador)


if jogador.vida > 0:
    print(f"🏆 VITÓRIA! {jogador.nome} derrotou o {orc.nome}!")
else:
    print("☠️ GAME OVER...")
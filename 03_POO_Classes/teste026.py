violencia = []
class Personagem:
    def __init__(self, nome, poder, cor_do_pijama):
        self.nome = nome
        self.poder = poder
        self.vida = 100
        self.cor_do_pijama = cor_do_pijama

    def mostrar_status(self):
        
        print(f"{self.nome} tem {self.vida} de vida.")

    def mostrar_pijama(self):
        print(f'eu, {self.nome}, amo dormir com meu {self.cor_do_pijama}')

    def atacar(self, inimigo): 
        
        print(f"👊 {self.nome} usou {self.poder} em {inimigo.nome}!")    
        inimigo.vida = inimigo.vida - 10

class Heroi(Personagem): 
    def agir_heroi(self):
        print(f"O Herói {self.nome} usa {self.poder} com o seu {self.cor_do_pijama} para SALVAR o dia! 🛡️")

class Vilao(Personagem):
    def agir_vilao(self):
        print(f"O Vilão {self.nome} usa {self.poder} com o seu {self.cor_do_pijama} para DESTRUIR tudo! 💣")


batman = Heroi("Batman", "Dinheiro", 'pijama rosa')
coringa = Vilao("Coringa", "Risada Maligna", 'pijama roxo')

batman.agir_heroi()  
coringa.agir_vilao() 

print('Batman:')
print(batman.vida)
print(batman.cor_do_pijama)

batman.mostrar_pijama()

batman.atacar(coringa)
print(coringa.vida)

print("\n--- 🤡 A VINGANÇA DO CORINGA ---")

for violencia in range(3):
    coringa.atacar(batman)

    

print(f"Vida do Batman depois da surra: {batman.vida}")


# CLASSE PAI (Genérica)
class Animal:
    def falar(self):
        print("...") # O animal genérico não fala nada

# FILHO 1
class Cachorro(Animal):
    def falar(self): # <--- MESMO NOME DO PAI
        print("🐶 Cachorro: Au Au!")

# FILHO 2
class Gato(Animal):
    def falar(self): # <--- MESMO NOME DO PAI
        print("🐱 Gato: Miau!")

class Pato(Animal):
    def falar(self):
        print('Patp Quak')

# --- A MÁGICA (POLIMORFISMO) ---
# Eu posso tratar todos como "Animal", sem saber qual é qual!

bichos = [Cachorro(), Gato(), Pato()]

for bicho in bichos:
    # O Python descobre sozinho quem é quem e usa o som certo!
    bicho.falar()
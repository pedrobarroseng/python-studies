class Animal:
    def falar():
        print('...')

class Gato(Animal):
    def falar(self):
        return 'miau'
    
class Cachorro(Animal):
    def falar(self):
        return 'Auau'

class Pato(Animal):
    def falar(self):
        return 'Quak'



while True:
    
    meu_bichinho = input('Ecolha um dos animais (Gato, Cachorro ou Pato): ').strip().capitalize()

    if meu_bichinho == 'Gato':
        meu_bichinho = Gato()
        print(f'Parabens pelo animalzinho: {meu_bichinho.falar()}')
        break
    
    elif meu_bichinho == 'Cachorro':
        meu_bichinho = Cachorro()
        print(f'Parabens pelo animalzinho: {meu_bichinho.falar()}')
        break
    
    elif meu_bichinho == 'Pato':
        meu_bichinho = Pato()
        print(f'Parabens pelo animalzinho: {meu_bichinho.falar()}')
        break
    else:
        print(f'Não temos esse bichinho: {meu_bichinho}')


        
        
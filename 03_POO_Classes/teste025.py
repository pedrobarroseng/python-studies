class poderes:

    def __init__(self, nome, poder, vida):
        self.nome = nome
        self.poder = poder
        self.vida = 100
    
    def mostrar_status_heroi(self):
        print(f"O herói {self.nome} tem {self.poder} e {self.vida} de vida.")

    def mostrar_status_vilao(self):
        print(f"O vilão {self.nome} tem {self.poder} e {self.vida} de vida.")
        
super_heroi = poderes('Barman', 'super velocidade', '100')
vilao = poderes('Megamente maligna', 'Super inteligência', '100')

print(f'Meu nome é {super_heroi.nome} e meu poder é {super_heroi.poder}. Minha vida é {super_heroi.vida}')
print(f'Meu nome é {vilao.nome} e meu poder é {vilao.poder}. Minha vida é {vilao.vida}')

super_heroi.mostrar_status_heroi()
vilao.mostrar_status_vilao()



    
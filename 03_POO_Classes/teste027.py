import random # 1. IMPORTAMOS A FERRAMENTA DE SORTE

# --- MOLDES (CLASSES) ---
class Personagem:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
        self.vida = 100 # Começam com 100 de vida

    def atacar(self, inimigo):
        # --- NOVIDADE AQUI ---
        # Sorteia um dano entre 5 (raspão) e 25 (crítico)
        dano = random.randint(5, 25) 
        
        inimigo.vida = inimigo.vida - dano
        
        # Lógica visual para ficar emocionante
        if dano > 20:
            print(f"🔥 CRÍTICO! {self.nome} espancou {inimigo.nome} com {self.poder} tirando {dano} de dano!")
        elif dano < 10:
             print(f"💨 RASPÃO... {self.nome} acertou {inimigo.nome} de leve tirando só {dano}.")
        else:
            print(f"👊 {self.nome} atacou {inimigo.nome} tirando {dano} de dano.")

# Herança (Filhos)
class Heroi(Personagem):
    pass

class Vilao(Personagem):
    pass

# --- CRIAÇÃO DOS OBJETOS ---
batman = Heroi("Batman", "Soco Rico")
coringa = Vilao("Coringa", "Pé de Cabra")

# --- O LOOP DA BATALHA (O FINAL DO EXERCÍCIO ANTERIOR) ---
print("--- 🔔 ROUND 1 - FIGHT! ---")

# Enquanto os dois estiverem vivos...
while batman.vida > 0 and coringa.vida > 0:
    
    # 1. Turno do Herói
    batman.atacar(coringa)
    
    # Verificamos se o vilão morreu antes de deixar ele revidar
    if coringa.vida <= 0:
        break # Quebra o loop imediatamente
        
    # 2. Turno do Vilão
    coringa.atacar(batman)
    
    print(f"   [PLACAR] Batman: {batman.vida} | Coringa: {coringa.vida}\n")
    
    # (Opcional) Pausa dramática de 1 segundo (precisa de 'import time' lá em cima se quiser usar)
    # time.sleep(1) 

print("--- 🏁 FIM DA LUTA ---")

# Quem sobrou em pé?
if batman.vida > 0:
    print(f"🏆 O VENCEDOR É: {batman.nome} com {batman.vida} de vida restante!")
else:
    print(f"☠️ O VENCEDOR É: {coringa.nome} com {coringa.vida} de vida restante!")
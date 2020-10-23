class Pokemon():
    
    def __init__(self, vida, ataque):
        self.vida=vida
        self.ataque=ataque

    def atacado(self,Pokemonatacante):
        self.vida=self.vida-Pokemonatacante.ataque    
        
Pikachu=Pokemon(100,55)
Jigglypuff=Pokemon(100,45)

Turno=1

while Pikachu.vida>0 and Jigglypuff.vida>0:
    if Turno==1:
        Jigglypuff.atacado(Pikachu)
        Turno=0
        
    else:
        Pikachu.atacado(Jigglypuff)
        Turno=1    
        
if Pikachu.vida>0:
    print("Ha ganado Pikachu")
else:
    print("Ha ganado Jigglypuf")
        

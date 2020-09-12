class Pokemon1():
    vida=100
    ataque=55 
    def atacado(self):
        self.vida=self.vida-45
       
class Pokemon2():
    vida=100
    ataque=45
    def atacado(self):
        self.vida=self.vida-55        

Picachu=Pokemon1()
Jigglypuff=Pokemon2()

Turno=1

while Picachu.vida>0 and Jigglypuff.vida>0:
    if Turno==1:
        Jigglypuff.atacado()
        Turno=0
        
    else:
        Picachu.atacado()
        Turno=1    
        
if Picachu.vida>0:
    print("Ha ganado Picachu")
else:
    print("Ha ganado Jigglypuf")
        


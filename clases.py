class MiClase:
    def __init__(self, x=2):
        self.x = x
        
    def devuelve_valor(self):
        return self.x
    
objeto = MiClase()

print(objeto.devuelve_valor())
print(dir(MiClase))

objeto = MiClase(5)
print(objeto.devuelve_valor())

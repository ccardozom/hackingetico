class Prueba:
    def __init__(self):
        self.__x = 4
        self.y = self.__x*2
        
    def getX(self):
        return self.__x
    
if __name__=='__main__':
    objeto1 = Prueba()
    
    print(objeto1.y)
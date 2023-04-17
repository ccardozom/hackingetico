
class CuentaBancaria:
    def __init__(self, titular, numeroCuenta, saldo):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.__saldo = saldo
        self.movimientos = []
    
    def hacerIngresos(self, ingreso):
        print(f"Has realizado un ingreso de {ingreso}€ correctamente.")
        self.__saldo = self.__saldo + ingreso
        print("Su saldo actualizado es de {}".format(self.__saldo))
        self.movimientos.append(f"Ingreso: {ingreso}€")
        
    def retirarDinero(self, retiro):
        if retiro > self.__saldo:
            print("No tiene suficiente saldo para realizar el retiro.")
            return False
        else:
            print("Retire su dinero...")
            self.__saldo = self.__saldo - retiro
            print(f"Su saldo es de {self.__saldo}")
            self.movimientos.append(f"Retiro: {retiro}€")
            
    def consultaSaldo(self):
        print("Consulta de saldo de {}".format(self.titular))
        print("Su saldo actual es de {}".format(self.__saldo))
        
    def movimientoCuenta(self):
        print(f"Movimientos de la cuenta de {self.titular}")
        for elemento in self.movimientos:
            print(elemento)

def main():
    cliente1 = CuentaBancaria("Carlos Cardozo", 10025001, 0)
    cliente1.hacerIngresos(200)
    cliente1.consultaSaldo()
    cliente1.retirarDinero(50)
    cliente1.consultaSaldo()
    cliente1.movimientoCuenta()
    
#7608271
if __name__=='__main__':
    main()
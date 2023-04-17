import argparse

class Parameters:
    def __init__(self, **kwargs):
        self.param1 = kwargs.get("ip")
        self.param2 = kwargs.get("puerto")
        
    def view_parameters(self): # añadir self como primer argumento
        print(self.param1)
        print(self.param2)

parser = argparse.ArgumentParser(description='Paso de parametros')
parser.add_argument("-p", dest="puerto", type=int)
parser.add_argument("-ip", dest="ip", type=str)
params = parser.parse_args()
input_parameters = Parameters(puerto=params.puerto, ip=params.ip) # corregir atributos
input_parameters.view_parameters()
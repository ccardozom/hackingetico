#coding=utf-8
#un tipo diccionario permite asociar valores con claves. Se puede acceder al valor de una clave con el operador de indexación []
#definimos un diccionario y accedemos a claves y valores a traves de los métodos keys() values() items()
diccionario = {'ip':'192.168.1.1', 'port':'443', 'state':'open'}
print(diccionario)
print(diccionario['ip'])
print(diccionario['port'])
print(diccionario['state'])
claves = diccionario.keys()
valores = diccionario.values()
print(claves)
print(valores)
for clave,valor in diccionario.items():
    print(clave + ' --> ' + valor)

iterador = iter(diccionario)
try:
    for item in iterador:
        print(item)
        print(item[iterador])
except:
    print("No se puede leer el diccionario")
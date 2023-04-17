#coding=utf-8
#una tupla es como una lista pero su tamaño y sus elementos son inmutables, es decir, no se pueden cambiar ni tampoco añadir elementos
#para definir una tupla lo hacemos con parentesis
tupla = ('192.168.1.1', '192.168.1.2')
try:
    print(tupla[0])
    tupla[0] = '192.168.1.3' # esto genera un error indicando que la tupla no soporta la asignación de elementos
except TypeError:
    print("El objeto es una tupla y no soporta modificaciones")
    
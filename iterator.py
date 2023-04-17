# coding=utf-8
#una estructura de datos es iterable si es capaz de proporcionar un iterador; si invocamos iter() sobre una lista obtenemos un objeto del tipo listitertor
iterator = iter(['python', 'java', 'c++'])
print(iterator)
for element in iterator:
    print(element)

#el iterador permite recorrer los elementos del objeto por medio del metodo next(), al finalizar el recorrido next provoca una excepción StopIteration
try:
    iterator = iter(['python', 'java', 'c++'])
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())  #--> el iterador esta apuntando al final del objeto por lo que al llamar a print genera una excepción StopIteration
except StopIteration:       # con try y except capturamos el error StopIteration que tira el iterador y asi lo podemos controlar
    print("Error StopIteration: porque ya no existen elementos en el objeto para seguir iterando")
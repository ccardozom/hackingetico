# coding=utf-8
#una lista equivale a una estructura como un vector dinamico, sus elementos están entre un par de corchetes [] y separados por comas ,
lista = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
#para verificar el tipo de la variable utilizamos el comando type(<nombre_de_la_variable>)
print(type(lista))

print("Antes") 
print(lista)

#para este ejemplo vamos a utilizar metodos de la lista para insertar y eliminar elementos. append - insert - delete
lista.append('192.168.1.4')
print("Despues") 
print(lista)
lista.insert(4,'192.168.1.5')
print("Despues") 
print(lista)
print("La lista tiene " + str(len(lista)) + " elementos")
print("Usamos \"del\" para eliminar un elemento, en este caso el elemento con indice 1")
del lista[1]
print("Entonces la lista anterior quedaria de esta forma") 
print(lista)

#podemos concatenar dos o mas listas utilizando el simbolo +
lista1 = ['192.168.1.6']
print(lista + lista1)

#una lista es iterable y se puede recorrer con un bucle for
print("Los elementos de la lista son: ")
for elemento in (lista+lista1):
    print(elemento)
    
#para dar la vuelta la lista podemos utilizar el método reverse
lista.reverse()
reverse = lista
print(lista)


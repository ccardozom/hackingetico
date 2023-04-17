f = open('fichero', 'w')
f.write('fichero abierto en modo escritura\n')
f.write('por defecto se trata como un fichero de texto')
f.close()

for line in open('fichero'):
    print(line)
    
f = open('fichero', 'w')
f.write('se sobreescribe los datos del fichero')
f.close()

for line in open('fichero'):
    print(line)
    
f = open('fichero', 'a')
f.write(" y se añaden datos")
f.close()

for line in open('fichero'):
    print(line)
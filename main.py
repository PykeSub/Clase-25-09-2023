from Auto import Auto
# Genero un objeto, referencia, instancia.
autito1 = Auto('rojo', 'toyota', 2000, 1.4, 'VICE12')
color = input('Ingrese color: ')
marca = input('Ingrese marca: ')
autito2 = Auto(color, marca, 2002, 1.6, 'LUCI13')
print('El auto 1: ')
print(autito1)
autito1.color = 'Verde'
autito1.set_patente('JOSE14')
print('El auto 1 : ')
print(autito1)
print('Autito 2: ')
print(autito2)
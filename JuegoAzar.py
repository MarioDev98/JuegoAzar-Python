import random

numero=random.randrange(1,1000)
# print(numero) linea para saber que numero es para casos de pruebas
respuesta=int(input('Dime el número que he elegido: '))
contador = 0
while respuesta!=numero:
    contador=contador+1
    if respuesta>numero:
      respuesta=int(input('El número que buscas es  mas pequeño al que ingresaste : '))
    elif respuesta<numero:
      respuesta=int(input('El número que buscas  es mas grande al que ingresaste : '))
print("\nFelicidades le atinaste al numero que se buscaba")
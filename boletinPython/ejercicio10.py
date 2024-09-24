lista = [1,5,7,10,12]

sumatorio = 0

for i in lista:
    sumatorio += i

sumatorio /= len(lista)

print("El promedio de la lista es: " + str(sumatorio))
num = 5
sumatorio = 1
i = num

while i > 1:
    sumatorio *= i
    i -= 1
    
print("El factorial de " + str(num) + " es: " + str(sumatorio))
#Ejercicio 1
for n in range(10):
    print (n)

print(list(range(10)))

#Ejercicio 2
for n in range(100,200):
    print (n)

print(list(range(100,200)))

#Ejercicio 3
for n in range(5,21,3):
    print(n)

print(list(range(5,21,3)))

#Ejercicio 4
n = int(input("Ingrese un numero entero positivo, número = "))
for x in range(n,n*2):
    print(x)

#Ejercicio 5 - 6
vocala = ''
vocale = ''
vocali = ''
vocalo = ''
vocalu = ''

def buscar_vocal(caracter):

    global vocala
    global vocale
    global vocali
    global vocalo
    global vocalu

    if caracter == 'a' or caracter == 'A':
        vocala = 'a'

    if caracter == 'e' or caracter == 'E':
        vocale = 'e'

    if caracter == 'i' or caracter == 'I':
        vocali = 'i'

    if caracter == 'o' or caracter == 'O':
        vocalo = 'o'

    if caracter == 'u' or caracter == 'U':
        vocalu = 'u'


cadena_frase = input("Ingrese una frase: ")

#Este FOR recorre los caracteres de la frase digitada ( UNO a UNO )
for n in cadena_frase:
    # n toma la letra de cada posición, y la envía a la funcion buscar_vocal
    buscar_vocal(n)

if vocala  + vocale + vocali + vocalo + vocalu == '':
    print("NO EXISTEN VOCALES")
else:
    print("Las vocales de la frase son : ", vocala + ' ' + vocale + ' '+ vocali + ' '+ vocalo + ' '+ vocalu)

#Ejercicio 7
suma = 0
for n in range(0,101):
    print(n)
    suma = suma + n
print("La sumatoria total es = " ,suma)


#Ejercicio 8
initialyear=int(input("Ingresa en año inicial: "))
finalyear=int(input("Ingresa en año final: "))
for year in range(initialyear, finalyear+1):
    if not year%10==0:
        continue
    if not year%4==0:
        continue
    if year%100!= 0 or year%400==0:
        print(year)


#Ejercicio 9
n = int(input("Ingresa un número entero positivo "))
factorial = 1
if n != 0:
    for i in range(1, n + 1):
        factorial = factorial * i
    print("El factorial de número ingresado es:" ,factorial)

#Ejercicio 10
numerofibonacci = ''
n_anterior = 0
suma = 0
suma_anterior = 0

for x in range(0,10):

    if x == 0 or x == 1:
        numerofibonacci = numerofibonacci + str(x) + ','
        n_anterior = x
    else:
        suma_anterior = suma
        suma = suma + n_anterior

        if x != 9:
            numerofibonacci = numerofibonacci + str(suma) + ','
        else:
            numerofibonacci = numerofibonacci + str(suma)

        if n_anterior != suma:
            n_anterior = suma_anterior

print("Los 10 primeros numeros de la cadena fibonacci son =", numerofibonacci)


























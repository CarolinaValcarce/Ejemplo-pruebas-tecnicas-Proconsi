import math

def is_Kaprekar_number(digit):

    SquareDigit=digit**2

    SquareDigitSt=str(SquareDigit)
    array=[]
    for item in SquareDigitSt:
        array.append(item)
    '''Del número hayamos el cuadrado y lo pasamos a string.
    Creamos un arreglo vacío y lo rellenamos con los dígitos del número 1 a 1.
    Hayamos la mitad de la longitud del array y cogemos por defecto el redondeo.
    Así si el número de dígitos de los elementos del arreglo es par, cogemos la exacta mitad, y si es impar, cogemos la mitad por defecto porque será flotante.'''
    lenhalfarray=math.floor((len(array)/2))

    halfarray=[]
    for i in range(0,lenhalfarray): 
        halfarray.append(array[i])
    Sthalfarray="".join(halfarray)
    '''Creamos un arreglo vacío, al que añadiremos como elementos la mitad de los dígitos por defecto del arreglo inicial.
    Y luego pasamos el arreglo a String con todos los elementos juntos.'''

    halfarray2=[]
    for i in range(lenhalfarray,len(array)):
        halfarray2.append(array[i])
    Sthalfarray2="".join(halfarray2)   
    '''Hacemos la misma operación con el segundo arreglo creado con la segunda mitad del arreglo original.
    También trasformamos el arreglo  en String con todos los elementos juntos.'''

    kaprekar=int(Sthalfarray)+int(Sthalfarray2)
    '''Sumamos las dos mitades pasadas previamente de string a entero.'''
    if kaprekar==digit:
        print(f'El número {digit} es un KAPREKAR porque: el cuadrado de {digit} es {SquareDigitSt} y la suma de sus dos descomposiciones de dígitos: {Sthalfarray}+{Sthalfarray2} es {kaprekar}.')
    else:
        print('El número no es Kaprekar')

print('---------------------------------o----------------------------------------')
print('---------------------------------o----------------------------------------')
print('                 ADIVINA NÚMEROS KAPREKAR (10 intentos)                   ')
print('---------------------------------o----------------------------------------')
print('---------------------------------o----------------------------------------')

'''Llamamos a la función creada desde la main, representada por la indexación.'''
for i in range(0,10):
    try:
        n=int(input('Dame un número para decirte si es kaprekar: '))
        is_Kaprekar_number(n)
    except:
        print('Debes introducir un número entero positivo para adivinar si es Kaprekar.')
print('GRACIAS POR JUGAR')

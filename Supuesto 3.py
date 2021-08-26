import time

text="Java es un lenguaje de programación y una plataforma informática que fue comercializada por primera vez en 1995 por Sun Microsystems.Hay muchas aplicaciones y sitios web que no funcionarán, probablemente, a menos que tengan Java instalado y cada día se crean más. Java es rápido,seguro y fiable."
print("El número de caracteres del texto es de: ",len(text))
print("***********************************************************")
print(text.upper())
print("***********************************************************")
print(text.lower())
print("***********************************************************")
print(text.replace("Java","Avaj"))
print("***********************************************************")

'''Para encontrar el número de palabras repetidas, primero pasamos todo el texto a minúsculas.
(Sino diferenciaría dos palabras por estar la primera con mayúsculas). Y quitamos puntos y comas.
Luego recogemos las palabras dividiendo el texto. Y creamos dos arreglos vacíos que contendrán palabras repetidas
y número de repeticiones. Estos dos arreglos siempre tendrán mismo número de elementos. De forma,
que la posición 2 del primer arreglo se repetirá tantas veces como indique la posición 2 del segundo arreglo.'''
textmodified=text.lower().replace(",","")
textmodified2= textmodified.replace(".","")
words=textmodified2.split()
frequency=[]
repeated=[]
for word in words:
    if words.count(word)>1:
        repeated.append(word)
        frequency.append(words.count(word))
'''Creamos otros 2 arreglos vacíos, en este caso para crear unicidad de las palabras repetidas,
ya que en el primer arreglo ponía las palabras repetidas cada vez que aparecían.
Habiendo elementos repetidos en el arreglo. Estos arreglos tienen las palabras repetidas una sola vez, la primera.
También recortamos el arreglo de la frecuencia, con la dimensión de los primeros elementos de la talla del arreglo con unicidad de palabras.
Por último, imprimimos, el número de palabras repetidas, las palabras repetidas y cada palabra cuantas veces se repite.''''
frequency2=[]
repeated2=[]

for item in repeated:
    if item not in repeated2:
        repeated2.append(item)
for i in range (0,len(repeated2)):
    frequency2.append(frequency[i])
    
print("El número de palabras repetidas es: ",len(repeated2))
print("Las palabras que se repeten en el texto son: ",repeated2)
for i in range (0,len(repeated2)):
    print(f"La palabra: '{repeated[i]}' se repite {frequency2[i]} veces.")
print("***********************************************************")

initialT=time.time()
newText=text*1000
'''A primera vista parecería un error el que tardase 0 segundos pero Python es rápido.
Si ponemos de prueba la siguiente linea de código junto con la anterior, veremos que:
en repetir el texto 1000 veces y en crear lista de los números pares del primer millón de números tarda: 1 segundo y poco.
list=[i for i in range(0,1000000) if i%2==0]'''
finalT=time.time()

print(f"La longitud del texto concatenado 1000 veces es {len(newText)}")
print(f"En concatenar el texto inicial 1000 veces he tardado {finalT-initialT} segundos.")




        
    
    

import math

def operation(number1, number2, number3):
    if number3>=0 and number2!=0:
        addition=number1+number2
        substraction=number1-number2
        product=number1*number2
        division= number1/number2
        modul=number1%number2
        '''Creamos la función con 3 parámetros de entrada que son los introducidos por consola por el usuario.
        Recogemos las excepciones de que no introduzca números, o que se divida entre 0.
        Si el resultado de la operación es mayor que el número3 elegido, redondeamos el resultado a la baja.
        Y en caso contrario, a la alta.'''
        
        if addition>number3:
            addition=math.floor(addition)
        else:
            addition=math.ceil(addition)
        if substraction>number3:
            substraction= math.floor(substraction)
        else:
            substraction= math.ceil(substraction)
        if product>number3:  
            product=math.floor(product)
        else:
            product=math.ceil(product)
        if division>number3:
            division= math.floor(division)
        else:
            division=math.ceil(division)
        if modul>number3:   
            modul=math.floor(modul)
        else:
            modul= math.ceil(modul)
        if number1>number2:
            solution="El primer número es mayor que el segundo"    
        elif number1<number2:
            solution="El primer número es menor que el segundo"    
        else:
            solution="El primer número y el segundo son iguales"

        print("*************************************************************************")
        print("La suma del primer número y el segundo redondeada al tecer número es: ",addition)
        print("La resta del primer número menos el segundo redondeada al tecer número es: ",substraction)
        print("El producto del primer número por el segundo redondeado al tecer número es: ",product)
        print("La division del primer número entre el segundo redondeada al tecer número es: ", division)
        print("El resto de la división del primer número entre el segundo redondeado al tecer número es: ",modul)
        print(solution)

    else:
        print("Elige un segundo número distinto de 0 para poder dividir y un tercer número positivo para realizar el redondeo")

try:
    first_number= float(input("Dame un primer número: "))
    second_number= float(input("Dame un segundo número distinto de 0: "))
    third_number= float(input("Dame un tercer número positivo: "))
    operation(first_number,second_number,third_number)
except:
    print("Sólo se aceptan números: ni palabras ni signos")

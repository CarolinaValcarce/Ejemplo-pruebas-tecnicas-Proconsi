from datetime import date
from calendar import isleap

try:
    '''Recogemos la excepción si no se ofrece una fecha en ese formato
    o si la segunda fecha no es anterior a la primera.
    Mapeamos la fecha recogiendo en nuevas variables el entero que indica, mes, año y día.
    Creamos nuevas variables, fecha dada en otro formato, Año Nuevo de ese mismo año y Nochevieja también de ese año.
    Para la segunda fecha que introduce el usuario por consola, hacemos lo mismo.'''
    
    date1= input("Dame la fecha más reciente en formato (YYYY/MM/DD): ")
    year, month, day= map(int, date1.split("/"))

    dateA= date( year, month, day)
    NewYearA=date(year,1,1)
    YearEveA=date (year,12,31)
    n_weekA=date(year,month,day).isocalendar()[1]

    date2=input("Dame una segunda fecha más antigua en formato (YYYY/MM/DD): ")
    year, month, day= map(int, date2.split("/"))

    dateB= date( year, month, day)
    NewYearB=date(year,1,1)
    YearEveB=date (year,12,31)
    n_weekB= date(year,month,day).isocalendar()[1]
    
    '''Imprimimos las diferencias de días y meses que nos pide el enunciado. La clase datetime en el formato date
    tomado nos proporciona los atributos: days, months o years. Además como hemos importado la librería calendario
    nos recoge isleap() como función del año bisiesto.'''
    
    print("")
    print("El número de días entre las 2 fechas es:",(dateA-dateB).days)

    print("******************DESDE LA PRIMERA FECHA************************")
    print("Han pasado ",(dateA.month-NewYearA.month)," meses y ",(dateA.day-NewYearA.day)," días desde Año Nuevo")
    print ("Quedan ",(YearEveA.month-dateA.month), "meses y ",(YearEveA.day-dateA.day)," días para Noche Vieja")
    print("******************DESDE LA SEGUNDA FECHA************************")
    print("Han pasado ",(dateB.month-NewYearB.month)," meses y ",(dateB.day-NewYearB.day)," días desde Año Nuevo")
    print ("Quedan ",(YearEveB.month-dateB.month), "meses y ",(YearEveB.day-dateB.day)," días para Noche Vieja")
    print ("***************************************************************")
    print("El número de días del año de la primera fecha es: ",((YearEveA-NewYearA).days)+1)
    if isleap(year):
        print("Y el año", year,"es bisiesto")
    print("El número de días del año de la segunda fecha es: ",((YearEveB-NewYearB).days)+1)
    print("****************************************************************")
    print("El número de la semana de la primera fecha es: ",n_weekA)
    print("El número de la semana de la segunda fecha es: ",n_weekB)

except:
    print("No me has dado alguna de las fechas en formato: (YYYY/MM/DD)")

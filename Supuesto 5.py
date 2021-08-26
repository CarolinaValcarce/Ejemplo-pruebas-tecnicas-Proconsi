from tkinter import *
import random
from tkinter.messagebox import showwarning
import math
'''Importamos las librerías: tkinter para la UI, messagebox para las ventanas de aviso,
    random para elección de números aleatorios y math para operaciones matemáticas.
    Creamos título y tamaño de la primera ventana.'''

root=Tk()
root.title('FIGURAS GEOMÉTRICAS')
root.geometry('800x550+100-120')



def draw_rectangule(lateral):
    x1=random.randrange(40,300,5)
    y1=random.randrange(40,250,5)
    x2=x1
    y2=y1+lateral
    x3=x2+lateral
    y3=y2
    x4=x3
    y4=y1
    '''El polígono se crea con las coordenadas de todos sus vértices.
    Busco su relación con el parámetro de entrada que es el 'lado',
    ya que luego lo necesitaremos para calcular su área.'''
    c.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, outline="red", fill='')
    
def draw_triangule(base, height):
    x1=random.randrange(40,300,5)
    y1=random.randrange(40,200,5)
    x3=x1+height
    x2=x1
    y2=y1+base
    y3=(y2-y1)/2
    '''Como es un triángulo, el polígono se crea con las coordenadas de sus 3 vértices.
    Introduzco de parámetro base y altura y busco su relación con las coordenadas.
    Porque más tarde lo necesitaremos para calcular el área.'''
    c.create_polygon(x1,y1,x2,y2,x3,y3, outline="blue", fill='')

def draw_circle(radious):

    x1=random.randrange(50,300,4)
    x2=abs(x1-2*radious)
    y1=x1
    y2=x2
    '''Al crear el óvalo, si hacemos x1=y1 y x2=y2, será un círculo perfecto en lugar de un óvalo.
    Las coordenadas son el cuadrado imaginario dónde se enmarca el círculo. Su esquina inferior izquierda y la superior derecha.
    Hacemos todas las figuras huecas porque sino al superponerse muchas no se verían o contarían.'''
    c.create_oval(x1,y1,x2,y2, outline="yellow", fill='')
    
def rectangules():
    try:
        '''Llamamos a la función de dibujar rectángulos tantas veces como veces hayamos recogido en el campo de n de rectángulos.
        Creamos valores de lado aleatorios y calculamos área sobre los valores escogidos mostrándolo en la etiqueta.'''
        n_rectang=e_rectangule.get()
        l=random.randint(25,35)
        for i in range(0,int(n_rectang)):
            draw_rectangule(l)
        area=l**2
        area_rectang=Label(c, text='Área de cada cuadrado='+str(area)).place(x=400, y=80)
    except:
        showwarning(title='ATENCIÓN', message='Introduce el número de rectángulos a dibujar antes de presionar el botón')

def triangules():
    try:
        '''Recogemos el valor introducido en campo de n triángulos.
        Elegimos valores de base y altura aleatoriamente pero con valores no muy pequeños o excesivamente grandes y que no entren en el lienzo.
        Pedimos que se repita la funcición de crear triángulos con límite máximo del número dado de triángulos a dibujar.
        Creamos la fórmula del área con los valores de base y altura aleatorios y
        la mostramos en una etiqueta incorporada dentro del lienzo, en vez de en la ventana general.
        Recogemos la excepción si presiona solo letras o no introduce nada en los campos.'''
        n_triang= e_triangule.get()
        b=random.randint(15,30)
        h=random.randint(25,30)
        for i in range(0, int(n_triang)):
            draw_triangule(b,h)
        area=(b*h)/2
        area_triang=Label(c, text='Área de cada triángulo='+str(area)).place(x=400, y=160)
    except:
        showwarning(title='ATENCIÓN', message='Introduce el número de triángulos a dibujar antes de presionar el botón')

def circles():
    try:
        '''De la misma forma que creamos la función 'triangules' creamos 'circles', llamando a dibujar círculos y creando etiqueta para mostrar área con radio elegido aleatoriamente.'''
        n_circ=e_circle.get()
        r=random.randint(4,18)
        for i in range (0,int(n_circ)):
            draw_circle(r)
        area=math.pi*r**2
        area_circ=Label(c, text='Área de cada círculo='+str(area)).place(x=400, y=240)
    except:
        showwarning(title='ATENCIÓN', message='Introduce el número de círculos a dibujar antes de presionar el botón')

def allFigures():
    '''LLamamos a las 3 funciones para dibujar todo'''
    circles()
    triangules()
    rectangules()
    
            
'''Creamos en la main, la interfaz gráfica: etiquetas, botones y campos de entrada, y lo colocamos con place() en lugar de pack().
El  lienzo Canvas lo podemos colocar con pack(), porque es un marco divisorio de la ventana Tk(). A su  vez, dentro del canvas podemos usar place().'''
    
l=Label(root, text='Elige número de triángulos:').place(x=70, y=500)
e_triangule= Entry(root, width=10)
e_triangule.place(x=300, y=500)
l2=Label(root, text='Elige número de círculos:').place(x=70, y=450)
e_circle= Entry(root, width=10)
e_circle.place(x=300, y=450)
l3=Label(root, text='Elige número de rectángulos:').place(x=70,y=400)
e_rectangule= Entry(root, width=10)
e_rectangule.place(x=300, y=400)

c=Canvas(root, bg="tan", height=320, width=750)

b1=Button(root, bd=5, text='Dibujar todo', command=allFigures).place(x=70, y=350)
b2=Button(root, bd=5, text='Dibujar solo círculos',command=circles).place(x=220, y=350)
b3=Button(root, bd=5, text='Dibujar solo rectángulos', command=rectangules).place(x=400, y=350)
b4= Button(root, bd=5, text='Dibujar solo triángulos', command=triangules).place(x=600, y=350)

c.pack()
root.mainloop()
'''Creamos el mainloop() sino tkinter no funcionaría. Al no interaccionar.'''

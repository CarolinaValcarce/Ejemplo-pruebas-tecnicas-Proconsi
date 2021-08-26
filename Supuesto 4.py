from tkinter import *
import sqlite3
from tkinter.messagebox import showwarning,showerror
from datetime import date, datetime
#Importamos las librerías. Usaremos como bbdd sqlite3 que trabaja en local, para UI tkinter, para mensajes messagebox y datetime para el formato fecha.

r=Tk()
r.title('AGENDA de CLIENTES')
r.geometry('770x450+50+20')
r.configure(bg='light slate grey')
#Configuramos, color, tamaño y título de la UI

connection=sqlite3.connect('AgendaProconsi.db')
c= connection.cursor()

def get_customer():
    e_typeCustomer.delete(0,END)
    e_typeCustomer.insert(0, radioValue.get())
    #Función que nos permite borrar el campo cliente e insertar el valor del radioButton elegido.

def save():

    '''Creamos una conexion a bd llamada AgendaProconsi que creamos en sqlite (previamente importada la librería)
    y creamos una tabla posicionando cursor en 0.'''
    try:
        connection=sqlite3.connect('AgendaProconsi.db')
        c= connection.cursor()
        #c.execute ('DROP TABLE Clientes')
        c.execute ('''CREATE TABLE IF NOT EXISTS Clientes(DNI INTEGER PRIMARY KEY,nombre TEXT, tipoCliente TEXT,
                    fechaAlta TEXT)''')


        #Insertamos los datos en la tabla creada usando query SQL
        DNI=e_DNI.get()
        entryDate=e_entryDate.get()
        if((len(DNI)==8 or len(DNI)==7)):
            c.execute('INSERT INTO Clientes VALUES(?,?,?,?)',
              (e_DNI.get(),e_name.get(),e_typeCustomer.get(), e_entryDate.get()))
        else:
            showerror (title= 'ATENCIÓN!!', message='El DNI esta formado por 8 digitos o 7 si es de extranjero.')

        #Borramos los campos, una vez introducida la info
        e_DNI.delete(0,END)
        e_name.delete(0,END)
        e_typeCustomer.delete(0,END)
        e_entryDate.delete(0,END)
        e_entryDate.insert(0,datestamp)
        
        #Hacemos el commit, para confirmar las operaciones
        connection.commit()
        
    except Exception as exct:
        showerror(title='ATENCIÓN', message='Ya existe un cliente con ese DNI. Corrige el DNI erroneo antes')

def query2():
    try:
        connection=sqlite3.connect('AgendaProconsi.db')
        c= connection.cursor()
        #Selecciona los valores de atributos de la bbdd y les vuelca en records.Ordenamos records por cada valor de fecha en record pasando el string a datetime.
        c.execute('SELECT * FROM Clientes')
        records=c.fetchall()
        
        ordered_records2=sorted(records, key=lambda record: (datetime.strptime(record[3],'%d/%m/%Y %H:%M:%S')))
        print(ordered_records2)
        
        print_records=''
        for record in ordered_records2:
            print_records+=str(record)+'\n'
            #Creamos una variable print_records que recoge cada record con salto de línea. Y creamos etiqueta para verlos.
        l_query=Label(r, text='       '+print_records+'      ').grid(row=9,column=0, columnspan=3)

        connection.commit()

    except Exception as ex:
        showwarning (title='ATENCIÓN', message='Todavia no existe ningun cliente.'
                     ' O has guardado un cliente con fecha de alta en formato incorrecto. Aconsejamos que borres ese cliente, y vuelvas a listar por fecha')
    
def query():
    try:
        connection=sqlite3.connect('AgendaProconsi.db')
        c= connection.cursor()
        #c.execute ('PRAGMA foreign_keys=ON')

        c.execute('SELECT * FROM Clientes')
        records=c.fetchall()
        print(records)
        ordered_records=sorted(records, key=lambda record :record[0])
        print(ordered_records)
        #Hacemos lo mismo que en el método anterior pero con la primer atributo de la bbdd, el DNI
        print_records=''
        for record in ordered_records:
            print_records+=str(record)+'\n'
        l_query=Label(r, text='       '+print_records+'      ').grid(row=9,column=0, columnspan=3)

        connection.commit()

    except Exception as ex:
        showwarning (title='ATENCIÓN', message='Todavia no existe ningun cliente.')


def delete():

    try:
        connection=sqlite3.connect('AgendaProconsi.db')
        c= connection.cursor()
        #Borramos el cliente cuyo DNI hayamos elegido previamente.
    
        c.execute('DELETE FROM Clientes WHERE DNI='+e_selection.get())
    except Exception as e:
        showwarning(title='ATENCIÓN!!!', message='Da "Listar clientes" y selecciona un cliente existente rellenando "Elegir DNI", antes de presionar "Borrar datos".')
    e_selection.delete(0,END)
    connection.commit()
    
def update():
  
    connection=sqlite3.connect('AgendaProconsi.db')
    c= connection.cursor()
    
    DNI_editor=e_DNI_editor.get()
   
    if((len(DNI_editor)==8 or len(DNI_editor)==7)):
    
         c.execute('UPDATE Clientes SET DNI=(?),nombre=(?), tipoCliente=(?), fechaAlta=(?) WHERE DNI=(?)',
          (e_DNI_editor.get(),e_name_editor.get(),customer.get(),e_entryDate_editor.get(), e_selection.get()))  
           #Actualizamos los valores del cliente con los introducidos en la UI de edición de valores. Nótese que se podría modificar la clave primaria incluso si nos equivocasemos. 
    else:
        showwarning (title= 'ATENCIÓN!!', message='El DNI contiene 8 digitos o 7 si es de extranjero.')

    #Tras actualizar quitamos la UI creada para editar datos.
    connection.commit()
    editor.destroy()

def get_choice():
    e_tCustom_editor.delete(0, END)
    e_tCustom_editor.insert(0, customer.get())
    #Recuadro del cliente que rellenamos en la pantalla de editar pulsando el radioButton Registrado o Socio.

def edit():

    global e_DNI_editor
    global e_name_editor
    global e_tCustom_editor
    global e_entryDate_editor
    global customer
    customer=StringVar()
    #Creamos variables globales para poder acceder a ellas desde cualquier función.
    
    try:
        connection=sqlite3.connect('AgendaProconsi.db')
        c= connection.cursor()
        #Como siempre nos conectamos con la bbdd situamos el cursor y seleccionamos todos los campos donde el DNI sea el introducido.

        c.execute('SELECT * FROM Clientes WHERE DNI='+e_selection.get())
        records=c.fetchall()

        global editor
        #Creamos un tk() de nivel superior llamado Toplevel que tiene completa funcionalidad, para crear la edición de datos.
        editor=Toplevel()
        editor.title('Editar datos de cliente')
        editor.geometry('700x450')
        editor.configure(bg='light slate grey')
      
        l_welcome_editor= Label(editor, text="EDICIÓN DE CLIENTES PROCONSI:", bg='light slate grey', fg='white').grid(row=0,column=1, padx=10, pady=20)
        l_DNI_editor=Label(editor, text='DNI sin letra ni espacios:',bg='light slate grey',fg='white').grid(row=1, column=0, padx=5, pady=5)
        e_DNI_editor= Entry (editor, width=65)
        e_DNI_editor.grid (row=1,column=1, columnspan=2)
        e_name_editor=Entry(editor, width=65)
        e_name_editor.grid(row=2, column=1, columnspan=2)
        l_name_editor=Label(editor, text='Nombre y Apellidos: ',bg='light slate grey',fg='white').grid(row=2, column=0,padx=5, pady=5 )

        l_tCustom_editor=Label(editor, text='Tipo de Cliente: ',bg='light slate grey',fg='white').grid(row=3, column=0,padx=5, pady=5)

        e_tCustom_editor=Entry(editor, width=65)
        e_tCustom_editor.grid(row=4, column=1,columnspan=2 )
        #Creamos todos los campos, botones y etiquetas de la nueva UI para edición de datos
        rb_registered_editor= Radiobutton(editor, text='REGISTRADO', value="REGISTRADO", variable=customer, command=get_choice).grid(row=3, column=0, columnspan=2)
        rb_membership_editor= Radiobutton(editor, text='SOCIO', value="SOCIO", variable=customer, command=get_choice).grid(row=3, column=1, columnspan=2)

        e_entryDate_editor=Entry(editor, width=65)
        e_entryDate_editor.grid(row=5, column=1,columnspan=2 )
        l_entryDate_editor=Label(editor, text='Fecha alta: formato: DD/MM/YYYY HH:mm:ss)',bg='light slate grey',fg='white').grid(row=5, column=0,padx=5, pady=5)
        

        for record in records:
            e_DNI_editor.insert(0,record[0])
            e_name_editor.insert(0,record[1])
            e_tCustom_editor.insert(0, record[2])
            e_entryDate_editor.insert(0, record[3])

            #Para cada record en records insertamos los datos grabados en la nueva UI, accediendo por número de campo a la bbdd
              
        b_update=Button(editor, text='Actualizar datos', command=update, bd=5).grid(row=6, column=0, columnspan=3,padx=15, pady=15)

        connection.commit()     

    except Exception as exc:
        showwarning(title='ATENCIÓN!!', message='Da "Listar clientes" y selecciona un cliente existente rellenando "Elegir DNI", antes de presionar "Actualizar datos".')

#Creamos el formulario con campos de texto y etiquetas y lo situamos en celdas grid.
l_welcome= Label(r, text="BIENVENIDO A LA AGENDA DE CLIENTES PROCONSI:", bg='light slate grey', fg='white').grid(row=0,column=1, padx=10, pady=20)
l_DNI=Label(r, text='DNI sin letra ni espacios:',bg='light slate grey',fg='white').grid(row=1, column=0, padx=5, pady=5)
e_DNI= Entry (r, width=65)
e_DNI.grid (row=1,column=1, columnspan=2)
e_name=Entry(r, width=65)
e_name.grid(row=2, column=1, columnspan=2)
l_name=Label(r, text='Nombre y Apellidos: ',bg='light slate grey',fg='white').grid(row=2, column=0,padx=5, pady=5 )

l_typeCustomer=Label(r, text='Tipo de Cliente: ',bg='light slate grey',fg='white').grid(row=3, column=0,padx=5, pady=5)
radioValue=StringVar()
radioValue.set("SOCIO")

'''He creado el campo de entrada de tipo de cliente que se rellena automáticamente al seleccionar con radioButton.
Pero no es del todo necesario, se pueden  recoger los valores directamente del radioButton.
Mi finalidad, era una vez resuelta la duda enviada por email de si la cuota de asociado meterla solo en socios o sólo en registrados,
dejar ese campo libre para esa cuota y crear un campo más en la bbdd de sqLite3.'''

e_typeCustomer=Entry(r, width=65)
e_typeCustomer.grid(row=4, column=1,columnspan=2 )
rb_registered= Radiobutton(r, text='REGISTRADO', variable=radioValue, value="REGISTRADO", command=get_customer).grid(row=3, column=0, columnspan=2)
rb_membership= Radiobutton(r, text='SOCIO',  variable=radioValue, value="SOCIO", command=get_customer).grid(row=3, column=1, columnspan=2)

e_entryDate=Entry(r, width=65)
e_entryDate.grid(row=5, column=1,columnspan=2 )
l_entryDate=Label(r, text='Fecha alta: formato: DD/MM/YYYY HH:mm:ss)',bg='light slate grey',fg='white').grid(row=5, column=0,padx=5, pady=5)
now=datetime.now()
datestamp=now.strftime("%d/%m/%Y %H:%M:%S")
e_entryDate.insert(0,datestamp)
#Introducimos como fecha y hora en el placeholder la actual. Para ello,recogemos fecha en formato dd-mm-yyyy y la pasamos al formato solicitado en el enunciado, en formato string.
                                                                                                             
b_send= Button (r, text='Añadir cliente', bd=5, command=save).grid(row=6, column=0, columnspan=2,padx=5, pady=20)
b_query= Button (r, text='Listar clientes x DNI',bd=5, command=query).grid(row=6, column=1, columnspan=2,padx=5, pady=20)
b_query2= Button (r, text='Listar clientes x fecha', bd=5, command=query2).grid(row=6, column=2, columnspan=2, padx=5, pady=20)

e_selection= Entry (r, width=20)
e_selection.grid(row=8, column=0, columnspan=2)
l_selection=Label(r, text='ELEGIR DNI:',bg='light slate grey', fg='white').grid(row=8, column=0)
b_delete=Button(r, text= 'Borrar cliente', bd=5, command=delete).grid(row=8, column=1, columnspan=2,padx=5, pady=5)
b_edit=Button(r, text='Editar cliente',bd=5, command=edit).grid(row=8, column=2, columnspan=1, padx=5, pady=5)


connection.close()
r.mainloop()

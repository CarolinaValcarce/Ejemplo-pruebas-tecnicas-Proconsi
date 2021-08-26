class ItemSeparator():
    
    '''Creamos el constructor, pasando como parámetro el string base llamado phrase.
        Modificamos la frase cambiando símbolos por coma y separándolos. Accedemos a cada elemento del array'''
    
    def __init__(self, phrase='ItemName$$##ItemPrice$$##ItemQuantity'):

        self.phrase=phrase
        self.arrayPhrase=(self.phrase.replace('$$##',',')).split(sep=',')
        self._name= self.arrayPhrase[0]
        self._price=self.arrayPhrase[1]
        self._quantity=self.arrayPhrase[2]
        
    #Usando propiedades del decorador
    @property
    def name(self):
        print('Llamada al método getter 0')
        return self._name
    #La función setter
    @name.setter
    def name(self, name):
        print('Llamada al método setter')
        self._name=name
    
    #Usando propiedades del decorador
    @property
    def price(self):
        print('Llamada al método getter 1')
        return self._price
    #La función setter
    @price.setter
    def price(self, price):
        print('Llamada al método setter')
        self._price=price

    #Usando propiedades del decorador
    @property
    def quantity(self):
        print('Llamada al método getter 2')
        return self._quantity
    #La función setter
    @quantity.setter
    def price(self, quantity):
        print('Llamada al método setter')
        self._quantity=quantity

'''Ahora creamos una entidad de la clase ItemSeparator llamada stdIn y le pasamos el nuevo string.
    Accedemos a los atributos de la clase para imprimirlos.'''

stdIn=ItemSeparator('Bread$$##12.5$$##10')
print('ItemName: '+stdIn.name)
print('ItemPrice: '+stdIn.price+' Item')
print('Quantity: '+stdIn.quantity)

'''No he conseguido resolver la duda de porque llama dos veces al método getter 2
y le asigna tanto el último valor como el anterior del arreglo. Pero creo que está bien planteado.'''



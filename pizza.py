from ingredientes import ingredientes_proteicos_posibles, ingredientes_vegetales_posibles, tipos_de_masa_posibles

class Pizza:
    """
    La clase Pizza representa una pizza en la aplicación de la cadena de pizzerías.
    
    Atributos de clase:
    - ingredientes_proteicos_posibles (list): Lista de ingredientes proteicos posibles que la pizza puede tener.
    - ingredientes_vegetales_posibles (list): Lista de ingredientes vegetales posibles que la pizza puede tener.
    - tipos_de_masa_posibles (list): Lista de tipos de masa posibles para la pizza.
    
    Atributos de instancia:
    - ingrediente_proteico (str): El ingrediente proteico seleccionado por el usuario.
    - ingredientes_vegetales (list): Lista de ingredientes vegetales seleccionados por el usuario.
    - tipo_de_masa (str): El tipo de masa seleccionada por el usuario.
    - es_valida (bool): Indica si la pizza creada es válida según las reglas de negocio.
    """
    
    # Atributos de clase
    ingredientes_proteicos_posibles = ingredientes_proteicos_posibles
    ingredientes_vegetales_posibles = ingredientes_vegetales_posibles
    tipos_de_masa_posibles = tipos_de_masa_posibles
    
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Pizza.
        
        Todos los atributos de instancia se inicializan con valores por defecto:
        - ingrediente_proteico: None
        - ingredientes_vegetales: Lista vacía
        - tipo_de_masa: None
        - es_valida: False
        """
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_de_masa = None
        self.es_valida = False
    
    @staticmethod
    def validar_ingrediente(ingrediente, lista_posibles):
        """
        Método estático para validar si un ingrediente está en la lista de opciones posibles.
        
        Args:
        - ingrediente (str): El ingrediente que se desea validar.
        - lista_posibles (list): Lista de opciones posibles en las que se debe buscar el ingrediente.
        
        Returns:
        - bool: True si el ingrediente se encuentra en la lista de opciones posibles, False en caso contrario.
        """
        return ingrediente in lista_posibles
    
    def realizar_pedido(self):
        """
        Método para solicitar al usuario los ingredientes de la pizza y el tipo de masa, 
        y validar si el pedido es válido según las reglas de negocio.
        
        Se solicita al usuario que ingrese:
        - Un ingrediente proteico.
        - Dos ingredientes vegetales.
        - El tipo de masa.
        
        Después de realizar la selección, se valida si los ingredientes y el tipo de masa 
        son válidos utilizando el método validar_ingrediente(). Si todos los valores son 
        válidos, se marca la pizza como válida (es_valida = True), en caso contrario, 
        se marca como no válida (es_valida = False).
        """
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingredientes_vegetales.append(input("Ingrese el primer ingrediente vegetal: "))
        self.ingredientes_vegetales.append(input("Ingrese el segundo ingrediente vegetal: "))
        self.tipo_de_masa = input("Ingrese el tipo de masa: ")
        
        # Validación de los ingredientes y tipo de masa
        if (self.validar_ingrediente(self.ingrediente_proteico, Pizza.ingredientes_proteicos_posibles) and
            all(self.validar_ingrediente(veg, Pizza.ingredientes_vegetales_posibles) for veg in self.ingredientes_vegetales) and
            self.validar_ingrediente(self.tipo_de_masa, Pizza.tipos_de_masa_posibles)):
            self.es_valida = True
        else:
            self.es_valida = False

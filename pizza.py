# pizza.py

from ingredientes import ingredientes_proteicos_posibles, ingredientes_vegetales_posibles, tipos_de_masa_posibles

class Pizza:
    # Atributos de clase
    ingredientes_proteicos_posibles = ingredientes_proteicos_posibles
    ingredientes_vegetales_posibles = ingredientes_vegetales_posibles
    tipos_de_masa_posibles = tipos_de_masa_posibles
    
    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_de_masa = None
        self.es_valida = False
    
    @staticmethod
    def validar_ingrediente(ingrediente, lista_posibles):
        """
        Método estático para validar si un ingrediente está en la lista de opciones posibles.
        """
        return ingrediente in lista_posibles
    
    def realizar_pedido(self):
        """
        Método para realizar un pedido de pizza.
        """
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingredientes_vegetales.append(input("Ingrese el primer ingrediente vegetal: "))
        self.ingredientes_vegetales.append(input("Ingrese el segundo ingrediente vegetal: "))
        self.tipo_de_masa = input("Ingrese el tipo de masa: ")
        
        # Validación de los ingredientes
        if (self.validar_ingrediente(self.ingrediente_proteico, Pizza.ingredientes_proteicos_posibles) and
            all(self.validar_ingrediente(veg, Pizza.ingredientes_vegetales_posibles) for veg in self.ingredientes_vegetales) and
            self.validar_ingrediente(self.tipo_de_masa, Pizza.tipos_de_masa_posibles)):
            self.es_valida = True
        else:
            self.es_valida = False

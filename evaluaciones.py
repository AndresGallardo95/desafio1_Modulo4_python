# evaluaciones.py

from pizza import Pizza

# a) Mostrar los valores de los atributos de clase
print("Ingredientes proteicos posibles:", Pizza.ingredientes_proteicos_posibles)
print("Ingredientes vegetales posibles:", Pizza.ingredientes_vegetales_posibles)
print("Tipos de masa posibles:", Pizza.tipos_de_masa_posibles)

# b) Verificar si "salsa de tomate" está en la lista ["salsa de tomate", "salsa bbq"]
print("¿Está 'salsa de tomate' en la lista?", Pizza.validar_ingrediente("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c) Crear una instancia de Pizza y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d) Mostrar los ingredientes y si la pizza es válida
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Tipo de masa:", mi_pizza.tipo_de_masa)
print("¿Es una pizza válida?", mi_pizza.es_valida)

# e) Mostrar si la clase Pizza es una pizza válida (debe generar un error)
try:
    print("¿Es la clase Pizza válida?", Pizza.es_valida)
except AttributeError as e:
    print("Error:", e)

# Pizzería: Sistema de Gestión de Pedidos de Pizza

Este proyecto es un prototipo de un sistema de gestión de pedidos de pizza para una cadena de pizzerías. El sistema permite a los clientes seleccionar los ingredientes y el tipo de masa de su pizza, y valida si la combinación seleccionada es válida según las reglas del negocio.

## Estructura del Proyecto

El proyecto está dividido en varios archivos para mejorar la modularidad y claridad del código:

- **`ingredientes.py`**: Contiene las listas de ingredientes proteicos, vegetales, y tipos de masa disponibles en la pizzería.
- **`pizza.py`**: Define la clase `Pizza`, que incluye métodos para validar ingredientes y gestionar el pedido de una pizza.
- **`evaluaciones.py`**: Realiza diversas evaluaciones sobre la clase `Pizza`, como mostrar atributos de clase, validar ingredientes específicos, y manejar pedidos de pizzas.

## Instalación

Para ejecutar este proyecto, asegúrate de tener instalado Python 3 en tu máquina. No se requieren dependencias adicionales.

Para ejecutar este proyecto, sigue estos pasos:

1. Clona este repositorio usando el siguiente comando en tu terminal:

   ```bash
   git clone https://github.com/AndresGallardo95/desafio1_Modulo4_python.git

2. Navega hasta el directorio del proyecto.

### 2. Clase `Pizza`

La clase `Pizza`, definida en `pizza.py`, permite crear objetos de pizza y validar las selecciones del usuario. Los principales métodos de esta clase son:

- **`validar_ingrediente`**: Método estático que verifica si un ingrediente es válido según una lista de opciones posibles. No requiere una instancia de la clase para ser utilizado.

- **`realizar_pedido`**: Solicita al usuario que ingrese los ingredientes (un ingrediente proteico y dos vegetales) y el tipo de masa, luego valida si la combinación es correcta según las reglas de negocio. Al final, indica si la pizza es válida o no.

La clase utiliza listas de ingredientes importadas desde el archivo `ingredientes.py`, y valida las entradas del usuario contra estas listas.

### 3. Evaluaciones

El archivo `evaluaciones.py` realiza diversas pruebas sobre la clase `Pizza`, y se estructura de la siguiente manera:

- **a) Mostrar los valores de los atributos de clase**: Utiliza la función `print()` para mostrar los valores de los atributos de clase (`ingredientes_proteicos_posibles`, `ingredientes_vegetales_posibles`, `tipos_de_masa_posibles`) sin crear una instancia de la clase `Pizza`.

- **b) Verificar si "salsa de tomate" está en una lista de ingredientes**: Utiliza el método `validar_ingrediente()` para comprobar si "salsa de tomate" está presente en la lista `["salsa de tomate", "salsa bbq"]`, sin necesidad de crear una instancia de la clase.

- **c) Crear una instancia de `Pizza` y realizar un pedido**: Crea una instancia de la clase `Pizza`, y llama al método `realizar_pedido()` para permitir que el usuario ingrese los ingredientes y el tipo de masa.

- **d) Mostrar los ingredientes y si la pizza es válida**: Después de que el usuario ingresa los ingredientes, muestra en pantalla los ingredientes seleccionados y si la pizza es válida o no.

- **e) Mostrar si la clase `Pizza` es válida sin crear una instancia (debe generar un error)**: Intenta acceder al atributo de instancia `es_valida` directamente desde la clase `Pizza` sin crear una instancia, lo que genera un error que es capturado y mostrado.

Este archivo proporciona una manera interactiva y automatizada de validar el comportamiento de la clase `Pizza` según las reglas de negocio establecidas.

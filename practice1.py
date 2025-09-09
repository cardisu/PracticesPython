"""
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */
 """

# Sitio web oficial de Python: https://www.python.org/

# Comentario de una sola linea
"""Comentario de varias
lineas en
python """

# Variable de python

mi_variable = 'Hola soy una variable'
MI_CONSTANTE = 3.14  # Constante en Python (convención de mayúsculas)

# Tipos de datos primitivos
cadena_texto = "Hola, Mundo!"  # Cadena de texto
entero = 42                     # Entero
flotante = 3.14                 # Número de punto flotante
booleano = True                 # Booleano
nulo = None                     # Valor nulo
lista = [1, 2, 3]              # Lista
tupla = (1, 2, 3)              # Tupla
diccionario = {'clave': 'valor'} # Diccionario
conjunto = {1, 2, 3}           # Conjunto
rango = range(5)               # Rango
complejo = 1 + 2j              # Número complejo
bytes = b'Hola'                # Bytes
bytearray = bytearray(b'Hola')  # Bytearray
memview = memoryview(b'Hola')   # Memoryview
frozenset = frozenset([1, 2, 3]) # Frozenset
tipo_de_dato = type(cadena_texto)  # Tipo de dato
identificador = id(cadena_texto)  # Identificador único
booleano_negado = not booleano  # Negación booleana
booleano_y = booleano and False  # Operación AND
booleano_o = booleano or False  # Operación OR

# Imprimir por terminal
print("¡Hola, Python!")
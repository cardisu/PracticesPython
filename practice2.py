"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

def aritmeticos():
    a = 10
    b = 3
    print("Aritméticos:")
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"Módulo: {a} % {b} = {a % b}")
    print(f"Exponente: {a} ** {b} = {a ** b}")
    print(f"División entera: {a} // {b} = {a // b}")

def logicos():
    x = True
    y = False
    print("\nLógicos:")
    print(f"AND: {x} and {y} = {x and y}")
    print(f"OR: {x} or {y} = {x or y}")
    print(f"NOT: not {x} = {not x}")
    print(f"XOR: {x} != {y} = {x != y}")
    print(f"NAND: not ({x} and {y}) = {not (x and y)}")
    print(f"NOR: not ({x} or {y}) = {not (x or y)}")
    print(f"XNOR: {x} == {y} = {x == y}")

def comparacion():
    a = 10
    b = 20
    print("\nComparación:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} is {b}: {a is b}")
    print(f"{a} is not {b}: {a is not b}")
    print(f"{a} in [10, 20, 30]: {a in [10, 20, 30]}")
    print(f"{b} not in [10, 20, 30]: {b not in [10, 20, 30]}")

def asignacion():
    print("\nAsignación:")
    a = 5
    print(f"Inicial: a = {a}")
    a += 3
    print(f"a += 3 -> a = {a}")
    a -= 2
    print(f"a -= 2 -> a = {a}")
    a *= 4
    print(f"a *= 4 -> a = {a}")
    a /= 3
    print(f"a /= 3 -> a = {a}")
    a %= 5
    print(f"a %= 5 -> a = {a}")
    a **= 2
    print(f"a **= 2 -> a = {a}")
    a //= 2
    print(f"a //= 2 -> a = {a}")

def bits():
    a = 0b1010  # 10 en binario
    b = 0b1100  # 12 en binario
    print("\nBits:")
    print(f"a: {bin(a)}, b: {bin(b)}")
    print(f"a & b: {bin(a & b)}")
    print(f"a | b: {bin(a | b)}")
    print(f"a ^ b: {bin(a ^ b)}")
    print(f"~a: {bin(~a)}")
    print(f"a << 2: {bin(a << 2)}")
    print(f"a >> 2: {bin(a >> 2)}")

def estructuras_control():
    print("\nEstructuras de Control:")
    # Condicionales
    x = 15
    if x < 10:
        print(f"{x} es menor que 10")
    elif 10 <= x < 20:
        print(f"{x} está entre 10 y 20")
    else:
        print(f"{x} es 20 o mayor")

    # Iterativas
    print("Números del 1 al 5 usando for:")
    for i in range(1, 6):
        print(i, end=' ')
    print()

    print("Números del 1 al 5 usando while:")
    i = 1
    while i <= 5:
        print(i, end=' ')
        i += 1
    print()

    # Excepciones
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")
    finally:
        print("Bloque finally ejecutado.")

def dificultad_extra():
    print("\nNúmeros entre 10 y 55, pares, no 16 ni múltiplos de 3:")
    for num in range(10,56):
        if num % 2 == 0 and num != 16 and num % 3 != 0:
            print(num, end=' ')
    print()

if __name__ == "__main__":
    aritmeticos()
    logicos()
    comparacion()
    asignacion()
    bits()
    estructuras_control()
    dificultad_extra()
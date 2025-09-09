def holaa():
    print("Hola mundo")

def suma_simple(a, b):
    return a + b

def retorna_Esto():
    return "Esto"

def funcion_Y_funcion():
    def funcion_interna():
        return "Función interna"
    return funcion_interna()

# Variable local
def variable_local():
    cosita = 3
    print(f"Variable local: {cosita}")
    return

# Variable global
cosota = 5
def variable_global():
    global cosota
    cosota += 2
    print(f"Variable global: {cosota}")
    return

# Reto de codigo

def extra(texto1, texto2) -> int:
    contador = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(texto1 + texto2)
        elif num % 3 == 0:
            print(texto1)
        elif num % 5 == 0:
            print(texto2)
        else:
            print(num)
            contador += 1
    return contador

def main():
    holaa()
    print(f"Suma: {suma_simple(3, 5)}")
    print(f"Retorna: {retorna_Esto()}")
    print(f"Función y función: {funcion_Y_funcion()}")
    variable_local()
    variable_global()
    print(f"Variable global después de llamar a la función: {cosota}")
    print("Reto extra:")
    print(extra("Fizz", "Buzz"))

if __name__ == "__main__":
    main()

# ============================================================
# BLOQUE 7: FUNCIONES
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame las funciones en Python: parámetros por
# defecto, retorno múltiple, *args, **kwargs, lambda y recursividad."
# Prompt proceso similar: "Crea un ejercicio con una función recursiva
# diferente al factorial, como la suma de dígitos de un número."
# Resolución propia: suma de dígitos recursiva (ver proceso similar abajo)

from functools import reduce
from typing import List


# ----------------------------------------------------------
# EJERCICIO 1: Función que calcula el doble de un número
# ----------------------------------------------------------
def doble(x: float) -> float:
    """Retorna el doble del número recibido."""
    if not isinstance(x, (int, float)):
        raise TypeError("El argumento debe ser numérico")
    return x * 2


# ----------------------------------------------------------
# EJERCICIO 2: Función que suma todos los elementos con *args
# ----------------------------------------------------------
def sumar_todos(*numeros: float) -> float:
    """Suma cualquier cantidad de números."""
    if not numeros:
        return 0
    for n in numeros:
        if not isinstance(n, (int, float)):
            raise TypeError(f"Valor no numérico: {n}")
    return sum(numeros)


# ----------------------------------------------------------
# EJERCICIO 3: Factorial recursivo
# ----------------------------------------------------------
def factorial(n: int) -> int:
    """Calcula el factorial de n de forma recursiva."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n == 0:
        return 1         # caso base
    return n * factorial(n - 1)  # llamada recursiva


# ----------------------------------------------------------
# EXTRAS: otras funciones del bloque
# ----------------------------------------------------------
def presentarse(nombre: str, edad: int = 20) -> str:
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    return f"{nombre} tiene {edad} años"


def dividir(a: float, b: float):
    """Retorna cociente y resto como tupla."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a // b, a % b


def mostrar_datos(**datos) -> None:
    """Imprime pares clave-valor de kwargs."""
    for clave, valor in datos.items():
        print(f"    {clave}: {valor}")


# Función lambda
cuadrado = lambda x: x ** 2


def fibonacci(n: int) -> int:
    """Calcula el n-ésimo número de Fibonacci recursivamente."""
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia): suma de dígitos recursiva
# ----------------------------------------------------------
def suma_digitos(n: int) -> int:
    """Suma los dígitos de un entero de forma recursiva."""
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    n = abs(n)           # manejar negativos
    if n < 10:
        return n          # caso base: un solo dígito
    return n % 10 + suma_digitos(n // 10)


def ejecutar_bloque_7():
    print("\n" + "="*55)
    print("  BLOQUE 7: FUNCIONES")
    print("="*55)

    print("\n--- Ejercicio 1: Función doble ---")
    for val in [3, 7.5, -2]:
        print(f"  doble({val}) = {doble(val)}")

    print("\n--- Ejercicio 2: Suma con *args ---")
    print(f"  sumar_todos(1,2,3,4)       = {sumar_todos(1, 2, 3, 4)}")
    print(f"  sumar_todos(10, 20, 30)    = {sumar_todos(10, 20, 30)}")
    print(f"  sumar_todos()              = {sumar_todos()}")

    print("\n--- Ejercicio 3: Factorial recursivo ---")
    for n in [0, 1, 5, 7]:
        print(f"  factorial({n}) = {factorial(n)}")

    print("\n--- Extras ---")
    print(f"  presentarse('Ana')         → {presentarse('Ana')}")
    print(f"  dividir(10, 3)             → cociente={dividir(10,3)[0]}, resto={dividir(10,3)[1]}")
    print(f"  lambda cuadrado(5)         → {cuadrado(5)}")
    print(f"  fibonacci(7)               → {fibonacci(7)}")

    print("\n  mostrar_datos(nombre='Fiorella', semestre=3):")
    mostrar_datos(nombre="Fiorella", semestre=3, universidad="UNEMI")

    print("\n--- Proceso similar (propio): Suma de dígitos recursiva ---")
    for num in [0, 9, 123, 9876, 4567]:
        print(f"  suma_digitos({num}) = {suma_digitos(num)}")

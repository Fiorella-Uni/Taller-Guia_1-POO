# ============================================================
# BLOQUES 13-15: DECORADORES, UNPACKING, FUNCIONES DE ORDEN SUPERIOR
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame decoradores en Python, unpacking con */**
# y las funciones map(), filter() y reduce() con ejemplos claros."
# Prompt proceso similar: "Crea un decorador de validación de tipos y
# ejercicios combinando map/filter/reduce."
# Resolución propia: decorador de tipo + pipeline funcional (ver abajo)

import functools
import time
from functools import reduce
from typing import List, Callable, Any


# ============================================================
# BLOQUE 13: DECORADORES
# ============================================================

# ----------------------------------------------------------
# EJERCICIO 1: Decorador que imprime "Iniciando..." antes
# ----------------------------------------------------------
def decorador_log(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"  Iniciando... [{funcion.__name__}]")
        resultado = funcion(*args, **kwargs)
        print(f"  Finalizando... [{funcion.__name__}]")
        return resultado
    return wrapper


@decorador_log
def saludar(nombre: str) -> str:
    msg = f"  Hola, {nombre}!"
    print(msg)
    return msg


# ----------------------------------------------------------
# EJERCICIO 2: Decorador que verifica argumento positivo
# ----------------------------------------------------------
def validar_positivo(funcion):
    @functools.wraps(funcion)
    def wrapper(x):
        if not isinstance(x, (int, float)):
            print(f"  Error: el argumento debe ser numérico")
            return None
        if x <= 0:
            print(f"  Error: el argumento {x} no es positivo")
            return None
        return funcion(x)
    return wrapper


@validar_positivo
def calcular_cuadrado(x: float) -> float:
    resultado = x ** 2
    print(f"  cuadrado({x}) = {resultado}")
    return resultado


# ----------------------------------------------------------
# EJERCICIO 3: @log para suma(a, b)
# ----------------------------------------------------------
def log(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"  Llamando función '{funcion.__name__}' con args={args}")
        resultado = funcion(*args, **kwargs)
        print(f"  Resultado: {resultado}")
        return resultado
    return wrapper


@log
def suma(a: float, b: float) -> float:
    return a + b


# ----------------------------------------------------------
# PROCESO SIMILAR (propio): Decorador que mide tiempo
# ----------------------------------------------------------
def medir_tiempo(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        print(f"  [{funcion.__name__}] tardó {(fin-inicio)*1000:.4f} ms")
        return resultado
    return wrapper


@medir_tiempo
def sumar_lista_grande(n: int) -> int:
    return sum(range(n))


# ============================================================
# BLOQUE 14: UNPACKING
# ============================================================
class DemoUnpacking:

    # --------------------------------------------------------
    # EJERCICIO 1: Desempaquetar tupla con *
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_unpacking_basico():
        valores = (10, 20, 30, 40)
        primera, *mitad, ultima = valores
        print(f"  Tupla: {valores}")
        print(f"  primera={primera}, mitad={mitad}, ultima={ultima}")

    # --------------------------------------------------------
    # EJERCICIO 2: Pasar lista como argumentos con *
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_star_args():
        def multiplicar(a: float, b: float, c: float) -> float:
            return a * b * c

        lista = [2, 3, 4]
        resultado = multiplicar(*lista)
        print(f"  multiplicar(*{lista}) = {resultado}")

    # --------------------------------------------------------
    # EJERCICIO 3: Combinar dos dicts con **
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_star_kwargs():
        dict1 = {"nombre": "Fiorella", "edad": 20}
        dict2 = {"ciudad": "Milagro", "universidad": "UNEMI"}
        combinado = {**dict1, **dict2}
        print(f"  dict1:     {dict1}")
        print(f"  dict2:     {dict2}")
        print(f"  combinado: {combinado}")
        # El original no se modifica
        print(f"  dict1 intacto: {dict1}")


# ============================================================
# BLOQUE 15: FUNCIONES DE ORDEN SUPERIOR
# ============================================================
class FuncionesOrdenSuperior:

    # --------------------------------------------------------
    # EJERCICIO 1: map() — incrementar en 1 cada elemento
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_map():
        nums = [2, 4, 6]
        resultado = list(map(lambda x: x + 1, nums))
        print(f"  map(x+1, {nums}) → {resultado}")

    # --------------------------------------------------------
    # EJERCICIO 2: filter() — mayores a 3
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_filter():
        nums = [1, 2, 3, 4, 5]
        resultado = list(filter(lambda x: x > 3, nums))
        print(f"  filter(x>3, {nums}) → {resultado}")

    # --------------------------------------------------------
    # EJERCICIO 3: reduce() — multiplicar todos los elementos
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_reduce():
        nums = [1, 2, 3, 4]
        resultado = reduce(lambda x, y: x * y, nums)
        print(f"  reduce(x*y, {nums}) → {resultado}")
        print(f"  Proceso: 1*2=2 → 2*3=6 → 6*4={resultado}")

    # --------------------------------------------------------
    # PROCESO SIMILAR (propio): pipeline con map+filter+reduce
    # --------------------------------------------------------
    @staticmethod
    def pipeline_funcional():
        ventas = [150.0, 90.0, 320.0, 45.0, 280.0, 60.0]

        # 1) Filtrar ventas mayores a 100
        grandes = list(filter(lambda v: v > 100, ventas))
        # 2) Aplicar 10% de descuento con map
        con_descuento = list(map(lambda v: round(v * 0.90, 2), grandes))
        # 3) Total con reduce
        total = reduce(lambda acc, v: acc + v, con_descuento)

        print(f"\n  Ventas originales: {ventas}")
        print(f"  Ventas > 100:      {grandes}")
        print(f"  Con 10% descuento: {con_descuento}")
        print(f"  Total (reduce):    ${total:.2f}")


def ejecutar_bloque_13():
    print("\n" + "="*55)
    print("  BLOQUE 13: DECORADORES")
    print("="*55)

    print("\n--- Ejercicio 1: @decorador_log ---")
    saludar("Fiorella")

    print("\n--- Ejercicio 2: @validar_positivo ---")
    calcular_cuadrado(5)
    calcular_cuadrado(-3)
    calcular_cuadrado(0)

    print("\n--- Ejercicio 3: @log con suma(2,3) ---")
    suma(2, 3)

    print("\n--- Proceso similar (propio): @medir_tiempo ---")
    sumar_lista_grande(1_000_000)


def ejecutar_bloque_14():
    print("\n" + "="*55)
    print("  BLOQUE 14: UNPACKING")
    print("="*55)
    du = DemoUnpacking()
    print("\n--- Ejercicio 1: Unpacking básico ---")
    du.ejercicio_unpacking_basico()
    print("\n--- Ejercicio 2: *args en función ---")
    du.ejercicio_star_args()
    print("\n--- Ejercicio 3: **kwargs combinar dicts ---")
    du.ejercicio_star_kwargs()


def ejecutar_bloque_15():
    print("\n" + "="*55)
    print("  BLOQUE 15: FUNCIONES DE ORDEN SUPERIOR")
    print("="*55)
    fos = FuncionesOrdenSuperior()
    print("\n--- Ejercicio 1: map() ---")
    fos.ejercicio_map()
    print("\n--- Ejercicio 2: filter() ---")
    fos.ejercicio_filter()
    print("\n--- Ejercicio 3: reduce() ---")
    fos.ejercicio_reduce()
    print("\n--- Proceso similar (propio): Pipeline funcional ---")
    fos.pipeline_funcional()

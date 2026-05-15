# ============================================================
# BLOQUE 2: VARIABLES Y TIPOS DE DATOS
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame todos los tipos de datos en Python:
# simples y complejos, con ejemplos de acceso por índice y slicing."
# Prompt proceso similar: "Crea un ejercicio con una clase que use
# distintos tipos de datos y acceda a sus elementos."
# Resolución propia: clase Inventario (ver proceso similar abajo)

from typing import List, Tuple, Dict, Set, Any


# ----------------------------------------------------------
# EJERCICIO 1: Variables de cada tipo simple y complejo
# ----------------------------------------------------------
def ejercicio_tipos():
    # Tipos simples
    entero: int = 19
    flotante: float = 3.14
    cadena: str = "Hola, soy Fiorella"
    booleano: bool = True
    nulo = None

    # Tipos complejos
    lista: List[Any] = [10, 3.14, "Python", True, None]
    tupla: Tuple = (1, "hola", 3.14)
    diccionario: Dict[str, Any] = {"nombre": "Fiorella", "edad": 20}
    conjunto: Set[int] = {1, 2, 3, 4, 5}

    print("Tipos simples:")
    print(f"  int     → {entero}")
    print(f"  float   → {flotante}")
    print(f"  str     → {cadena}")
    print(f"  bool    → {booleano}")
    print(f"  None    → {nulo}")

    print("\nTipos complejos:")
    print(f"  list    → {lista}")
    print(f"  tuple   → {tupla}")
    print(f"  dict    → {diccionario}")
    print(f"  set     → {conjunto}")


# ----------------------------------------------------------
# EJERCICIO 2: Lista con 5 elementos — acceso por índice y slicing
# ----------------------------------------------------------
def ejercicio_lista():
    frutas: List[str] = ["manzana", "pera", "uva", "mango", "fresa"]

    print("\nLista:", frutas)
    print(f"  Primero   → frutas[0]  = {frutas[0]}")
    print(f"  Último    → frutas[-1] = {frutas[-1]}")
    print(f"  [1:4]     → {frutas[1:4]}")
    print(f"  [:3]      → {frutas[:3]}")
    print(f"  [-2:]     → {frutas[-2:]}")


# ----------------------------------------------------------
# EJERCICIO 3: Clase con método que usa str, list y dict
# ----------------------------------------------------------
class TiposDatos:
    def mostrar_tipos(self):
        texto: str = "Programacion Orientada a Objetos"
        numeros: List[int] = [5, 10, 15, 20, 25]
        info: Dict[str, Any] = {"curso": "POO", "semestre": 3, "aprobado": True}

        print(f"\n  Texto completo    : {texto}")
        print(f"  Primer carácter   : {texto[0]}")
        print(f"  Caracteres [0:13] : {texto[0:13]}")

        print(f"\n  Lista completa    : {numeros}")
        print(f"  Último elemento   : {numeros[-1]}")
        print(f"  Sublista [1:4]    : {numeros[1:4]}")

        print(f"\n  Diccionario       : {info}")
        print(f"  Valor 'curso'     : {info['curso']}")
        print(f"  Valor 'semestre'  : {info['semestre']}")


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia): clase Inventario
# ----------------------------------------------------------
class Inventario:
    def __init__(self):
        self.nombre_tienda: str = "TechStore Guayaquil"
        self.productos: List[str] = ["Laptop", "Mouse", "Teclado", "Monitor", "Auriculares"]
        self.precios: Dict[str, float] = {
            "Laptop": 850.0, "Mouse": 25.0, "Teclado": 45.0
        }

    def mostrar_resumen(self):
        print(f"\n  Tienda: {self.nombre_tienda}")
        print(f"  Inicial nombre tienda: {self.nombre_tienda[0]}")
        print(f"  Primer producto:  {self.productos[0]}")
        print(f"  Últimos 2:        {self.productos[-2:]}")
        print(f"  Precio Laptop:    ${self.precios['Laptop']:.2f}")


def ejecutar_bloque_2():
    print("\n" + "="*55)
    print("  BLOQUE 2: VARIABLES Y TIPOS DE DATOS")
    print("="*55)

    print("\n--- Ejercicio 1: Todos los tipos ---")
    ejercicio_tipos()

    print("\n--- Ejercicio 2: Lista y acceso ---")
    ejercicio_lista()

    print("\n--- Ejercicio 3: Clase TiposDatos ---")
    td = TiposDatos()
    td.mostrar_tipos()

    print("\n--- Proceso similar (propio): Inventario ---")
    inv = Inventario()
    inv.mostrar_resumen()

#!/usr/bin/env python3
# ============================================================
# MENÚ PRINCIPAL — GUÍA PRÁCTICA POO EN PYTHON
# Estudiante: Fiorella Solis
# Universidad: UNEMI — Asignatura: POO
# ============================================================

import sys
import os

# Asegurar que el módulo encuentra los bloques
sys.path.insert(0, os.path.dirname(__file__))

from bloques.bloque_00_intro           import ejecutar_bloque_0
from bloques.bloque_01_constructor     import ejecutar_bloque_1
from bloques.bloque_02_tipos           import ejecutar_bloque_2
from bloques.bloque_03_operadores      import ejecutar_bloque_3
from bloques.bloque_04_entrada_salida  import ejecutar_bloque_4
from bloques.bloque_05_condicionales   import ejecutar_bloque_5
from bloques.bloque_06_bucles          import ejecutar_bloque_6
from bloques.bloque_07_funciones       import ejecutar_bloque_7
from bloques.bloque_08_11_colecciones  import (
    ejecutar_bloque_8, ejecutar_bloque_9,
    ejecutar_bloque_10, ejecutar_bloque_11
)
from bloques.bloque_12_excepciones          import ejecutar_bloque_12
from bloques.bloque_13_15_decoradores_up_hop import (
    ejecutar_bloque_13, ejecutar_bloque_14, ejecutar_bloque_15
)
from bloques.bloque_16_archivos_json   import ejecutar_bloque_16
from bloques.bloque_17_mixins          import ejecutar_bloque_17


# ============================================================
# Mapa de bloques disponibles
# ============================================================
BLOQUES = {
    "0":  ("Introducción a la POO",               ejecutar_bloque_0),
    "1":  ("Constructor __init__",                ejecutar_bloque_1),
    "2":  ("Variables y Tipos de Datos",          ejecutar_bloque_2),
    "3":  ("Operadores",                          ejecutar_bloque_3),
    "4":  ("Entrada y Salida (input/print)",      ejecutar_bloque_4),
    "5":  ("Condicionales (if/elif/else)",         ejecutar_bloque_5),
    "6":  ("Bucles (for/while)",                  ejecutar_bloque_6),
    "7":  ("Funciones",                           ejecutar_bloque_7),
    "8":  ("Listas",                              ejecutar_bloque_8),
    "9":  ("Tuplas",                              ejecutar_bloque_9),
    "10": ("Diccionarios",                        ejecutar_bloque_10),
    "11": ("Conjuntos (set)",                     ejecutar_bloque_11),
    "12": ("Excepciones (try/except)",            ejecutar_bloque_12),
    "13": ("Decoradores",                         ejecutar_bloque_13),
    "14": ("Unpacking",                           ejecutar_bloque_14),
    "15": ("Funciones de Orden Superior",         ejecutar_bloque_15),
    "16": ("Archivos y JSON",                     ejecutar_bloque_16),
    "17": ("Mixins",                              ejecutar_bloque_17),
}

GRUPOS = {
    "A": ("Bloques 0-3  | Fundamentos",          ["0", "1", "2", "3"]),
    "B": ("Bloques 4-7  | Control y Funciones",  ["4", "5", "6", "7"]),
    "C": ("Bloques 8-11 | Colecciones",          ["8", "9", "10", "11"]),
    "D": ("Bloques 12-15| Avanzado",             ["12", "13", "14", "15"]),
    "E": ("Bloques 16-17| Archivos y Mixins",    ["16", "17"]),
}


# ============================================================
# Clase MenuBloque — menú de un bloque específico
# ============================================================
class MenuBloque:
    def __init__(self, numero: str, nombre: str, ejecutar_fn):
        self.numero = numero
        self.nombre = nombre
        self._ejecutar_fn = ejecutar_fn

    def mostrar(self):
        while True:
            print(f"\n{'─'*55}")
            print(f"  BLOQUE {self.numero}: {self.nombre}")
            print(f"{'─'*55}")
            print("  [1] Ejecutar ejercicios del bloque")
            print("  [0] ← Volver al menú anterior")
            opcion = input("\n  Seleccione: ").strip()

            if opcion == "1":
                try:
                    self._ejecutar_fn()
                except Exception as e:
                    print(f"\n  ⚠ Error en bloque {self.numero}: {e}")
                input("\n  Presione Enter para continuar...")
            elif opcion == "0":
                break
            else:
                print("  Opción no válida.")


# ============================================================
# Clase MenuGrupo — menú de un grupo de bloques
# ============================================================
class MenuGrupo:
    def __init__(self, letra: str, descripcion: str, numeros: list):
        self.letra = letra
        self.descripcion = descripcion
        self.numeros = numeros

    def mostrar(self):
        while True:
            print(f"\n{'═'*55}")
            print(f"  GRUPO {self.letra}: {self.descripcion}")
            print(f"{'═'*55}")
            for num in self.numeros:
                nombre = BLOQUES[num][0]
                print(f"  [{num:>2}] Bloque {num} — {nombre}")
            print(f"  [ A] Ejecutar TODOS los bloques del grupo")
            print(f"  [ 0] ← Volver al menú principal")

            opcion = input("\n  Seleccione: ").strip().upper()

            if opcion == "0":
                break
            elif opcion == "A":
                for num in self.numeros:
                    nombre, fn = BLOQUES[num]
                    try:
                        fn()
                    except Exception as e:
                        print(f"\n  ⚠ Error en bloque {num}: {e}")
                input("\n  Todos los bloques ejecutados. Enter para continuar...")
            elif opcion in self.numeros:
                nombre, fn = BLOQUES[opcion]
                mb = MenuBloque(opcion, nombre, fn)
                mb.mostrar()
            else:
                print("  Opción no válida.")


# ============================================================
# Clase MenuPrincipal
# ============================================================
class MenuPrincipal:
    """Menú raíz que gestiona todos los grupos y bloques."""

    def _mostrar_cabecera(self):
        print("\n" + "╔" + "═"*53 + "╗")
        print("║" + " "*10 + "GUÍA PRÁCTICA POO — PYTHON" + " "*17 + "║")
        print("║" + " "*8  + "Fiorella Solis | UNEMI 2025" + " "*16 + "║")
        print("╚" + "═"*53 + "╝")

    def _mostrar_menu_principal(self):
        self._mostrar_cabecera()
        print("\n  ── GRUPOS DE BLOQUES ──")
        for letra, (desc, _) in GRUPOS.items():
            print(f"  [{letra}] {desc}")
        print("\n  ── ACCESO RÁPIDO ──")
        print("  [T] Ejecutar TODOS los bloques (demo completa)")
        print("  [X] Salir")

    def ejecutar(self):
        while True:
            self._mostrar_menu_principal()
            opcion = input("\n  Seleccione una opción: ").strip().upper()

            if opcion == "X":
                print("\n  ¡Hasta luego, Fiorella! 👋\n")
                break
            elif opcion == "T":
                print("\n  Ejecutando TODOS los bloques...\n")
                for num, (nombre, fn) in BLOQUES.items():
                    try:
                        fn()
                    except Exception as e:
                        print(f"\n  ⚠ Error en bloque {num}: {e}")
                input("\n  Demo completa finalizada. Enter para continuar...")
            elif opcion in GRUPOS:
                desc, numeros = GRUPOS[opcion]
                mg = MenuGrupo(opcion, desc, numeros)
                mg.mostrar()
            else:
                print("  Opción no válida. Intente nuevamente.")


# ============================================================
# Punto de entrada
# ============================================================
if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ejecutar()

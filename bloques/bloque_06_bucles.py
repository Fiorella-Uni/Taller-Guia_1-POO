# ============================================================
# BLOQUE 6: BUCLES (for / while)
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame los bucles en Python: while, for con range(),
# for sobre colecciones, enumerate, break/continue y list comprehension."
# Prompt proceso similar: "Crea un ejercicio de tabla de multiplicar usando
# bucles anidados y list comprehension."
# Resolución propia: tabla de multiplicar y pirámide de asteriscos (ver abajo)

class Bucles:
    """Clase que agrupa los ejercicios de bucles."""

    # ----------------------------------------------------------
    # EJERCICIO 1: Números del 1 al 10 con while
    # ----------------------------------------------------------
    @staticmethod
    def numeros_con_while():
        print("  Números del 1 al 10 con while:")
        contador = 1
        resultado = []
        while contador <= 10:
            resultado.append(str(contador))
            contador += 1
        print("  " + " - ".join(resultado))

    # ----------------------------------------------------------
    # EJERCICIO 2: Recorrer frutas con enumerate
    # ----------------------------------------------------------
    @staticmethod
    def frutas_con_enumerate():
        frutas = ["manzana", "pera", "uva", "mango", "fresa"]
        print("  Lista de frutas con índice:")
        for indice, fruta in enumerate(frutas):
            print(f"    [{indice}] {fruta.capitalize()}")

    # ----------------------------------------------------------
    # EJERCICIO 3: Cuadrados de pares del 1 al 10 — list comprehension
    # ----------------------------------------------------------
    @staticmethod
    def cuadrados_pares():
        # Números pares del 1 al 10: 2, 4, 6, 8, 10
        cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0]
        print(f"  Cuadrados de pares [1..10]: {cuadrados}")
        # Resultado esperado: [4, 16, 36, 64, 100]

    # ----------------------------------------------------------
    # PROCESO SIMILAR (resolución propia): Tabla de multiplicar
    # ----------------------------------------------------------
    @staticmethod
    def tabla_multiplicar(numero: int):
        if not (1 <= numero <= 12):
            raise ValueError("El número debe estar entre 1 y 12")
        print(f"\n  Tabla del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"    {numero} x {i:2} = {resultado:3}")

    # ----------------------------------------------------------
    # EXTRA (proceso similar 2): Pirámide con for anidado
    # ----------------------------------------------------------
    @staticmethod
    def piramide(filas: int):
        if filas < 1 or filas > 10:
            raise ValueError("Las filas deben estar entre 1 y 10")
        print(f"\n  Pirámide de {filas} filas:")
        for i in range(1, filas + 1):
            espacios = " " * (filas - i)
            estrellas = "*" * (2 * i - 1)
            print(f"  {espacios}{estrellas}")

    # ----------------------------------------------------------
    # DEMO: break y continue
    # ----------------------------------------------------------
    @staticmethod
    def demo_break_continue():
        print("\n  Con break (para cuando i == 3):")
        nums_break = []
        for i in range(6):
            if i == 3:
                break
            nums_break.append(i)
        print(f"    → {nums_break}")

        print("\n  Con continue (salta cuando i == 2):")
        nums_continue = [i for i in range(6) if i != 2]
        print(f"    → {nums_continue}")


def ejecutar_bloque_6():
    print("\n" + "="*55)
    print("  BLOQUE 6: BUCLES")
    print("="*55)

    b = Bucles()

    print("\n--- Ejercicio 1: While del 1 al 10 ---")
    b.numeros_con_while()

    print("\n--- Ejercicio 2: Frutas con enumerate ---")
    b.frutas_con_enumerate()

    print("\n--- Ejercicio 3: Cuadrados de pares ---")
    b.cuadrados_pares()

    print("\n--- Demo: break y continue ---")
    b.demo_break_continue()

    print("\n--- Proceso similar (propio): Tabla de multiplicar ---")
    b.tabla_multiplicar(7)

    print("\n--- Proceso similar 2 (propio): Pirámide ---")
    b.piramide(5)

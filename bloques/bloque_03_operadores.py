# ============================================================
# BLOQUE 3: OPERADORES
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame todos los operadores en Python: aritméticos,
# comparación, lógicos, diferencia entre == e is, y precedencia."
# Prompt proceso similar: "Dame un ejercicio similar al de precedencia de
# operadores para practicar el orden de evaluación."
# Resolución propia: evaluación de expresión con paréntesis (ver abajo)

class CalculadoraOperadores:
    """Clase que demuestra el uso de operadores en Python."""

    def __init__(self, a: int, b: int):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los valores deben ser numéricos")
        self.a = a
        self.b = b

    # ----------------------------------------------------------
    # EJERCICIO 1: Operadores aritméticos con a=20, b=4
    # ----------------------------------------------------------
    def mostrar_aritmeticos(self):
        a, b = self.a, self.b
        print(f"\n  a={a}, b={b}")
        print(f"  Suma         a + b  = {a + b}")
        print(f"  Resta        a - b  = {a - b}")
        print(f"  Multiplicar  a * b  = {a * b}")
        print(f"  División     a / b  = {a / b}")
        print(f"  Div. entera  a // b = {a // b}")
        print(f"  Módulo       a % b  = {a % b}")
        print(f"  Potencia     a ** b = {a ** b}")

    # ----------------------------------------------------------
    # EJERCICIO 2: == vs is con dos listas idénticas
    # ----------------------------------------------------------
    @staticmethod
    def demostrar_igualdad():
        lista_a = [1, 2, 3]
        lista_b = [1, 2, 3]
        lista_c = lista_a  # misma referencia

        print(f"\n  lista_a = {lista_a}")
        print(f"  lista_b = {lista_b} (contenido igual, objeto distinto)")
        print(f"  lista_c = lista_a  (misma referencia)")

        print(f"\n  lista_a == lista_b → {lista_a == lista_b}  (mismo contenido)")
        print(f"  lista_a is lista_b → {lista_a is lista_b}  (diferentes objetos en memoria)")
        print(f"  lista_a is lista_c → {lista_a is lista_c}  (misma referencia)")

    # ----------------------------------------------------------
    # EJERCICIO 3: Precedencia — x = 2 + 1 * 2 % 2 + (2**1)//2
    # ----------------------------------------------------------
    @staticmethod
    def explicar_precedencia():
        # Orden de evaluación:
        # 1° ** → 2**1 = 2
        # 2° *  → 1 * 2 = 2
        # 3° %  → 2 % 2 = 0
        # 4° // → 2 // 2 = 1
        # 5° +  → 2 + 0 + 1 = 3
        x = 2 + 1 * 2 % 2 + (2**1)//2
        print(f"\n  Expresión: x = 2 + 1 * 2 % 2 + (2**1)//2")
        print(f"  Paso 1 → 2**1      = 2")
        print(f"  Paso 2 → 1 * 2     = 2")
        print(f"  Paso 3 → 2 % 2     = 0")
        print(f"  Paso 4 → 2 // 2    = 1")
        print(f"  Paso 5 → 2 + 0 + 1 = 3")
        print(f"  Resultado final x  = {x}")


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia):
# Evaluar: y = 3 ** 2 - 4 * (6 // 2) + 10 % 3
# ----------------------------------------------------------
def proceso_similar_precedencia():
    # Paso 1: 3**2 = 9
    # Paso 2: 6//2 = 3
    # Paso 3: 4*3  = 12
    # Paso 4: 10%3 = 1
    # Paso 5: 9 - 12 + 1 = -2
    y = 3 ** 2 - 4 * (6 // 2) + 10 % 3
    print(f"\n  Expresión propia: y = 3 ** 2 - 4 * (6 // 2) + 10 % 3")
    print(f"  Paso 1 → 3**2      = 9")
    print(f"  Paso 2 → 6//2      = 3")
    print(f"  Paso 3 → 4 * 3     = 12")
    print(f"  Paso 4 → 10 % 3    = 1")
    print(f"  Paso 5 → 9-12+1    = -2")
    print(f"  Resultado final y  = {y}")


def ejecutar_bloque_3():
    print("\n" + "="*55)
    print("  BLOQUE 3: OPERADORES")
    print("="*55)

    calc = CalculadoraOperadores(20, 4)

    print("\n--- Ejercicio 1: Operadores aritméticos ---")
    calc.mostrar_aritmeticos()

    print("\n--- Ejercicio 2: == vs is ---")
    CalculadoraOperadores.demostrar_igualdad()

    print("\n--- Ejercicio 3: Precedencia de operadores ---")
    CalculadoraOperadores.explicar_precedencia()

    print("\n--- Proceso similar (propio): otra expresión ---")
    proceso_similar_precedencia()

# ============================================================
# BLOQUE 5: CONDICIONALES (if / elif / else)
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame los condicionales en Python: if/elif/else,
# operador ternario, match-case y evaluación corta (short-circuit)."
# Prompt proceso similar: "Genera un sistema de validación de contraseña
# que use if/elif/else con varias condiciones."
# Resolución propia: validador de contraseña segura (ver abajo)

class Condicionales:
    """Clase que agrupa todos los ejercicios de condicionales."""

    # ----------------------------------------------------------
    # EJERCICIO 1: Par o impar
    # ----------------------------------------------------------
    @staticmethod
    def par_o_impar(numero: int) -> str:
        if not isinstance(numero, int):
            raise TypeError("Debe ingresar un número entero")
        resultado = "Par" if numero % 2 == 0 else "Impar"
        return f"  El número {numero} es: {resultado}"

    # ----------------------------------------------------------
    # EJERCICIO 2: Calificación por letra (A, B, C, D)
    # ----------------------------------------------------------
    @staticmethod
    def calificacion_letra(nota: float) -> str:
        if not (0 <= nota <= 100):
            raise ValueError("La nota debe estar entre 0 y 100")

        if nota >= 90:
            letra = "A — Excelente"
        elif nota >= 80:
            letra = "B — Muy bueno"
        elif nota >= 70:
            letra = "C — Bueno"
        elif nota >= 60:
            letra = "D — Suficiente"
        else:
            letra = "F — Reprobado"

        return f"  Nota {nota:.1f} → {letra}"

    # ----------------------------------------------------------
    # EJERCICIO 3: Sistema de login
    # ----------------------------------------------------------
    @staticmethod
    def sistema_login(usuario: str, password: str) -> str:
        if not usuario or not password:
            return "  Error: usuario y contraseña no pueden estar vacíos"

        USUARIO_CORRECTO = "admin"
        PASSWORD_CORRECTA = "123"

        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
            return "  ✓ Bienvenido/a al sistema, admin!"
        elif usuario == USUARIO_CORRECTO and password != PASSWORD_CORRECTA:
            return "  ✗ Contraseña incorrecta"
        else:
            return "  ✗ Acceso denegado: usuario no encontrado"

    # ----------------------------------------------------------
    # PROCESO SIMILAR (resolución propia): Validador de contraseña
    # ----------------------------------------------------------
    @staticmethod
    def validar_contrasena(contrasena: str) -> str:
        if not contrasena:
            return "  Contraseña vacía — inválida"

        tiene_mayuscula = any(c.isupper() for c in contrasena)
        tiene_numero = any(c.isdigit() for c in contrasena)
        longitud_ok = len(contrasena) >= 8

        if longitud_ok and tiene_mayuscula and tiene_numero:
            nivel = "FUERTE ✓"
        elif longitud_ok and (tiene_mayuscula or tiene_numero):
            nivel = "MEDIA — mejora añadiendo números o mayúsculas"
        elif longitud_ok:
            nivel = "DÉBIL — agrega mayúsculas y números"
        else:
            nivel = "MUY DÉBIL — muy corta (mínimo 8 caracteres)"

        return (f"  Contraseña: {'*' * len(contrasena)}\n"
                f"  Longitud ≥8: {longitud_ok} | Mayúscula: {tiene_mayuscula} "
                f"| Número: {tiene_numero}\n"
                f"  Nivel: {nivel}")


def ejecutar_bloque_5():
    print("\n" + "="*55)
    print("  BLOQUE 5: CONDICIONALES")
    print("="*55)

    cond = Condicionales()

    print("\n--- Ejercicio 1: Par o impar ---")
    for n in [0, 7, 14, 33]:
        print(cond.par_o_impar(n))

    print("\n--- Ejercicio 2: Calificación por letra ---")
    for nota in [95, 84, 72, 63, 45]:
        print(cond.calificacion_letra(nota))

    print("\n--- Ejercicio 3: Sistema de login ---")
    print(cond.sistema_login("admin", "123"))
    print(cond.sistema_login("admin", "wrongpass"))
    print(cond.sistema_login("hacker", "123"))

    print("\n--- Proceso similar (propio): Validador contraseña ---")
    for pwd in ["abc", "password", "Password1", "P@ss2024"]:
        print(f"\n  Probando: {pwd}")
        print(cond.validar_contrasena(pwd))

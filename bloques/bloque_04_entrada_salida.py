# ============================================================
# BLOQUE 4: ENTRADA Y SALIDA (input / print)
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame cómo usar input() y print() en Python,
# qué es el casting y cómo usar f-strings correctamente."
# Prompt proceso similar: "Genera un ejercicio en el que el usuario
# ingrese datos y se calculen operaciones matemáticas básicas."
# Resolución propia: calculadora de IMC con datos del usuario (ver abajo)

class EntradaSalida:
    """
    Clase que gestiona las demos de entrada/salida.
    Los métodos usan datos predefinidos para funcionar sin
    interacción real (modo demostración), pero también incluyen
    versiones interactivas comentadas.
    """

    # ----------------------------------------------------------
    # EJERCICIO 1: Solicitar nombre y edad, mostrar con f-string
    # ----------------------------------------------------------
    @staticmethod
    def ejercicio_nombre_edad():
        # Versión interactiva (descomentar para usar):
        # nombre = input("Ingrese su nombre: ")
        # edad = int(input("Ingrese su edad: "))

        # Versión demostración:
        nombre = "Fiorella Solis"
        edad = 20

        print(f"\n  Hola, {nombre}!")
        print(f"  Tienes {edad} años.")
        print(f"  En 5 años tendrás {edad + 5} años.")

    # ----------------------------------------------------------
    # EJERCICIO 2: Leer dos números, calcular suma y promedio
    # ----------------------------------------------------------
    @staticmethod
    def ejercicio_suma_promedio():
        # Versión interactiva (descomentar para usar):
        # num1 = float(input("Ingrese el primer número: "))
        # num2 = float(input("Ingrese el segundo número: "))

        # Versión demostración:
        num1 = 14.5
        num2 = 9.5

        suma = num1 + num2
        promedio = suma / 2

        print(f"\n  Número 1: {num1}")
        print(f"  Número 2: {num2}")
        print(f"  Suma:     {suma}")
        print(f"  Promedio: {promedio:.2f}")

    # ----------------------------------------------------------
    # EJERCICIO 3: Sin casting — qué pasa con número + "5"
    # ----------------------------------------------------------
    @staticmethod
    def ejercicio_sin_casting():
        numero_str = "10"  # Simula input() sin conversión
        cinco_str = "5"

        resultado_str = numero_str + cinco_str
        print(f"\n  Sin casting: '10' + '5' = '{resultado_str}'")
        print(f"  ¡Se CONCATENAN como cadenas de texto, no suman!")

        numero_int = int(numero_str)
        resultado_int = numero_int + int(cinco_str)
        print(f"\n  Con casting: int('10') + int('5') = {resultado_int}")
        print(f"  ¡Ahora SÍ suma correctamente!")

    # ----------------------------------------------------------
    # PROCESO SIMILAR (resolución propia): Calculadora de IMC
    # ----------------------------------------------------------
    @staticmethod
    def calculadora_imc():
        # Versión interactiva (descomentar para usar):
        # nombre = input("Ingrese su nombre: ")
        # peso = float(input("Ingrese su peso en kg: "))
        # altura = float(input("Ingrese su altura en metros: "))

        nombre = "Fiorella"
        peso = 58.0
        altura = 1.63

        if altura <= 0:
            print("  Error: la altura debe ser mayor a 0")
            return

        imc = peso / (altura ** 2)

        if imc < 18.5:
            categoria = "Bajo peso"
        elif imc < 25.0:
            categoria = "Peso normal"
        elif imc < 30.0:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"

        print(f"\n  Nombre:     {nombre}")
        print(f"  Peso:       {peso} kg")
        print(f"  Altura:     {altura} m")
        print(f"  IMC:        {imc:.2f}")
        print(f"  Categoría:  {categoria}")


def ejecutar_bloque_4():
    print("\n" + "="*55)
    print("  BLOQUE 4: ENTRADA Y SALIDA")
    print("="*55)

    es = EntradaSalida()

    print("\n--- Ejercicio 1: Nombre y edad con f-string ---")
    es.ejercicio_nombre_edad()

    print("\n--- Ejercicio 2: Suma y promedio de dos números ---")
    es.ejercicio_suma_promedio()

    print("\n--- Ejercicio 3: Concatenación sin casting ---")
    es.ejercicio_sin_casting()

    print("\n--- Proceso similar (propio): Calculadora de IMC ---")
    es.calculadora_imc()

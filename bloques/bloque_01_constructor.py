# ============================================================
# BLOQUE 1: EL CONSTRUCTOR __init__
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame cómo funciona __init__ en Python,
# qué es self, cómo validar datos dentro del constructor y cómo
# crear constructores alternativos con @classmethod."
# Prompt proceso similar: "Genera un ejercicio similar al de Producto
# con una clase diferente que tenga validaciones en el constructor."
# Resolución propia: clase Vehiculo con validaciones (ver abajo)

# ----------------------------------------------------------
# EJERCICIO 1: Clase Producto con validaciones
# ----------------------------------------------------------
class Producto:
    def __init__(self, codigo, nombre, precio):
        if not codigo or not nombre:
            raise ValueError("Código y nombre son obligatorios")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    @classmethod
    def desde_diccionario(cls, datos):
        """Constructor alternativo: crea Producto desde un dict."""
        return cls(datos["codigo"], datos["nombre"], datos["precio"])

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"


# ----------------------------------------------------------
# EJERCICIO 2: Validación de precio negativo (incluida arriba)
# ----------------------------------------------------------

# ----------------------------------------------------------
# EJERCICIO 3: Clase Estudiante con notas opcionales
# ----------------------------------------------------------
class Estudiante:
    def __init__(self, nombre, notas=None):
        if not nombre:
            raise ValueError("El nombre del estudiante es obligatorio")
        self.nombre = nombre
        # Si no se pasan notas, iniciar lista vacía (evitar mutabilidad compartida)
        self.notas = notas if notas is not None else []

    def agregar_nota(self, nota):
        if not (0 <= nota <= 10):
            raise ValueError("La nota debe estar entre 0 y 10")
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    @classmethod
    def desde_diccionario(cls, datos):
        """Constructor alternativo desde diccionario."""
        return cls(datos["nombre"], datos.get("notas"))

    def __str__(self):
        return (f"Estudiante: {self.nombre} | "
                f"Notas: {self.notas} | Promedio: {self.promedio():.2f}")


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia): clase Vehiculo
# ----------------------------------------------------------
class Vehiculo:
    def __init__(self, placa, marca, anio):
        if not placa or not marca:
            raise ValueError("Placa y marca son obligatorias")
        if anio < 1900 or anio > 2026:
            raise ValueError("Año de fabricación inválido")
        self.placa = placa
        self.marca = marca
        self.anio = anio

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["placa"], datos["marca"], datos["anio"])

    def __str__(self):
        return f"Vehículo {self.marca} ({self.anio}) - Placa: {self.placa}"


def ejecutar_bloque_1():
    print("\n" + "="*55)
    print("  BLOQUE 1: EL CONSTRUCTOR __init__")
    print("="*55)

    print("\n--- Ejercicio 1: Clase Producto ---")
    p1 = Producto("P001", "Laptop", 900)
    p2 = Producto("P002", "Mouse", 25)
    print(p1)
    print(p2)

    print("\n--- Ejercicio 2: Validación precio negativo ---")
    try:
        p_malo = Producto("P003", "Teclado", -50)
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")

    print("\n--- Ejercicio 3: Clase Estudiante ---")
    est1 = Estudiante("Fiorella Solis")
    est1.agregar_nota(9)
    est1.agregar_nota(8)
    est1.agregar_nota(10)

    datos_est = {"nombre": "Luis Torres", "notas": [7, 8, 9]}
    est2 = Estudiante.desde_diccionario(datos_est)

    print(est1)
    print(est2)

    print("\n--- Proceso similar (propio): Clase Vehiculo ---")
    v1 = Vehiculo("GYE-001", "Toyota", 2020)
    datos_v = {"placa": "GYE-002", "marca": "Chevrolet", "anio": 2018}
    v2 = Vehiculo.desde_diccionario(datos_v)
    print(v1)
    print(v2)

    try:
        v_malo = Vehiculo("ABC-999", "Honda", 1800)
    except ValueError as e:
        print(f"Error de año inválido capturado: {e}")

# ============================================================
# BLOQUE 17: MIXINS
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame qué es un Mixin en Python, cómo se usa
# para agregar funcionalidad reutilizable sin instanciar la clase,
# y qué es el MRO (Method Resolution Order)."
# Prompt proceso similar: "Crea un mixin de auditoría que registre
# cuándo se crean y modifican objetos."
# Resolución propia: AuditoriaMixin para rastrear cambios (ver abajo)

import json
import csv
import io
import re
from typing import List, Any
from datetime import datetime


# ============================================================
# EJERCICIO 1: PromedioMixin
# ============================================================
class PromedioMixin:
    """Mixin que calcula el promedio de una lista de notas."""

    def calcular_promedio(self, notas: List[float]) -> float:
        if not notas:
            raise ValueError("La lista de notas no puede estar vacía")
        if any(not isinstance(n, (int, float)) for n in notas):
            raise TypeError("Todas las notas deben ser numéricas")
        if any(n < 0 or n > 10 for n in notas):
            raise ValueError("Las notas deben estar entre 0 y 10")
        return round(sum(notas) / len(notas), 2)


class Estudiante(PromedioMixin):
    """Estudiante que usa PromedioMixin para calcular su promedio."""

    def __init__(self, nombre: str, notas: List[float] = None):
        if not nombre:
            raise ValueError("El nombre del estudiante es obligatorio")
        self.nombre = nombre
        self.notas = notas if notas is not None else []

    def mostrar_resultado(self) -> None:
        if not self.notas:
            print(f"  {self.nombre}: sin notas registradas")
            return
        promedio = self.calcular_promedio(self.notas)
        estado = "✓ Aprobado" if promedio >= 7 else "✗ Reprobado"
        print(f"  {self.nombre:20} Notas: {self.notas}  "
              f"Promedio: {promedio}  {estado}")


# ============================================================
# EJERCICIO 2: ValidacionMixin
# ============================================================
class ValidacionMixin:
    """Mixin para validar email y edad antes de registrar."""

    def validar_email(self, correo: str) -> bool:
        """Verifica que el correo tenga @ y .com"""
        if not correo:
            raise ValueError("El correo no puede estar vacío")
        patron = r'^[\w\.-]+@[\w\.-]+\.com$'
        if not re.match(patron, correo):
            raise ValueError(f"Email inválido: '{correo}' (debe contener @ y terminar en .com)")
        return True

    def validar_edad(self, edad: int) -> bool:
        """Verifica que la edad sea >= 18."""
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un entero")
        if edad < 18:
            raise ValueError(f"Edad inválida: {edad}. Debe ser mayor o igual a 18")
        return True


class Usuario(ValidacionMixin):
    """Usuario que valida sus datos antes de registrarse."""

    def __init__(self, nombre: str, email: str, edad: int):
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        # Validaciones del mixin
        self.validar_email(email)
        self.validar_edad(edad)
        self.nombre = nombre
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"Usuario: {self.nombre} | {self.email} | {self.edad} años"


# ============================================================
# EJERCICIO 3: ExportarMixin
# ============================================================
class ExportarMixin:
    """Mixin para exportar datos a JSON y CSV."""

    def exportar_json(self, datos: Any) -> str:
        """Convierte los datos a formato JSON con indentación."""
        return json.dumps(datos, indent=2, ensure_ascii=False)

    def exportar_csv(self, datos: List[dict]) -> str:
        """Convierte una lista de dicts a formato CSV."""
        if not datos:
            return ""
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)
        return output.getvalue()


class Reporte(ExportarMixin):
    """Clase que genera reportes exportables de ventas."""

    def __init__(self, titulo: str):
        if not titulo:
            raise ValueError("El título del reporte es obligatorio")
        self.titulo = titulo
        self._registros: List[dict] = []

    def agregar_registro(self, producto: str, cantidad: int, precio: float) -> None:
        if not producto:
            raise ValueError("El producto no puede estar vacío")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._registros.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio_unit": precio,
            "total": round(cantidad * precio, 2)
        })

    def mostrar_json(self) -> None:
        print(f"\n  JSON del reporte '{self.titulo}':")
        print(self.exportar_json(self._registros))

    def mostrar_csv(self) -> None:
        print(f"\n  CSV del reporte '{self.titulo}':")
        print(self.exportar_csv(self._registros))


# ============================================================
# PROCESO SIMILAR (resolución propia): AuditoriaMixin
# ============================================================
class AuditoriaMixin:
    """Mixin que registra cuándo se crean y modifican objetos."""

    def __init__(self):
        self._auditoria: List[str] = []
        self._registrar_evento("CREACIÓN")

    def _registrar_evento(self, evento: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entrada = f"[{timestamp}] {evento}"
        self._auditoria.append(entrada)

    def mostrar_auditoria(self) -> None:
        print(f"  Auditoría ({len(self._auditoria)} eventos):")
        for entrada in self._auditoria:
            print(f"    {entrada}")


class Producto(AuditoriaMixin):
    """Producto con auditoría de cambios."""

    def __init__(self, codigo: str, nombre: str, precio: float):
        if not codigo or not nombre:
            raise ValueError("Código y nombre son obligatorios")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        AuditoriaMixin.__init__(self)
        self.codigo = codigo
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        precio_anterior = self._precio
        self._precio = nuevo_precio
        self._registrar_evento(
            f"PRECIO CAMBIADO: ${precio_anterior:.2f} → ${nuevo_precio:.2f}"
        )

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self._precio:.2f}"


def ejecutar_bloque_17():
    print("\n" + "="*55)
    print("  BLOQUE 17: MIXINS")
    print("="*55)

    # ---- Ejercicio 1: PromedioMixin ----
    print("\n--- Ejercicio 1: PromedioMixin ---")
    estudiantes = [
        Estudiante("Fiorella Solis",  [8, 9, 10]),
        Estudiante("Luis Mendoza",    [6, 5, 7]),
        Estudiante("Ana Carillo",     [10, 9, 9]),
        Estudiante("Pedro Reyes",     [4, 5, 6]),
    ]
    for est in estudiantes:
        est.mostrar_resultado()

    # Error de validación
    try:
        mal = Estudiante("Test", [11, 8, 9])
        mal.mostrar_resultado()
    except ValueError as e:
        print(f"  Validación correcta: {e}")

    # ---- Ejercicio 2: ValidacionMixin ----
    print("\n--- Ejercicio 2: ValidacionMixin ---")
    datos_validos = [
        ("Fiorella Solis",  "fsolis@unemi.com", 20),
        ("Ana Torres",      "atorres@gmail.com", 19),
    ]
    for nombre, email, edad in datos_validos:
        try:
            u = Usuario(nombre, email, edad)
            print(f"  ✓ {u}")
        except ValueError as e:
            print(f"  ✗ Error: {e}")

    datos_invalidos = [
        ("Sin arroba",   "emailsinvalido.com", 22),
        ("Menor edad",   "menor@gmail.com", 16),
    ]
    for nombre, email, edad in datos_invalidos:
        try:
            u = Usuario(nombre, email, edad)
            print(f"  ✓ {u}")
        except ValueError as e:
            print(f"  ✗ Validación OK → {e}")

    # ---- Ejercicio 3: ExportarMixin ----
    print("\n--- Ejercicio 3: ExportarMixin ---")
    reporte = Reporte("Ventas Mayo 2025")
    reporte.agregar_registro("Laptop",  3, 850.0)
    reporte.agregar_registro("Mouse",   10, 25.0)
    reporte.agregar_registro("Monitor", 5, 320.0)
    reporte.mostrar_json()
    reporte.mostrar_csv()

    # ---- Proceso similar: AuditoriaMixin ----
    print("\n--- Proceso similar (propio): AuditoriaMixin ---")
    prod = Producto("P001", "Laptop", 850.0)
    print(f"  {prod}")
    prod.precio = 780.0
    prod.precio = 820.0
    print(f"  {prod}")
    prod.mostrar_auditoria()

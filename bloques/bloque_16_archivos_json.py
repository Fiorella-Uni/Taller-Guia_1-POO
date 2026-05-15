# ============================================================
# BLOQUE 16: ARCHIVOS Y JSON
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame cómo trabajar con archivos de texto y JSON
# en Python: open(), modos r/w/a, with, json.dump, json.load."
# Prompt proceso similar: "Crea un sistema que guarde y cargue registros
# de estudiantes en formato JSON."
# Resolución propia: sistema de registro de notas en JSON (ver abajo)

import json
import os
from typing import List, Dict, Any


# Directorio base de datos
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)


# ----------------------------------------------------------
# EJERCICIO 1: Escribir "Python" en archivo y leerlo
# ----------------------------------------------------------
class ManejadorArchivos:

    @staticmethod
    def ejercicio_escribir_leer():
        ruta = os.path.join(DATA_DIR, "ejemplo.txt")

        # Escribir
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("Python\n")
            f.write("Programación Orientada a Objetos\n")
            f.write("UNEMI - Fiorella Solis\n")

        # Leer todo
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        print(f"  Contenido del archivo:\n{contenido}")

        # Leer línea a línea
        print("  Líneas individuales:")
        with open(ruta, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, 1):
                print(f"    Línea {i}: {linea.strip()}")

    # --------------------------------------------------------
    # EJERCICIO 2: Guardar y cargar dict en JSON
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_json_dict():
        ruta = os.path.join(DATA_DIR, "coordenada.json")
        datos = {"x": 10, "y": 20}

        # Guardar
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2)
        print(f"  Guardado: {datos}")

        # Cargar
        with open(ruta, "r", encoding="utf-8") as f:
            cargado = json.load(f)
        print(f"  Cargado:  {cargado}")
        print(f"  x={cargado['x']}, y={cargado['y']}")

    # --------------------------------------------------------
    # EJERCICIO 3: Lista de usuarios en JSON
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_json_lista():
        ruta = os.path.join(DATA_DIR, "usuarios.json")
        usuarios = [
            {"nombre": "Ana Martínez", "edad": 22},
            {"nombre": "Luis Torres",  "edad": 25}
        ]

        # Guardar
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=2, ensure_ascii=False)
        print(f"  Guardados {len(usuarios)} usuarios")

        # Cargar y recorrer
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("  Usuarios cargados:")
        for u in data:
            print(f"    → {u['nombre']}, {u['edad']} años")


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia): Registro de notas
# ----------------------------------------------------------
class RegistroNotas:
    """Guarda y carga notas de estudiantes en JSON."""

    def __init__(self):
        self._ruta = os.path.join(DATA_DIR, "notas_estudiantes.json")
        self._datos: List[Dict[str, Any]] = self._cargar()

    def _cargar(self) -> List[Dict[str, Any]]:
        try:
            with open(self._ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _guardar(self) -> None:
        with open(self._ruta, "w", encoding="utf-8") as f:
            json.dump(self._datos, f, indent=2, ensure_ascii=False)

    def agregar(self, nombre: str, notas: List[float]) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not notas:
            raise ValueError("Debe tener al menos una nota")
        promedio = round(sum(notas) / len(notas), 2)
        entrada = {"nombre": nombre, "notas": notas, "promedio": promedio}
        self._datos.append(entrada)
        self._guardar()
        print(f"  Registrado: {nombre} | promedio={promedio}")

    def listar(self) -> None:
        if not self._datos:
            print("  Sin registros.")
            return
        print("  Registro de estudiantes:")
        for est in self._datos:
            estado = "Aprobado" if est["promedio"] >= 7 else "Reprobado"
            print(f"    {est['nombre']:20} Promedio: {est['promedio']:.2f}  [{estado}]")

    def limpiar(self) -> None:
        self._datos = []
        self._guardar()


def ejecutar_bloque_16():
    print("\n" + "="*55)
    print("  BLOQUE 16: ARCHIVOS Y JSON")
    print("="*55)

    maf = ManejadorArchivos()

    print("\n--- Ejercicio 1: Escribir y leer archivo de texto ---")
    maf.ejercicio_escribir_leer()

    print("\n--- Ejercicio 2: Dict a JSON y vuelta ---")
    maf.ejercicio_json_dict()

    print("\n--- Ejercicio 3: Lista de usuarios en JSON ---")
    maf.ejercicio_json_lista()

    print("\n--- Proceso similar (propio): RegistroNotas ---")
    rn = RegistroNotas()
    rn.limpiar()  # reiniciar para la demo
    rn.agregar("Fiorella Solis", [9, 8, 10, 9])
    rn.agregar("Carlos Mora",    [6, 7, 5, 8])
    rn.agregar("Valeria Cruz",   [10, 9, 10, 8])
    rn.listar()

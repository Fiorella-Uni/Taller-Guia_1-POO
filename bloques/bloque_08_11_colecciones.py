# ============================================================
# BLOQUES 8-11: LISTAS, TUPLAS, DICCIONARIOS, CONJUNTOS
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame en detalle listas, tuplas, diccionarios y
# conjuntos en Python: métodos, diferencias, cuándo usar cada uno y el
# concepto de referencia vs copia."
# Prompt proceso similar: "Genera ejercicios donde se combinen estas 4
# estructuras de datos en una clase que gestione un inventario."
# Resolución propia: clase GestorEstudiantes (ver proceso similar abajo)

from typing import List, Dict, Set, Tuple, Any


# ============================================================
# BLOQUE 8: LISTAS
# ============================================================
class GestorListas:
    """Demuestra operaciones con listas."""

    # --------------------------------------------------------
    # EJERCICIO 1: Crear lista, agregar con append, ordenar
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_append_sort():
        calificaciones: List[float] = []
        calificaciones.append(7.5)
        calificaciones.append(9.0)
        calificaciones.append(6.8)
        calificaciones.append(8.3)
        calificaciones.append(10.0)

        print(f"  Lista original:  {calificaciones}")
        calificaciones.sort()
        print(f"  Después sort():  {calificaciones}")
        calificaciones.reverse()
        print(f"  Después reverse(): {calificaciones}")

    # --------------------------------------------------------
    # EJERCICIO 2: Suma, máximo y mínimo
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_estadisticas():
        nums = [5, 3, 8, 1, 9, 3]
        print(f"  Lista: {nums}")
        print(f"  Suma:  {sum(nums)}")
        print(f"  Máx:   {max(nums)}")
        print(f"  Mín:   {min(nums)}")
        print(f"  Largo: {len(nums)}")
        print(f"  sorted (sin modificar): {sorted(nums)}")
        print(f"  Original intacta:       {nums}")

    # --------------------------------------------------------
    # EJERCICIO 3: Referencia vs copia
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_referencia_copia():
        lista_original = [1, 2, 3]
        copia_referencia = lista_original     # MISMA referencia
        copia_real = lista_original.copy()    # NUEVO objeto

        copia_referencia.append(4)
        print(f"  lista_original    (luego de modificar copia_ref): {lista_original}")
        print(f"  copia_referencia  (también cambió):               {copia_referencia}")
        print(f"  copia_real        (no cambió):                    {copia_real}")
        print(f"  ¿Por qué? Porque copia_referencia apunta al MISMO objeto en memoria.")


# ============================================================
# BLOQUE 9: TUPLAS
# ============================================================
class GestorTuplas:
    """Demuestra operaciones con tuplas."""

    # --------------------------------------------------------
    # EJERCICIO 1: Intento de modificar tupla
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_inmutabilidad():
        tupla = (10, 20, 30, 40)
        print(f"  Tupla: {tupla}")
        try:
            tupla[0] = 99  # type: ignore
        except TypeError as e:
            print(f"  Error al intentar modificar: {e}")
        print(f"  La tupla sigue igual: {tupla}")

    # --------------------------------------------------------
    # EJERCICIO 2: Unpacking con *
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_unpacking():
        valores = (100, 200, 300, 400)
        a, b, *resto = valores
        print(f"  Tupla original: {valores}")
        print(f"  a={a}, b={b}, resto={resto}")

        # Unpacking en bucle de coordenadas
        coordenadas: List[Tuple[int, int]] = [(1, 2), (3, 4), (5, 6)]
        print(f"\n  Coordenadas: {coordenadas}")
        for x, y in coordenadas:
            print(f"    x={x}, y={y}")

    # --------------------------------------------------------
    # EJERCICIO 3: Recorrer lista de coordenadas
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_coordenadas_ciudades():
        ciudades: List[Tuple[str, float, float]] = [
            ("Guayaquil", -2.1894, -79.8891),
            ("Quito",     -0.2295, -78.5243),
            ("Milagro",   -2.1347, -79.5953),
        ]
        print("  Ciudades Ecuador (nombre, lat, lng):")
        for nombre, lat, lng in ciudades:
            print(f"    {nombre:12} → lat={lat}, lng={lng}")


# ============================================================
# BLOQUE 10: DICCIONARIOS
# ============================================================
class GestorDiccionarios:
    """Demuestra operaciones con diccionarios."""

    # --------------------------------------------------------
    # EJERCICIO 1: Crear dict y acceder con [] y get()
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_acceso():
        persona: Dict[str, Any] = {
            "nombre": "Fiorella Solis",
            "edad": 20,
            "ciudad": "Milagro"
        }
        print(f"  Dict: {persona}")
        print(f"  nombre (con []):    {persona['nombre']}")
        print(f"  edad   (con get()): {persona.get('edad')}")
        print(f"  telefono (get safe): {persona.get('telefono', 'No registrado')}")

    # --------------------------------------------------------
    # EJERCICIO 2: Iterar sobre items
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_iterar_items():
        estudiante: Dict[str, Any] = {
            "nombre": "Ana Torres",
            "semestre": 4,
            "promedio": 8.7,
            "activo": True
        }
        print("  Iterando sobre items del diccionario:")
        for clave, valor in estudiante.items():
            print(f"    {clave}: {valor}")

    # --------------------------------------------------------
    # EJERCICIO 3: Referencia vs copia en dict
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_referencia_dict():
        datos_original = {"a": 1, "b": 2}
        copia_ref = datos_original       # misma referencia
        copia_real = datos_original.copy()

        copia_ref["c"] = 3
        print(f"  datos_original (afectado): {datos_original}")
        print(f"  copia_ref      (modificado): {copia_ref}")
        print(f"  copia_real     (intacto):    {copia_real}")
        print(f"  → Usar .copy() para evitar modificar el original")


# ============================================================
# BLOQUE 11: CONJUNTOS (set)
# ============================================================
class GestorConjuntos:
    """Demuestra operaciones con conjuntos."""

    # --------------------------------------------------------
    # EJERCICIO 1: Unión, intersección, diferencia
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_operaciones():
        A: Set[int] = {1, 2, 3, 4, 5}
        B: Set[int] = {4, 5, 6, 7, 8}

        print(f"  A = {sorted(A)}")
        print(f"  B = {sorted(B)}")
        print(f"  Unión (A|B):           {sorted(A | B)}")
        print(f"  Intersección (A&B):    {sorted(A & B)}")
        print(f"  Diferencia (A-B):      {sorted(A - B)}")
        print(f"  Diferencia (B-A):      {sorted(B - A)}")
        print(f"  Dif. simétrica (A^B):  {sorted(A ^ B)}")

    # --------------------------------------------------------
    # EJERCICIO 2: Eliminar duplicados de lista
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_eliminar_duplicados():
        lista_con_dup = [1, 2, 2, 3, 3, 3, 4, 4, 1]
        sin_duplicados = list(set(lista_con_dup))
        sin_duplicados.sort()
        print(f"  Lista original:     {lista_con_dup}")
        print(f"  Sin duplicados:     {sin_duplicados}")

    # --------------------------------------------------------
    # EJERCICIO 3: (A|B) - (A&B) = diferencia simétrica
    # --------------------------------------------------------
    @staticmethod
    def ejercicio_diferencia_simetrica():
        A: Set[int] = {1, 2, 3, 4}
        B: Set[int] = {3, 4, 5, 6}

        resultado = (A | B) - (A & B)
        print(f"  A = {sorted(A)},  B = {sorted(B)}")
        print(f"  (A|B) - (A&B) = {sorted(resultado)}")
        print(f"  A^B           = {sorted(A ^ B)}")
        print(f"  Son iguales: {resultado == (A ^ B)}")
        print(f"  Estos son los elementos que NO comparten A y B.")


# ============================================================
# PROCESO SIMILAR (resolución propia): GestorEstudiantes
# Combina listas, tuplas, diccionarios y conjuntos
# ============================================================
class GestorEstudiantes:
    """Sistema que combina las 4 estructuras de datos."""

    def __init__(self):
        # Lista de dicts — cada estudiante
        self.estudiantes: List[Dict[str, Any]] = []
        # Set para cédulas únicas (evita duplicados)
        self._cedulas_registradas: Set[str] = set()

    def registrar(self, cedula: str, nombre: str, notas: Tuple):
        if not cedula or not nombre:
            raise ValueError("Cédula y nombre son obligatorios")
        if cedula in self._cedulas_registradas:
            raise ValueError(f"La cédula {cedula} ya está registrada")
        if not notas:
            raise ValueError("Debe incluir al menos una nota")

        promedio = sum(notas) / len(notas)
        self.estudiantes.append({
            "cedula": cedula,
            "nombre": nombre,
            "notas": list(notas),
            "promedio": round(promedio, 2)
        })
        self._cedulas_registradas.add(cedula)

    def listar(self):
        if not self.estudiantes:
            print("  Sin estudiantes registrados.")
            return
        for est in self.estudiantes:
            estado = "✓ Aprobado" if est["promedio"] >= 7 else "✗ Reprobado"
            print(f"  [{est['cedula']}] {est['nombre']:20} "
                  f"Promedio: {est['promedio']:.2f}  {estado}")

    def cedulas_unicas(self):
        return sorted(self._cedulas_registradas)


def ejecutar_bloque_8():
    print("\n" + "="*55)
    print("  BLOQUE 8: LISTAS")
    print("="*55)
    gl = GestorListas()
    print("\n--- Ejercicio 1: append y sort ---")
    gl.ejercicio_append_sort()
    print("\n--- Ejercicio 2: Estadísticas ---")
    gl.ejercicio_estadisticas()
    print("\n--- Ejercicio 3: Referencia vs copia ---")
    gl.ejercicio_referencia_copia()


def ejecutar_bloque_9():
    print("\n" + "="*55)
    print("  BLOQUE 9: TUPLAS")
    print("="*55)
    gt = GestorTuplas()
    print("\n--- Ejercicio 1: Inmutabilidad ---")
    gt.ejercicio_inmutabilidad()
    print("\n--- Ejercicio 2: Unpacking ---")
    gt.ejercicio_unpacking()
    print("\n--- Ejercicio 3: Coordenadas ciudades ---")
    gt.ejercicio_coordenadas_ciudades()


def ejecutar_bloque_10():
    print("\n" + "="*55)
    print("  BLOQUE 10: DICCIONARIOS")
    print("="*55)
    gd = GestorDiccionarios()
    print("\n--- Ejercicio 1: Acceso con [] y get() ---")
    gd.ejercicio_acceso()
    print("\n--- Ejercicio 2: Iterar items ---")
    gd.ejercicio_iterar_items()
    print("\n--- Ejercicio 3: Referencia dict ---")
    gd.ejercicio_referencia_dict()


def ejecutar_bloque_11():
    print("\n" + "="*55)
    print("  BLOQUE 11: CONJUNTOS (set)")
    print("="*55)
    gc = GestorConjuntos()
    print("\n--- Ejercicio 1: Operaciones de conjuntos ---")
    gc.ejercicio_operaciones()
    print("\n--- Ejercicio 2: Eliminar duplicados ---")
    gc.ejercicio_eliminar_duplicados()
    print("\n--- Ejercicio 3: Diferencia simétrica ---")
    gc.ejercicio_diferencia_simetrica()

    print("\n--- Proceso similar (propio): GestorEstudiantes ---")
    gestor = GestorEstudiantes()
    gestor.registrar("0912345678", "Fiorella Solis",  (9, 8, 10, 9))
    gestor.registrar("0923456789", "Luis Mendoza",    (6, 7, 5, 8))
    gestor.registrar("0934567890", "Ana Carillo",     (10, 9, 10, 8))
    gestor.listar()
    print(f"\n  Cédulas únicas: {gestor.cedulas_unicas()}")

    try:
        gestor.registrar("0912345678", "Duplicado", (5, 5, 5))
    except ValueError as e:
        print(f"  Error capturado: {e}")

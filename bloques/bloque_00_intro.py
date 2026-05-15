# ============================================================
# BLOQUE 0: INTRODUCCIÓN A LA POO
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame qué es la POO en Python, qué es una clase
# y qué es un objeto. Muéstrame cómo modelar entidades del mundo real."
# Prompt proceso similar: "Genera un ejercicio similar donde modele un
# sistema diferente al de biblioteca, con al menos 5 clases."
# Resolución propia: sistema de hospital (ver ejercicio 1 resuelto abajo)

# ----------------------------------------------------------
# EJERCICIO 1: Identificar 5 clases para un sistema de biblioteca
# ----------------------------------------------------------
# Clases identificadas:
#   1. Libro        → representa un libro con título, autor, ISBN
#   2. Usuario      → persona que puede pedir prestado libros
#   3. Prestamo     → relación entre un usuario y un libro
#   4. Autor        → persona que escribió uno o más libros
#   5. Categoria    → clasificación temática de los libros

class Libro:
    def __init__(self, isbn, titulo, autor):
        if not isbn or not titulo:
            raise ValueError("ISBN y título son obligatorios")
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: '{self.titulo}' de {self.autor} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, id_usuario, nombre, email):
        if not nombre:
            raise ValueError("El nombre del usuario no puede estar vacío")
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Usuario [{self.id_usuario}]: {self.nombre} - {self.email}"


class Prestamo:
    def __init__(self, id_prestamo, libro, usuario, fecha):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha

    def __str__(self):
        return (f"Préstamo #{self.id_prestamo}: '{self.libro.titulo}' "
                f"→ {self.usuario.nombre} ({self.fecha})")


class Autor:
    def __init__(self, nombre, nacionalidad):
        if not nombre:
            raise ValueError("El nombre del autor es obligatorio")
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre} ({self.nacionalidad})"


class Categoria:
    def __init__(self, nombre, descripcion="Sin descripción"):
        if not nombre:
            raise ValueError("La categoría debe tener nombre")
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Categoría: {self.nombre} - {self.descripcion}"


# ----------------------------------------------------------
# EJERCICIO 2: Clase Persona con nombre y edad, 3 objetos
# ----------------------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"


# ----------------------------------------------------------
# EJERCICIO 3 (proceso similar — resolución propia):
# Sistema de Hospital: Paciente, Medico, Cita, Especialidad, Hospital
# ----------------------------------------------------------
class Paciente:
    def __init__(self, cedula, nombre):
        if not cedula or not nombre:
            raise ValueError("Cédula y nombre son obligatorios")
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        return f"Paciente: {self.nombre} (Cédula: {self.cedula})"


class Medico:
    def __init__(self, codigo, nombre, especialidad):
        if not nombre or not especialidad:
            raise ValueError("Nombre y especialidad son obligatorios")
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad}"


def ejecutar_bloque_0():
    print("\n" + "="*55)
    print("  BLOQUE 0: INTRODUCCIÓN A LA POO")
    print("="*55)

    print("\n--- Ejercicio 1: 5 clases del sistema biblioteca ---")
    libro1 = Libro("978-0-13", "Clean Code", "Robert C. Martin")
    libro2 = Libro("978-0-20", "Design Patterns", "Gang of Four")
    usuario1 = Usuario(1, "Fiorella Solis", "fsolis@unemi.edu.ec")
    autor1 = Autor("Robert C. Martin", "Estadounidense")
    cat1 = Categoria("Ingeniería de Software", "Libros técnicos de desarrollo")
    prestamo1 = Prestamo(1, libro1, usuario1, "2025-05-14")

    print(libro1)
    print(libro2)
    print(usuario1)
    print(autor1)
    print(cat1)
    print(prestamo1)

    print("\n--- Ejercicio 2: Clase Persona — 3 instancias ---")
    p1 = Persona("Ana García", 22)
    p2 = Persona("Luis Pérez", 30)
    p3 = Persona("María Rodríguez", 19)
    for p in [p1, p2, p3]:
        print(p)

    print("\n--- Ejercicio 3 (proceso similar): Sistema Hospital ---")
    pac = Paciente("0912345678", "Carlos Mendoza")
    med = Medico("M001", "Sofía Vargas", "Cardiología")
    print(pac)
    print(med)

    print("\n--- Reflexión: Diferencia entre clase y objeto ---")
    print("Clase  → es el MOLDE/PLANO (ej: la clase 'Persona' define qué tiene)")
    print("Objeto → es la INSTANCIA REAL creada a partir del molde")
    print("         (ej: p1 = Persona('Ana',22) → Ana ES un objeto de tipo Persona)")

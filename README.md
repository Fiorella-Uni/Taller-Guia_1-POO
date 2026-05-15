# 📘 Guía Práctica 1 — Programación Orientada a Objetos en Python

**Estudiante:** Fiorella Solis  
**Universidad:** Universidad Estatal de Milagro (UNEMI)  
**Asignatura:** Programación Orientada a Objetos  
**Ciclo:** 2025  

---

## 📂 Estructura del Proyecto

```
poo_fiorella_solis/
├── menu.py                              ← Punto de entrada principal
├── README.md                            ← Este archivo
├── data/                                ← Archivos generados (JSON, TXT)
│   ├── ejemplo.txt
│   ├── coordenada.json
│   ├── usuarios.json
│   └── notas_estudiantes.json
└── bloques/
    ├── bloque_00_intro.py               ← Bloque 0: Introducción a POO
    ├── bloque_01_constructor.py         ← Bloque 1: Constructor __init__
    ├── bloque_02_tipos.py               ← Bloque 2: Variables y Tipos
    ├── bloque_03_operadores.py          ← Bloque 3: Operadores
    ├── bloque_04_entrada_salida.py      ← Bloque 4: Input / Print
    ├── bloque_05_condicionales.py       ← Bloque 5: Condicionales
    ├── bloque_06_bucles.py              ← Bloque 6: Bucles
    ├── bloque_07_funciones.py           ← Bloque 7: Funciones
    ├── bloque_08_11_colecciones.py      ← Bloques 8-11: Colecciones
    ├── bloque_12_excepciones.py         ← Bloque 12: Excepciones
    ├── bloque_13_15_decoradores_up_hop.py ← Bloques 13-15: Avanzado
    ├── bloque_16_archivos_json.py       ← Bloque 16: Archivos y JSON
    └── bloque_17_mixins.py              ← Bloque 17: Mixins
```

---

## 🚀 Cómo Ejecutar

```bash
# Desde la carpeta raíz del proyecto
python menu.py
```

El menú interactivo permite:
- Navegar por **grupos** de bloques (A, B, C, D, E)
- Ejecutar un **bloque individual**
- Ejecutar **todos los bloques** a la vez (opción T)

---

## 📋 Descripción de Bloques

| Bloque | Tema | Archivo |
|--------|------|---------|
| 0 | Introducción a la POO | bloque_00_intro.py |
| 1 | Constructor `__init__` | bloque_01_constructor.py |
| 2 | Variables y Tipos de Datos | bloque_02_tipos.py |
| 3 | Operadores | bloque_03_operadores.py |
| 4 | Entrada y Salida | bloque_04_entrada_salida.py |
| 5 | Condicionales | bloque_05_condicionales.py |
| 6 | Bucles | bloque_06_bucles.py |
| 7 | Funciones | bloque_07_funciones.py |
| 8 | Listas | bloque_08_11_colecciones.py |
| 9 | Tuplas | bloque_08_11_colecciones.py |
| 10 | Diccionarios | bloque_08_11_colecciones.py |
| 11 | Conjuntos (set) | bloque_08_11_colecciones.py |
| 12 | Excepciones | bloque_12_excepciones.py |
| 13 | Decoradores | bloque_13_15_decoradores_up_hop.py |
| 14 | Unpacking | bloque_13_15_decoradores_up_hop.py |
| 15 | Funciones de Orden Superior | bloque_13_15_decoradores_up_hop.py |
| 16 | Archivos y JSON | bloque_16_archivos_json.py |
| 17 | Mixins | bloque_17_mixins.py |

---

## 🤖 Uso de Inteligencia Artificial

**IA utilizada:** Claude (Anthropic) — claude.ai

---

### Bloque 0 — Introducción a la POO

**Prompt principal:**
> "Explícame qué es la POO en Python, qué es una clase y qué es un objeto. Muéstrame cómo modelar entidades del mundo real con un ejemplo de sistema de biblioteca."

**Prompt proceso similar:**
> "Genera un ejercicio similar donde modele un sistema diferente al de biblioteca, con al menos 5 clases relacionadas entre sí. Explícame cómo se relacionan."

**Resolución propia:** Modelé un sistema de hospital con las clases Paciente, Medico, Cita, Especialidad y Hospital, identificando las relaciones entre ellas de forma independiente.

---

### Bloque 1 — Constructor `__init__`

**Prompt principal:**
> "Explícame cómo funciona `__init__` en Python, qué es `self`, cómo validar datos dentro del constructor y cómo crear constructores alternativos con `@classmethod`. Muéstrame ejemplos con validaciones reales."

**Prompt proceso similar:**
> "Genera un ejercicio similar al de Producto pero con una clase diferente que tenga al menos 3 atributos, validaciones en el constructor y un `@classmethod` para crear la instancia desde diccionario."

**Resolución propia:** Creé la clase `Vehiculo` con placa, marca y año, validando el rango del año (1900-2026) y añadí el `@classmethod desde_diccionario` por mi cuenta.

---

### Bloque 2 — Variables y Tipos de Datos

**Prompt principal:**
> "Explícame todos los tipos de datos en Python: int, float, str, bool, None, list, tuple, dict y set. Muéstrame acceso por índice y slicing con ejemplos claros."

**Prompt proceso similar:**
> "Crea un ejercicio con una clase que use los 4 tipos complejos (list, tuple, dict, set) y muestre acceso a índices, slicing y valores de diccionario."

**Resolución propia:** Creé la clase `Inventario` que combina string, lista y diccionario con acceso a sus elementos.

---

### Bloque 3 — Operadores

**Prompt principal:**
> "Explícame todos los operadores en Python: aritméticos, de comparación, lógicos, la diferencia crítica entre `==` e `is`, y la precedencia de operadores de mayor a menor prioridad."

**Prompt proceso similar:**
> "Dame una expresión matemática con varios operadores mezclados para que yo practique explicar el orden de evaluación paso a paso, como hice con `2 + 1 * 2 % 2 + (2**1)//2`."

**Resolución propia:** Evalué `y = 3 ** 2 - 4 * (6 // 2) + 10 % 3` explicando cada paso del orden de evaluación.

---

### Bloque 4 — Entrada y Salida

**Prompt principal:**
> "Explícame cómo usar `input()` y `print()` en Python, qué es el casting de tipos, cómo usar f-strings, y qué pasa si no convierto el input antes de operar con él."

**Prompt proceso similar:**
> "Crea un ejercicio donde el usuario ingrese peso y altura para calcular su IMC, mostrando la categoría correspondiente con f-strings."

**Resolución propia:** Implementé la `calculadora_imc()` con todas las categorías de IMC y formato adecuado.

---

### Bloque 5 — Condicionales

**Prompt principal:**
> "Explícame los condicionales en Python: estructura if/elif/else, operador ternario, match-case (Python 3.10+) y short-circuit evaluation. Muéstrame un sistema de login básico."

**Prompt proceso similar:**
> "Genera un sistema de validación de contraseñas que use if/elif/else con múltiples condiciones: longitud, mayúsculas y números, mostrando el nivel de seguridad."

**Resolución propia:** Creé el validador `validar_contrasena()` que clasifica la fortaleza en 4 niveles.

---

### Bloque 6 — Bucles

**Prompt principal:**
> "Explícame los bucles `while` y `for` en Python: uso con `range()`, sobre colecciones, `enumerate()`, `items()`, `break`, `continue` y list/dict comprehension con ejemplos."

**Prompt proceso similar:**
> "Crea ejercicios para practicar: uno con tabla de multiplicar usando for, y otro con un patrón visual usando bucles anidados."

**Resolución propia:** Implementé la tabla de multiplicar del 7 y una pirámide de asteriscos con `for` anidado.

---

### Bloque 7 — Funciones

**Prompt principal:**
> "Explícame las funciones en Python: parámetros por defecto, retorno de múltiples valores, `*args`, `**kwargs`, funciones lambda y recursividad con factorial y Fibonacci."

**Prompt proceso similar:**
> "Genera una función recursiva diferente al factorial para que yo practique la recursividad. Que tenga caso base claro y llamada recursiva identificable."

**Resolución propia:** Creé `suma_digitos(n)` que suma recursivamente los dígitos de un número entero.

---

### Bloque 8 — Listas

**Prompt principal:**
> "Explícame los métodos principales de listas en Python: append, extend, insert, pop, remove, sort, reverse, copy. Explícame la diferencia crucial entre referencia y copia."

**Prompt proceso similar:**
> "Crea un ejercicio donde se demuestre claramente qué pasa cuando copias una lista por referencia y por `.copy()`, modificando ambas."

**Resolución propia:** Implementé `ejercicio_referencia_copia()` mostrando cómo `copia_ref` afecta al original pero `copia_real` no.

---

### Bloque 9 — Tuplas

**Prompt principal:**
> "Explícame las tuplas en Python: inmutabilidad, cuándo usarlas en lugar de listas, desempaquetado básico y con `*`, y cómo recorrer una lista de tuplas."

**Prompt proceso similar:**
> "Genera un ejercicio donde desempaquete tuplas de coordenadas de ciudades ecuatorianas y las muestre formateadas."

**Resolución propia:** Creé `ejercicio_coordenadas_ciudades()` con Guayaquil, Quito y Milagro.

---

### Bloque 10 — Diccionarios

**Prompt principal:**
> "Explícame los diccionarios en Python: acceso con `[]` vs `.get()`, métodos keys/values/items, `.update()`, `.copy()`, dict comprehension y diccionarios anidados."

**Prompt proceso similar:**
> "Crea un ejercicio que demuestre la diferencia entre copiar un diccionario por referencia vs con `.copy()`."

**Resolución propia:** Implementé `ejercicio_referencia_dict()` demostrando ambos comportamientos.

---

### Bloque 11 — Conjuntos

**Prompt principal:**
> "Explícame los conjuntos en Python: propiedades (sin orden, sin duplicados), operaciones matemáticas (unión, intersección, diferencia, diferencia simétrica) y cómo eliminar duplicados de una lista."

**Prompt proceso similar:**
> "Explícame por qué `(A|B) - (A&B)` es igual a `A^B`. Dame un ejercicio para demostrarlo con números concretos."

**Resolución propia:** Demostré con A={1,2,3,4} y B={3,4,5,6} que ambas expresiones dan el mismo resultado.

---

### Bloque 12 — Excepciones

**Prompt principal:**
> "Explícame el manejo de excepciones en Python: estructura completa try/except/else/finally, tipos de error comunes, `raise`, `assert` y cómo crear excepciones personalizadas heredando de Exception."

**Prompt proceso similar:**
> "Crea un sistema bancario básico con excepciones propias: una para saldo insuficiente y otra para datos inválidos."

**Resolución propia:** Creé `SaldoInsuficienteError` y `DatoInvalidoError`, y las usé en la clase `CuentaBancaria`.

---

### Bloque 13 — Decoradores

**Prompt principal:**
> "Explícame los decoradores en Python paso a paso: qué son, cómo se aplican con `@`, cómo se usa `functools.wraps` para preservar el nombre de la función, y para qué sirven en la vida real."

**Prompt proceso similar:**
> "Crea un decorador que mida el tiempo de ejecución de una función en milisegundos, para practicar el patrón de decoradores con casos reales."

**Resolución propia:** Creé `@medir_tiempo` usando `time.perf_counter()` aplicado a `sumar_lista_grande`.

---

### Bloque 14 — Unpacking

**Prompt principal:**
> "Explícame el unpacking en Python: básico, con operador `*` para capturar el resto, cómo pasar listas como argumentos con `*lista`, y cómo combinar diccionarios con `**`."

**Prompt proceso similar:**
> "Genera ejercicios de unpacking donde yo practique: desempaquetar una tupla con `*`, pasar una lista a una función con `*`, y combinar dos diccionarios con `**`."

**Resolución propia:** Resolví los tres ejercicios: `(primera, *mitad, ultima)`, `multiplicar(*lista)` y `{**dict1, **dict2}`.

---

### Bloque 15 — Funciones de Orden Superior

**Prompt principal:**
> "Explícame `map()`, `filter()` y `reduce()` en Python con ejemplos concretos. Muéstrame cómo combinarlos en cadena para procesar listas."

**Prompt proceso similar:**
> "Crea un ejercicio tipo pipeline donde combine filter + map + reduce para procesar una lista de ventas: filtrar las grandes, aplicar descuento y calcular el total."

**Resolución propia:** Implementé `pipeline_funcional()` que filtra ventas > 100, aplica 10% de descuento y suma el total.

---

### Bloque 16 — Archivos y JSON

**Prompt principal:**
> "Explícame cómo trabajar con archivos en Python: modos de apertura (r/w/a), uso del `with`, lectura línea a línea. Y cómo guardar y cargar datos JSON con `json.dump` y `json.load`."

**Prompt proceso similar:**
> "Crea un sistema que guarde y cargue registros de estudiantes con notas en formato JSON, con validaciones al agregar registros."

**Resolución propia:** Creé la clase `RegistroNotas` que persiste datos en `notas_estudiantes.json` con validaciones.

---

### Bloque 17 — Mixins

**Prompt principal:**
> "Explícame qué es un Mixin en Python: qué lo diferencia de una clase normal, cómo se hereda, qué es el MRO (Method Resolution Order) y para qué casos reales se usa."

**Prompt proceso similar:**
> "Crea un mixin de auditoría que registre automáticamente cuándo se crea un objeto y cuándo se cambian sus propiedades, para practicar mixins con casos útiles."

**Resolución propia:** Creé `AuditoriaMixin` con `_registrar_evento()` y lo integré en la clase `Producto` usando `@property` para detectar cambios de precio.

---

## ✅ Validaciones Implementadas

Todos los ejercicios incluyen validaciones como indica la guía:

- Datos obligatorios: se lanza `ValueError` si están vacíos
- Rangos numéricos: precios ≥ 0, notas entre 0-10, edades válidas
- Tipos de datos: se verifica con `isinstance()` antes de operar
- Emails: se valida formato con expresión regular
- Duplicados: se usa `set` para evitar registros repetidos
- Excepciones personalizadas en bloque 12 y 17

---

## 📌 Notas Técnicas

- Python requerido: **3.10+** (para match-case en bloque 5)
- Sin dependencias externas — solo librería estándar
- Los archivos JSON se generan automáticamente en `/data/`
- El bloque 4 usa datos fijos en lugar de `input()` para funcionar en modo demo

---

*Tarea desarrollada con apoyo de Claude (Anthropic) siguiendo la metodología indicada:  
explicación → proceso similar → resolución propia → repetición hasta comprender.*

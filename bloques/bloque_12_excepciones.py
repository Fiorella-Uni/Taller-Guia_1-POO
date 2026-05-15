# ============================================================
# BLOQUE 12: EXCEPCIONES (try / except)
# Estudiante: Fiorella Solis
# Asignatura: Programación Orientada a Objetos - UNEMI
# ============================================================

# IA utilizada: Claude
# Prompt principal: "Explícame el manejo de excepciones en Python:
# try/except/else/finally, tipos de error comunes, raise, assert
# y cómo crear excepciones personalizadas."
# Prompt proceso similar: "Crea un sistema de registro de usuarios
# que valide datos y use múltiples tipos de excepciones."
# Resolución propia: sistema de banco con excepciones propias (ver abajo)


# ----------------------------------------------------------
# Excepción personalizada
# ----------------------------------------------------------
class SaldoInsuficienteError(Exception):
    """Se lanza cuando no hay saldo suficiente para la operación."""
    def __init__(self, saldo_actual: float, monto_solicitado: float):
        self.saldo_actual = saldo_actual
        self.monto_solicitado = monto_solicitado
        super().__init__(
            f"Saldo insuficiente: tienes ${saldo_actual:.2f}, "
            f"intentas retirar ${monto_solicitado:.2f}"
        )


class DatoInvalidoError(Exception):
    """Se lanza cuando un dato ingresado no es válido."""
    pass


# ----------------------------------------------------------
# EJERCICIO 1: Capturar ValueError al convertir input a int
# ----------------------------------------------------------
class ConversorEntero:
    @staticmethod
    def convertir(valor: str) -> int:
        try:
            resultado = int(valor)
            return resultado
        except ValueError as e:
            print(f"  Error de conversión: '{valor}' no es un entero válido → {e}")
            return -1


# ----------------------------------------------------------
# EJERCICIO 2: Capturar IndexError
# ----------------------------------------------------------
class AccesoLista:
    @staticmethod
    def acceder(lista: list, indice: int):
        try:
            return lista[indice]
        except IndexError as e:
            print(f"  IndexError: índice {indice} fuera de rango "
                  f"(lista tiene {len(lista)} elementos) → {e}")
            return None


# ----------------------------------------------------------
# EJERCICIO 3: Manejar ValueError y ZeroDivisionError
# ----------------------------------------------------------
class Calculadora:
    @staticmethod
    def dividir_texto(a_str: str, b_str: str):
        try:
            a = float(a_str)
            b = float(b_str)
            resultado = a / b
            print(f"  {a} / {b} = {resultado:.4f}")
        except ValueError as e:
            print(f"  ValueError: entrada no numérica → {e}")
        except ZeroDivisionError:
            print(f"  ZeroDivisionError: no se puede dividir entre cero")
        else:
            print(f"  División completada sin errores")
        finally:
            print(f"  [finally] Operación finalizada")


# ----------------------------------------------------------
# PROCESO SIMILAR (resolución propia): CuentaBancaria
# ----------------------------------------------------------
class CuentaBancaria:
    """Sistema bancario básico con manejo de excepciones."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        if not titular:
            raise DatoInvalidoError("El titular no puede estar vacío")
        if saldo_inicial < 0:
            raise DatoInvalidoError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self._saldo = saldo_inicial
        self._historial: list = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, monto: float) -> None:
        try:
            assert isinstance(monto, (int, float)), "El monto debe ser numérico"
            assert monto > 0, "El monto debe ser mayor a cero"
            self._saldo += monto
            self._historial.append(f"+${monto:.2f}")
            print(f"  Depósito de ${monto:.2f} exitoso. Saldo: ${self._saldo:.2f}")
        except AssertionError as e:
            raise DatoInvalidoError(str(e))

    def retirar(self, monto: float) -> None:
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise DatoInvalidoError("El monto de retiro debe ser un número positivo")
        if monto > self._saldo:
            raise SaldoInsuficienteError(self._saldo, monto)

        self._saldo -= monto
        self._historial.append(f"-${monto:.2f}")
        print(f"  Retiro de ${monto:.2f} exitoso. Saldo: ${self._saldo:.2f}")

    def historial(self) -> None:
        print(f"  Historial de {self.titular}: {self._historial}")

    def __str__(self):
        return f"Cuenta de {self.titular} | Saldo: ${self._saldo:.2f}"


def ejecutar_bloque_12():
    print("\n" + "="*55)
    print("  BLOQUE 12: EXCEPCIONES")
    print("="*55)

    print("\n--- Ejercicio 1: ValueError con int() ---")
    conv = ConversorEntero()
    print(f"  Convertir '42'  → {conv.convertir('42')}")
    conv.convertir("abc")
    conv.convertir("3.14")

    print("\n--- Ejercicio 2: IndexError con lista ---")
    acc = AccesoLista()
    mi_lista = [10, 20, 30]
    print(f"  lista[1] = {acc.acceder(mi_lista, 1)}")
    acc.acceder(mi_lista, 5)

    print("\n--- Ejercicio 3: ValueError y ZeroDivisionError ---")
    calc = Calculadora()
    calc.dividir_texto("10", "4")
    print()
    calc.dividir_texto("10", "0")
    print()
    calc.dividir_texto("abc", "2")

    print("\n--- Proceso similar (propio): CuentaBancaria ---")
    try:
        cuenta = CuentaBancaria("Fiorella Solis", 100.0)
        print(f"  {cuenta}")
        cuenta.depositar(250.0)
        cuenta.retirar(80.0)
        cuenta.retirar(500.0)  # debe lanzar SaldoInsuficienteError
    except SaldoInsuficienteError as e:
        print(f"  SaldoInsuficienteError capturado: {e}")
    except DatoInvalidoError as e:
        print(f"  DatoInvalidoError capturado: {e}")
    finally:
        print("  [finally] Operación bancaria finalizada")

    cuenta.historial()

    try:
        cuenta_invalida = CuentaBancaria("", 50)
    except DatoInvalidoError as e:
        print(f"\n  DatoInvalidoError al crear cuenta: {e}")

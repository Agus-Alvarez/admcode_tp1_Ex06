# calculator_package/
# ├── calculator/
# │   ├── __init__.py
# │   └── complex_calculator.py
# └── test/
#     ├── __init__.py
#     └── test_complex_calculator.py

# calculator_package/calculator/complex_calculator.py
class SimpleComplexCalculator:
    """
    Calculadora de números complejos que realiza operaciones aritméticas básicas.
    Incluye validaciones de tipo y manejo de errores.
    """
    
    def __init__(self):
        pass
    
    def _validar_numeros(self, c1: list, c2: list) -> None:
        """
        Valida que las entradas sean listas de dos números.
        
        Args:
            c1, c2: Números complejos en formato [real, imaginario]
            
        Raises:
            TypeError: Si los argumentos no son del tipo correcto
            ValueError: Si las listas no tienen el formato correcto
        """
        if not isinstance(c1, list) or not isinstance(c2, list):
            raise TypeError("Los argumentos deben ser listas")
        if len(c1) != 2 or len(c2) != 2:
            raise ValueError("Los números complejos deben ser listas de dos elementos")
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in c1 + c2):
            raise TypeError("Todos los elementos deben ser números enteros o flotantes")
    
    def sumar(self, c1: list, c2: list) -> list:
        """
        Suma dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            return [c1[0] + c2[0], c1[1] + c2[1]]
        except (TypeError, ValueError) as e:
            return "ERROR"
    
    def restar(self, c1: list, c2: list) -> list:
        """
        Resta dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            return [c1[0] - c2[0], c1[1] - c2[1]]
        except (TypeError, ValueError) as e:
            return "ERROR"
    
    def multiplicar(self, c1: list, c2: list) -> list:
        """
        Multiplica dos números complejos con validación.
        """
        try:
            self._validar_numeros(c1, c2)
            real = c1[0] * c2[0] - c1[1] * c2[1]
            imaginario = c1[0] * c2[1] + c1[1] * c2[0]
            return [real, imaginario]
        except (TypeError, ValueError) as e:
            return "ERROR"
    
    def dividir(self, c1: list, c2: list) -> list:
        """
        Divide dos números complejos con validación.
        
        Raises:
            ZeroDivisionError: Si el denominador es cero
        """
        try:
            self._validar_numeros(c1, c2)
            denominador = c2[0]**2 + c2[1]**2
            if denominador == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            
            real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominador
            imaginario = (c1[1] * c2[0] - c1[0] * c2[1]) / denominador
            return [real, imaginario]
        except ZeroDivisionError as e:
            raise e
        except (TypeError, ValueError) as e:
            return "ERROR"
    
    @staticmethod
    def formato_complejo(c: list) -> str:
        """
        Formatea un número complejo como string.
        """
        try:
            if not isinstance(c, list) or len(c) != 2:
                return "ERROR"
            if not all(isinstance(x, (int, float)) for x in c):
                return "ERROR"
            if c[1] >= 0:
                return f"{c[0]:.2f} + {c[1]:.2f}i"
            return f"{c[0]:.2f} - {abs(c[1]):.2f}i"
        except:
            return "ERROR"

"""
calculator_core.py - Core mathematical functions for Python Scientific Calculator
Author: Python Calculator Project
Description: Modular mathematical functions that can be imported by both CLI and GUI versions
"""

import math
import cmath
from typing import Union, Tuple, List
from decimal import Decimal, getcontext

# Set decimal precision for high-precision calculations
getcontext().prec = 50


class MathematicalFunctions:
    """Core mathematical functions for the scientific calculator."""

    @staticmethod
    def basic_operations(a: float, b: float, operation: str) -> float:
        """Perform basic arithmetic operations."""
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else None,
            '**': lambda x, y: x ** y,
            '%': lambda x, y: x % y if y != 0 else None,
            '//': lambda x, y: x // y if y != 0 else None
        }

        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")

        result = operations[operation](a, b)
        if result is None:
            raise ZeroDivisionError("Division by zero")

        return result

    @staticmethod
    def trigonometric_functions(x: float, function: str, angle_mode: str = "degrees") -> float:
        """Trigonometric functions with angle mode support."""
        # Convert to radians if in degree mode
        if angle_mode.lower() == "degrees" and function in ['sin', 'cos', 'tan']:
            x_rad = math.radians(x)
        else:
            x_rad = x

        functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'asinh': math.asinh,
            'acosh': math.acosh,
            'atanh': math.atanh
        }

        if function not in functions:
            raise ValueError(f"Unknown trigonometric function: {function}")

        # Input validation for inverse trig functions
        if function in ['asin', 'acos'] and abs(x) > 1:
            raise ValueError(f"{function} requires input between -1 and 1")
        if function == 'acosh' and x < 1:
            raise ValueError("acosh requires input >= 1")
        if function == 'atanh' and abs(x) >= 1:
            raise ValueError("atanh requires input between -1 and 1")

        if function in ['sin', 'cos', 'tan']:
            result = functions[function](x_rad)
        else:
            result = functions[function](x)

        # Convert result back to degrees for inverse functions if needed
        if angle_mode.lower() == "degrees" and function in ['asin', 'acos', 'atan']:
            result = math.degrees(result)

        return result

    @staticmethod
    def logarithmic_functions(x: float, function: str, base: float = None) -> float:
        """Logarithmic and exponential functions."""
        if x <= 0 and function in ['ln', 'log', 'log2', 'log_base']:
            raise ValueError("Logarithm requires positive input")

        functions = {
            'ln': lambda: math.log(x),
            'log': lambda: math.log10(x),
            'log2': lambda: math.log2(x),
            'log_base': lambda: math.log(x, base) if base and base > 0 and base != 1 else None,
            'exp': lambda: math.exp(x),
            'exp2': lambda: 2 ** x,
            'exp10': lambda: 10 ** x
        }

        if function not in functions:
            raise ValueError(f"Unknown logarithmic function: {function}")

        if function == 'log_base' and (not base or base <= 0 or base == 1):
            raise ValueError("Invalid logarithm base")

        result = functions[function]()
        if result is None:
            raise ValueError("Invalid logarithm calculation")

        return result

    @staticmethod
    def power_and_root_functions(x: float, function: str, n: float = None) -> float:
        """Power and root functions."""
        functions = {
            'sqrt': lambda: math.sqrt(x) if x >= 0 else None,
            'cbrt': lambda: x ** (1/3),
            'nth_root': lambda: x ** (1/n) if n != 0 else None,
            'square': lambda: x ** 2,
            'cube': lambda: x ** 3,
            'power': lambda: x ** n if n is not None else None,
            'reciprocal': lambda: 1 / x if x != 0 else None
        }

        if function not in functions:
            raise ValueError(f"Unknown power/root function: {function}")

        if function == 'sqrt' and x < 0:
            raise ValueError("Square root of negative number")
        if function == 'nth_root' and n == 0:
            raise ValueError("Root index cannot be zero")
        if function == 'reciprocal' and x == 0:
            raise ZeroDivisionError("Division by zero")
        if function in ['nth_root', 'power'] and n is None:
            raise ValueError("Missing required parameter")

        result = functions[function]()
        if result is None:
            raise ValueError("Invalid calculation")

        return result

    @staticmethod
    def statistical_functions(numbers: List[float], function: str) -> float:
        """Statistical functions for lists of numbers."""
        if not numbers:
            raise ValueError("Empty list provided")

        functions = {
            'mean': lambda: sum(numbers) / len(numbers),
            'median': lambda: MathematicalFunctions._median(numbers),
            'mode': lambda: MathematicalFunctions._mode(numbers),
            'std_dev': lambda: MathematicalFunctions._standard_deviation(numbers),
            'variance': lambda: MathematicalFunctions._variance(numbers),
            'sum': lambda: sum(numbers),
            'product': lambda: MathematicalFunctions._product(numbers),
            'min': lambda: min(numbers),
            'max': lambda: max(numbers),
            'range': lambda: max(numbers) - min(numbers)
        }

        if function not in functions:
            raise ValueError(f"Unknown statistical function: {function}")

        return functions[function]()

    @staticmethod
    def _median(numbers: List[float]) -> float:
        """Calculate median of a list."""
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            return sorted_nums[n//2]

    @staticmethod
    def _mode(numbers: List[float]) -> float:
        """Calculate mode of a list."""
        from collections import Counter
        counts = Counter(numbers)
        max_count = max(counts.values())
        modes = [num for num, count in counts.items() if count == max_count]
        return modes[0]  # Return first mode if multiple exist

    @staticmethod
    def _standard_deviation(numbers: List[float]) -> float:
        """Calculate standard deviation."""
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)

    @staticmethod
    def _variance(numbers: List[float]) -> float:
        """Calculate variance."""
        mean = sum(numbers) / len(numbers)
        return sum((x - mean) ** 2 for x in numbers) / len(numbers)

    @staticmethod
    def _product(numbers: List[float]) -> float:
        """Calculate product of all numbers."""
        result = 1
        for num in numbers:
            result *= num
        return result

    @staticmethod
    def combinatorics_functions(n: int, r: int, function: str) -> int:
        """Combinatorial functions."""
        if n < 0 or r < 0:
            raise ValueError("Combinatorics require non-negative integers")

        functions = {
            'factorial': lambda: math.factorial(n),
            'permutation': lambda: math.perm(n, r) if r <= n else 0,
            'combination': lambda: math.comb(n, r) if r <= n else 0,
            'double_factorial': lambda: MathematicalFunctions._double_factorial(n)
        }

        if function not in functions:
            raise ValueError(f"Unknown combinatorics function: {function}")

        if function == 'factorial' and n > 170:
            raise ValueError("Factorial input too large")

        return functions[function]()

    @staticmethod
    def _double_factorial(n: int) -> int:
        """Calculate double factorial (n!!)."""
        if n <= 0:
            return 1
        result = 1
        while n > 0:
            result *= n
            n -= 2
        return result

    @staticmethod
    def number_theory_functions(a: int, b: int = None, function: str = "gcd") -> int:
        """Number theory functions."""
        functions = {
            'gcd': lambda: math.gcd(a, b) if b is not None else a,
            'lcm': lambda: abs(a * b) // math.gcd(a, b) if b is not None and b != 0 else None,
            'is_prime': lambda: MathematicalFunctions._is_prime(a),
            'fibonacci': lambda: MathematicalFunctions._fibonacci(a),
            'factorial': lambda: math.factorial(a) if a >= 0 else None
        }

        if function not in functions:
            raise ValueError(f"Unknown number theory function: {function}")

        result = functions[function]()
        if result is None:
            raise ValueError("Invalid calculation")

        return result

    @staticmethod
    def _is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def _fibonacci(n: int) -> int:
        """Calculate nth Fibonacci number."""
        if n < 0:
            raise ValueError("Fibonacci index must be non-negative")
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def conversion_functions(value: float, from_unit: str, to_unit: str, conversion_type: str) -> float:
        """Unit conversion functions."""
        conversions = {
            'temperature': {
                'celsius_to_fahrenheit': lambda c: (c * 9/5) + 32,
                'fahrenheit_to_celsius': lambda f: (f - 32) * 5/9,
                'celsius_to_kelvin': lambda c: c + 273.15,
                'kelvin_to_celsius': lambda k: k - 273.15,
                'fahrenheit_to_kelvin': lambda f: (f - 32) * 5/9 + 273.15,
                'kelvin_to_fahrenheit': lambda k: (k - 273.15) * 9/5 + 32
            },
            'angle': {
                'degrees_to_radians': lambda d: math.radians(d),
                'radians_to_degrees': lambda r: math.degrees(r),
                'degrees_to_gradians': lambda d: d * 10/9,
                'gradians_to_degrees': lambda g: g * 9/10
            },
            'length': {
                'meters_to_feet': lambda m: m * 3.28084,
                'feet_to_meters': lambda f: f / 3.28084,
                'inches_to_cm': lambda i: i * 2.54,
                'cm_to_inches': lambda c: c / 2.54
            }
        }

        if conversion_type not in conversions:
            raise ValueError(f"Unknown conversion type: {conversion_type}")

        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key not in conversions[conversion_type]:
            raise ValueError(f"Unknown conversion: {conversion_key}")

        return conversions[conversion_type][conversion_key](value)

    @staticmethod
    def constants():
        """Mathematical and physical constants."""
        return {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
            'golden_ratio': (1 + math.sqrt(5)) / 2,
            'sqrt2': math.sqrt(2),
            'sqrt3': math.sqrt(3),
            'euler_gamma': 0.5772156649015329,  # Euler-Mascheroni constant
            'speed_of_light': 299792458,  # m/s
            'planck_constant': 6.62607015e-34,  # J⋅s
            'avogadro_number': 6.02214076e23,  # mol⁻¹
            'boltzmann_constant': 1.380649e-23,  # J/K
            'elementary_charge': 1.602176634e-19,  # C
            'gravitational_constant': 6.67430e-11,  # m³⋅kg⁻¹⋅s⁻²
        }


class CalculatorMemory:
    """Memory management for calculator."""

    def __init__(self):
        self.memory = 0.0
        self.history = []
        self.variables = {}

    def store(self, value: float):
        """Store value in memory."""
        self.memory = value

    def recall(self) -> float:
        """Recall value from memory."""
        return self.memory

    def clear(self):
        """Clear memory."""
        self.memory = 0.0

    def add(self, value: float):
        """Add to memory."""
        self.memory += value

    def subtract(self, value: float):
        """Subtract from memory."""
        self.memory -= value

    def multiply(self, value: float):
        """Multiply memory."""
        self.memory *= value

    def divide(self, value: float):
        """Divide memory."""
        if value != 0:
            self.memory /= value
        else:
            raise ZeroDivisionError("Cannot divide memory by zero")

    def add_to_history(self, expression: str, result: str):
        """Add calculation to history."""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 100:  # Keep last 100 calculations
            self.history.pop(0)

    def get_history(self) -> List[str]:
        """Get calculation history."""
        return self.history.copy()

    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()

    def store_variable(self, name: str, value: float):
        """Store a named variable."""
        self.variables[name] = value

    def recall_variable(self, name: str) -> float:
        """Recall a named variable."""
        if name in self.variables:
            return self.variables[name]
        else:
            raise KeyError(f"Variable '{name}' not found")

    def list_variables(self) -> dict:
        """List all stored variables."""
        return self.variables.copy()

    def clear_variables(self):
        """Clear all variables."""
        self.variables.clear()


class ExpressionEvaluator:
    """Safe expression evaluator for calculator."""

    ALLOWED_FUNCTIONS = {
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
        'sinh', 'cosh', 'tanh', 'asinh', 'acosh', 'atanh',
        'log', 'log10', 'log2', 'ln', 'exp', 'sqrt', 'cbrt',
        'abs', 'floor', 'ceil', 'round', 'factorial',
        'pi', 'e', 'tau'
    }

    @staticmethod
    def evaluate_expression(expression: str, angle_mode: str = "degrees") -> float:
        """Safely evaluate a mathematical expression."""
        # Replace common mathematical notation
        expression = expression.replace('^', '**')
        expression = expression.replace('×', '*')
        expression = expression.replace('÷', '/')
        expression = expression.replace('−', '-')

        # Add math module functions
        safe_dict = {
            "__builtins__": {},
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow
        }

        # Add math functions
        for func_name in MathematicalFunctions.constants():
            safe_dict[func_name] = MathematicalFunctions.constants()[func_name]

        # Add trigonometric functions with angle mode support
        if angle_mode.lower() == "degrees":
            safe_dict.update({
                'sin': lambda x: math.sin(math.radians(x)),
                'cos': lambda x: math.cos(math.radians(x)),
                'tan': lambda x: math.tan(math.radians(x)),
                'asin': lambda x: math.degrees(math.asin(x)),
                'acos': lambda x: math.degrees(math.acos(x)),
                'atan': lambda x: math.degrees(math.atan(x))
            })
        else:
            safe_dict.update({
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan
            })

        # Add other math functions
        safe_dict.update({
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'asinh': math.asinh,
            'acosh': math.acosh,
            'atanh': math.atanh,
            'log': math.log10,
            'ln': math.log,
            'log10': math.log10,
            'log2': math.log2,
            'exp': math.exp,
            'sqrt': math.sqrt,
            'cbrt': lambda x: x ** (1/3),
            'factorial': math.factorial,
            'floor': math.floor,
            'ceil': math.ceil
        })

        try:
            result = eval(expression, safe_dict)
            return float(result)
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")


# Example usage and testing
if __name__ == "__main__":
    # Test basic operations
    calc = MathematicalFunctions()
    print("Testing Calculator Core Functions:")
    print("-" * 40)

    # Basic operations
    print(f"5 + 3 = {calc.basic_operations(5, 3, '+')}")
    print(f"10 - 4 = {calc.basic_operations(10, 4, '-')}")
    print(f"6 * 7 = {calc.basic_operations(6, 7, '*')}")
    print(f"15 / 3 = {calc.basic_operations(15, 3, '/')}")

    # Trigonometric functions
    print(f"sin(30°) = {calc.trigonometric_functions(30, 'sin', 'degrees'):.6f}")
    print(f"cos(60°) = {calc.trigonometric_functions(60, 'cos', 'degrees'):.6f}")

    # Logarithmic functions
    print(f"ln(e) = {calc.logarithmic_functions(math.e, 'ln'):.6f}")
    print(f"log10(100) = {calc.logarithmic_functions(100, 'log'):.6f}")

    # Power functions
    print(f"sqrt(16) = {calc.power_and_root_functions(16, 'sqrt')}")
    print(f"2^3 = {calc.power_and_root_functions(2, 'power', 3)}")

    # Combinatorics
    print(f"5! = {calc.combinatorics_functions(5, 0, 'factorial')}")
    print(f"C(5,2) = {calc.combinatorics_functions(5, 2, 'combination')}")

    # Constants
    constants = calc.constants()
    print(f"π = {constants['pi']:.6f}")
    print(f"e = {constants['e']:.6f}")

    print("\nAll tests completed successfully!")
#!/usr/bin/env python3
"""
Python Scientific Calculator - Command Line Interface
Author: Python Calculator Project
Description: A comprehensive calculator with basic and scientific operations
"""

import math
import cmath
import sys
import os
from typing import Union, Tuple

class ScientificCalculator:
    """A comprehensive scientific calculator class."""

    def __init__(self):
        self.memory = 0.0
        self.last_result = 0.0
        self.angle_mode = "degrees"  # "degrees" or "radians"
        self.precision = 6  # decimal places for display

    # Basic Operations
    def add(self, a: float, b: float) -> float:
        """Addition operation."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtraction operation."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplication operation."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Division operation with zero check."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Power operation."""
        try:
            return math.pow(base, exponent)
        except (ValueError, OverflowError) as e:
            raise ValueError(f"Power calculation error: {e}")

    def square_root(self, x: float) -> float:
        """Square root operation."""
        if x < 0:
            raise ValueError("Square root of negative number requires complex mode")
        return math.sqrt(x)

    def nth_root(self, x: float, n: float) -> float:
        """Calculate nth root of x."""
        if n == 0:
            raise ValueError("Root index cannot be zero")
        return math.pow(x, 1/n)

    # Trigonometric Functions
    def _to_radians(self, angle: float) -> float:
        """Convert angle to radians if in degree mode."""
        if self.angle_mode == "degrees":
            return math.radians(angle)
        return angle

    def _from_radians(self, angle: float) -> float:
        """Convert angle from radians if in degree mode."""
        if self.angle_mode == "degrees":
            return math.degrees(angle)
        return angle

    def sine(self, x: float) -> float:
        """Sine function."""
        return math.sin(self._to_radians(x))

    def cosine(self, x: float) -> float:
        """Cosine function."""
        return math.cos(self._to_radians(x))

    def tangent(self, x: float) -> float:
        """Tangent function."""
        return math.tan(self._to_radians(x))

    def arc_sine(self, x: float) -> float:
        """Arc sine function."""
        if abs(x) > 1:
            raise ValueError("Arc sine input must be between -1 and 1")
        return self._from_radians(math.asin(x))

    def arc_cosine(self, x: float) -> float:
        """Arc cosine function."""
        if abs(x) > 1:
            raise ValueError("Arc cosine input must be between -1 and 1")
        return self._from_radians(math.acos(x))

    def arc_tangent(self, x: float) -> float:
        """Arc tangent function."""
        return self._from_radians(math.atan(x))

    # Hyperbolic Functions
    def sinh(self, x: float) -> float:
        """Hyperbolic sine."""
        return math.sinh(x)

    def cosh(self, x: float) -> float:
        """Hyperbolic cosine."""
        return math.cosh(x)

    def tanh(self, x: float) -> float:
        """Hyperbolic tangent."""
        return math.tanh(x)

    # Logarithmic Functions
    def natural_log(self, x: float) -> float:
        """Natural logarithm (base e)."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log(x)

    def log_base_10(self, x: float) -> float:
        """Logarithm base 10."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log10(x)

    def log_base_2(self, x: float) -> float:
        """Logarithm base 2."""
        if x <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log2(x)

    def log_base_n(self, x: float, base: float) -> float:
        """Logarithm with custom base."""
        if x <= 0 or base <= 0 or base == 1:
            raise ValueError("Invalid logarithm inputs")
        return math.log(x, base)

    # Advanced Mathematical Functions
    def factorial(self, n: int) -> int:
        """Factorial function."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n > 170:  # Prevent overflow
            raise ValueError("Factorial input too large (max 170)")
        return math.factorial(n)

    def combination(self, n: int, r: int) -> int:
        """Combination (nCr)."""
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid combination inputs")
        return math.comb(n, r)

    def permutation(self, n: int, r: int) -> int:
        """Permutation (nPr)."""
        if n < 0 or r < 0 or r > n:
            raise ValueError("Invalid permutation inputs")
        return math.perm(n, r)

    def absolute_value(self, x: float) -> float:
        """Absolute value."""
        return abs(x)

    def floor(self, x: float) -> int:
        """Floor function."""
        return math.floor(x)

    def ceiling(self, x: float) -> int:
        """Ceiling function."""
        return math.ceil(x)

    def round_number(self, x: float, digits: int = 0) -> float:
        """Round to specified decimal places."""
        return round(x, digits)

    # Constants
    def get_pi(self) -> float:
        """Return pi constant."""
        return math.pi

    def get_e(self) -> float:
        """Return Euler's number."""
        return math.e

    def get_tau(self) -> float:
        """Return tau constant (2*pi)."""
        return math.tau

    # Memory Functions
    def memory_store(self, value: float) -> None:
        """Store value in memory."""
        self.memory = value

    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory

    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = 0.0

    def memory_add(self, value: float) -> None:
        """Add value to memory."""
        self.memory += value

    def memory_subtract(self, value: float) -> None:
        """Subtract value from memory."""
        self.memory -= value

    # Settings
    def set_angle_mode(self, mode: str) -> None:
        """Set angle mode: 'degrees' or 'radians'."""
        if mode.lower() in ["degrees", "radians"]:
            self.angle_mode = mode.lower()
        else:
            raise ValueError("Angle mode must be 'degrees' or 'radians'")

    def set_precision(self, precision: int) -> None:
        """Set decimal precision for display."""
        if 0 <= precision <= 15:
            self.precision = precision
        else:
            raise ValueError("Precision must be between 0 and 15")

    def format_result(self, result: float) -> str:
        """Format result according to precision setting."""
        if abs(result) < 1e-10:  # Very small numbers
            return "0"
        elif abs(result) > 1e10:  # Very large numbers
            return f"{result:.{self.precision}e}"
        else:
            return f"{result:.{self.precision}f}".rstrip('0').rstrip('.')


class CalculatorInterface:
    """Command-line interface for the scientific calculator."""

    def __init__(self):
        self.calc = ScientificCalculator()
        self.history = []

    def display_menu(self):
        """Display the main calculator menu."""
        print("\n" + "="*60)
        print("           PYTHON SCIENTIFIC CALCULATOR")
        print("="*60)
        print("\nBASIC OPERATIONS:")
        print("1. Addition (+)        2. Subtraction (-)      3. Multiplication (*)")
        print("4. Division (/)        5. Power (^)            6. Square Root (√)")
        print("7. Nth Root           8. Absolute Value       9. Factorial (!)")
        print("\nTRIGONOMETRIC FUNCTIONS:")
        print("10. Sine              11. Cosine              12. Tangent")
        print("13. Arc Sine          14. Arc Cosine          15. Arc Tangent")
        print("16. Hyperbolic Sine   17. Hyperbolic Cosine   18. Hyperbolic Tangent")
        print("\nLOGARITHMIC FUNCTIONS:")
        print("19. Natural Log (ln)  20. Log Base 10         21. Log Base 2")
        print("22. Log Base N        23. Exponential (e^x)")
        print("\nADVANCED OPERATIONS:")
        print("24. Combination (nCr) 25. Permutation (nPr)   26. Floor")
        print("27. Ceiling           28. Round")
        print("\nCONSTANTS:")
        print("29. Pi (π)            30. Euler's Number (e)  31. Tau (τ)")
        print("\nMEMORY OPERATIONS:")
        print("32. Store Memory      33. Recall Memory       34. Clear Memory")
        print("35. Add to Memory     36. Subtract from Memory")
        print("\nSETTINGS & UTILITIES:")
        print("37. Change Angle Mode 38. Set Precision       39. View History")
        print("40. Clear History     41. Help                42. Exit")
        print("\n" + "="*60)

    def get_number_input(self, prompt: str) -> float:
        """Get number input from user with validation."""
        while True:
            try:
                value = input(prompt)
                if value.lower() == 'q':
                    return None
                return float(value)
            except ValueError:
                print("❌ Invalid input. Please enter a valid number or 'q' to quit.")

    def get_integer_input(self, prompt: str) -> int:
        """Get integer input from user with validation."""
        while True:
            try:
                value = input(prompt)
                if value.lower() == 'q':
                    return None
                return int(value)
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer or 'q' to quit.")

    def add_to_history(self, operation: str, result: str):
        """Add operation to history."""
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 50:  # Keep last 50 operations
            self.history.pop(0)

    def run_calculator(self):
        """Main calculator loop."""
        print("🔬 Welcome to Python Scientific Calculator!")
        print("💡 Tip: Enter 'q' at any number prompt to return to main menu.")

        while True:
            try:
                self.display_menu()
                print(f"\n📐 Current Settings: Angle Mode = {self.calc.angle_mode.title()}, Precision = {self.calc.precision}")
                print(f"💾 Memory: {self.calc.memory}")

                choice = input("\n➤ Enter your choice (1-42): ").strip()

                if choice == '42':
                    print("\n🙏 Thank you for using Python Scientific Calculator!")
                    break

                self.handle_operation(choice)

            except KeyboardInterrupt:
                print("\n\n🛑 Calculator interrupted by user.")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")

    def handle_operation(self, choice: str):
        """Handle the selected operation."""
        try:
            # Basic Operations
            if choice == '1':  # Addition
                a = self.get_number_input("Enter first number: ")
                if a is None: return
                b = self.get_number_input("Enter second number: ")
                if b is None: return
                result = self.calc.add(a, b)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: {a} + {b} = {formatted_result}")
                self.add_to_history(f"{a} + {b}", formatted_result)

            elif choice == '2':  # Subtraction
                a = self.get_number_input("Enter first number: ")
                if a is None: return
                b = self.get_number_input("Enter second number: ")
                if b is None: return
                result = self.calc.subtract(a, b)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: {a} - {b} = {formatted_result}")
                self.add_to_history(f"{a} - {b}", formatted_result)

            elif choice == '3':  # Multiplication
                a = self.get_number_input("Enter first number: ")
                if a is None: return
                b = self.get_number_input("Enter second number: ")
                if b is None: return
                result = self.calc.multiply(a, b)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: {a} × {b} = {formatted_result}")
                self.add_to_history(f"{a} × {b}", formatted_result)

            elif choice == '4':  # Division
                a = self.get_number_input("Enter dividend: ")
                if a is None: return
                b = self.get_number_input("Enter divisor: ")
                if b is None: return
                result = self.calc.divide(a, b)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: {a} ÷ {b} = {formatted_result}")
                self.add_to_history(f"{a} ÷ {b}", formatted_result)

            elif choice == '5':  # Power
                base = self.get_number_input("Enter base: ")
                if base is None: return
                exp = self.get_number_input("Enter exponent: ")
                if exp is None: return
                result = self.calc.power(base, exp)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: {base}^{exp} = {formatted_result}")
                self.add_to_history(f"{base}^{exp}", formatted_result)

            elif choice == '6':  # Square Root
                x = self.get_number_input("Enter number: ")
                if x is None: return
                result = self.calc.square_root(x)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: √{x} = {formatted_result}")
                self.add_to_history(f"√{x}", formatted_result)

            elif choice == '10':  # Sine
                x = self.get_number_input(f"Enter angle in {self.calc.angle_mode}: ")
                if x is None: return
                result = self.calc.sine(x)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: sin({x}) = {formatted_result}")
                self.add_to_history(f"sin({x})", formatted_result)

            elif choice == '19':  # Natural Log
                x = self.get_number_input("Enter number: ")
                if x is None: return
                result = self.calc.natural_log(x)
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ Result: ln({x}) = {formatted_result}")
                self.add_to_history(f"ln({x})", formatted_result)

            elif choice == '29':  # Pi
                result = self.calc.get_pi()
                formatted_result = self.calc.format_result(result)
                print(f"\n✅ π = {formatted_result}")
                self.add_to_history("π", formatted_result)

            elif choice == '39':  # View History
                self.show_history()

            elif choice == '37':  # Change Angle Mode
                current_mode = self.calc.angle_mode
                new_mode = "radians" if current_mode == "degrees" else "degrees"
                self.calc.set_angle_mode(new_mode)
                print(f"\n✅ Angle mode changed to: {new_mode.title()}")

            elif choice == '41':  # Help
                self.show_help()

            else:
                print("\n❌ Invalid choice. Please select a number between 1-42.")

        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

    def show_history(self):
        """Display calculation history."""
        if not self.history:
            print("\n📝 No calculations in history.")
        else:
            print("\n📝 CALCULATION HISTORY:")
            print("-" * 40)
            for i, calc in enumerate(self.history[-10:], 1):  # Show last 10
                print(f"{i:2d}. {calc}")

    def show_help(self):
        """Display help information."""
        print("\n" + "="*60)
        print("                         HELP GUIDE")
        print("="*60)
        print("\n🔢 BASIC OPERATIONS:")
        print("   • Use standard arithmetic operations")
        print("   • Division by zero will show an error")
        print("   • Results are formatted based on precision setting")
        print("\n📐 TRIGONOMETRIC FUNCTIONS:")
        print("   • Angle mode affects sin, cos, tan and their inverses")
        print("   • Switch between degrees and radians as needed")
        print("   • Hyperbolic functions always work with real numbers")
        print("\n📊 LOGARITHMIC FUNCTIONS:")
        print("   • All log functions require positive inputs")
        print("   • ln = natural logarithm (base e)")
        print("   • Log base N allows custom base logarithms")
        print("\n💾 MEMORY OPERATIONS:")
        print("   • Store: Save current result to memory")
        print("   • Recall: Get value from memory")
        print("   • Add/Subtract: Modify memory value")
        print("\n⚙️  SETTINGS:")
        print("   • Precision: Decimal places (0-15)")
        print("   • Angle Mode: Degrees or Radians")
        print("   • History: Last 50 calculations saved")
        print("\n❓ TIPS:")
        print("   • Enter 'q' at number prompts to return to menu")
        print("   • Use Ctrl+C to exit calculator")  
        print("   • Check current settings display before operations")


def main():
    """Main function to run the calculator."""
    calculator_interface = CalculatorInterface()
    calculator_interface.run_calculator()


if __name__ == "__main__":
    main()
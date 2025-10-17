#!/usr/bin/env python3
"""
test_calculator_core.py - Unit tests for calculator core functions
"""

import unittest
import math
import sys
import os

# Add the parent directory to the path to import calculator modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from calculator_core import MathematicalFunctions, CalculatorMemory, ExpressionEvaluator
except ImportError:
    print("Warning: calculator_core module not found. Make sure it's in the same directory.")
    sys.exit(1)


class TestMathematicalFunctions(unittest.TestCase):
    """Test cases for MathematicalFunctions class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = MathematicalFunctions()
        self.precision = 6  # Number of decimal places for float comparisons

    def assertAlmostEqualFloat(self, first, second, msg=None):
        """Helper method for float comparisons with custom precision."""
        self.assertAlmostEqual(first, second, places=self.precision, msg=msg)

    def test_basic_operations(self):
        """Test basic arithmetic operations."""
        # Addition
        self.assertEqual(self.calc.basic_operations(5, 3, '+'), 8)
        self.assertEqual(self.calc.basic_operations(-2, 7, '+'), 5)
        self.assertAlmostEqualFloat(self.calc.basic_operations(2.5, 3.7, '+'), 6.2)

        # Subtraction
        self.assertEqual(self.calc.basic_operations(10, 4, '-'), 6)
        self.assertEqual(self.calc.basic_operations(3, 8, '-'), -5)

        # Multiplication
        self.assertEqual(self.calc.basic_operations(6, 7, '*'), 42)
        self.assertEqual(self.calc.basic_operations(-3, 4, '*'), -12)
        self.assertEqual(self.calc.basic_operations(0, 100, '*'), 0)

        # Division
        self.assertEqual(self.calc.basic_operations(15, 3, '/'), 5)
        self.assertAlmostEqualFloat(self.calc.basic_operations(10, 3, '/'), 3.333333)

        # Division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.basic_operations(10, 0, '/')

        # Power
        self.assertEqual(self.calc.basic_operations(2, 3, '**'), 8)
        self.assertEqual(self.calc.basic_operations(5, 0, '**'), 1)

        # Modulo
        self.assertEqual(self.calc.basic_operations(10, 3, '%'), 1)

        # Floor division
        self.assertEqual(self.calc.basic_operations(10, 3, '//'), 3)

        # Invalid operation
        with self.assertRaises(ValueError):
            self.calc.basic_operations(5, 3, 'invalid')

    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test in degrees
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(30, 'sin', 'degrees'), 0.5
        )
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(60, 'cos', 'degrees'), 0.5
        )
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(45, 'tan', 'degrees'), 1.0
        )

        # Test in radians
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(math.pi/6, 'sin', 'radians'), 0.5
        )
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(math.pi/3, 'cos', 'radians'), 0.5
        )

        # Test inverse functions
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(0.5, 'asin', 'degrees'), 30.0
        )
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(0.5, 'acos', 'degrees'), 60.0
        )

        # Test invalid inputs for inverse functions
        with self.assertRaises(ValueError):
            self.calc.trigonometric_functions(2, 'asin', 'degrees')

        with self.assertRaises(ValueError):
            self.calc.trigonometric_functions(2, 'acos', 'degrees')

        # Test hyperbolic functions
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(0, 'sinh', 'degrees'), 0.0
        )
        self.assertAlmostEqualFloat(
            self.calc.trigonometric_functions(0, 'cosh', 'degrees'), 1.0
        )

        # Test invalid function
        with self.assertRaises(ValueError):
            self.calc.trigonometric_functions(30, 'invalid', 'degrees')

    def test_logarithmic_functions(self):
        """Test logarithmic and exponential functions."""
        # Natural logarithm
        self.assertAlmostEqualFloat(
            self.calc.logarithmic_functions(math.e, 'ln'), 1.0
        )

        # Base 10 logarithm
        self.assertAlmostEqualFloat(
            self.calc.logarithmic_functions(100, 'log'), 2.0
        )

        # Base 2 logarithm
        self.assertAlmostEqualFloat(
            self.calc.logarithmic_functions(8, 'log2'), 3.0
        )

        # Custom base logarithm
        self.assertAlmostEqualFloat(
            self.calc.logarithmic_functions(8, 'log_base', 2), 3.0
        )

        # Exponential
        self.assertAlmostEqualFloat(
            self.calc.logarithmic_functions(0, 'exp'), 1.0
        )

        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.logarithmic_functions(-1, 'ln')

        with self.assertRaises(ValueError):
            self.calc.logarithmic_functions(10, 'log_base', 1)  # Invalid base

        # Test invalid function
        with self.assertRaises(ValueError):
            self.calc.logarithmic_functions(10, 'invalid')

    def test_power_and_root_functions(self):
        """Test power and root functions."""
        # Square root
        self.assertAlmostEqualFloat(
            self.calc.power_and_root_functions(16, 'sqrt'), 4.0
        )

        # Cube root
        self.assertAlmostEqualFloat(
            self.calc.power_and_root_functions(27, 'cbrt'), 3.0
        )

        # Nth root
        self.assertAlmostEqualFloat(
            self.calc.power_and_root_functions(32, 'nth_root', 5), 2.0
        )

        # Square
        self.assertEqual(self.calc.power_and_root_functions(5, 'square'), 25)

        # Cube
        self.assertEqual(self.calc.power_and_root_functions(3, 'cube'), 27)

        # Power
        self.assertEqual(self.calc.power_and_root_functions(2, 'power', 10), 1024)

        # Reciprocal
        self.assertAlmostEqualFloat(
            self.calc.power_and_root_functions(4, 'reciprocal'), 0.25
        )

        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.power_and_root_functions(-1, 'sqrt')

        with self.assertRaises(ZeroDivisionError):
            self.calc.power_and_root_functions(0, 'reciprocal')

        with self.assertRaises(ValueError):
            self.calc.power_and_root_functions(8, 'nth_root', 0)

    def test_combinatorics_functions(self):
        """Test combinatorial functions."""
        # Factorial
        self.assertEqual(self.calc.combinatorics_functions(5, 0, 'factorial'), 120)
        self.assertEqual(self.calc.combinatorics_functions(0, 0, 'factorial'), 1)

        # Combination
        self.assertEqual(self.calc.combinatorics_functions(5, 2, 'combination'), 10)
        self.assertEqual(self.calc.combinatorics_functions(10, 3, 'combination'), 120)

        # Permutation
        self.assertEqual(self.calc.combinatorics_functions(5, 2, 'permutation'), 20)
        self.assertEqual(self.calc.combinatorics_functions(10, 3, 'permutation'), 720)

        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.combinatorics_functions(-1, 2, 'factorial')

        with self.assertRaises(ValueError):
            self.calc.combinatorics_functions(200, 0, 'factorial')  # Too large

    def test_statistical_functions(self):
        """Test statistical functions."""
        test_data = [1, 2, 3, 4, 5]

        # Mean
        self.assertEqual(self.calc.statistical_functions(test_data, 'mean'), 3.0)

        # Median
        self.assertEqual(self.calc.statistical_functions(test_data, 'median'), 3.0)
        self.assertEqual(self.calc.statistical_functions([1, 2, 3, 4], 'median'), 2.5)

        # Sum
        self.assertEqual(self.calc.statistical_functions(test_data, 'sum'), 15)

        # Min and Max
        self.assertEqual(self.calc.statistical_functions(test_data, 'min'), 1)
        self.assertEqual(self.calc.statistical_functions(test_data, 'max'), 5)

        # Range
        self.assertEqual(self.calc.statistical_functions(test_data, 'range'), 4)

        # Standard deviation (approximately)
        std_dev = self.calc.statistical_functions(test_data, 'std_dev')
        self.assertAlmostEqualFloat(std_dev, 1.581139, places=5)

        # Test empty list
        with self.assertRaises(ValueError):
            self.calc.statistical_functions([], 'mean')

    def test_constants(self):
        """Test mathematical constants."""
        constants = self.calc.constants()

        # Check that constants exist and have reasonable values
        self.assertAlmostEqualFloat(constants['pi'], math.pi)
        self.assertAlmostEqualFloat(constants['e'], math.e)
        self.assertAlmostEqualFloat(constants['tau'], 2 * math.pi)
        self.assertAlmostEqualFloat(constants['golden_ratio'], 1.618034, places=5)
        self.assertAlmostEqualFloat(constants['sqrt2'], math.sqrt(2))

        # Check physical constants are positive
        self.assertGreater(constants['speed_of_light'], 0)
        self.assertGreater(constants['planck_constant'], 0)
        self.assertGreater(constants['avogadro_number'], 0)


class TestCalculatorMemory(unittest.TestCase):
    """Test cases for CalculatorMemory class."""

    def setUp(self):
        """Set up test fixtures."""
        self.memory = CalculatorMemory()

    def test_basic_memory_operations(self):
        """Test basic memory operations."""
        # Initial memory should be 0
        self.assertEqual(self.memory.recall(), 0.0)

        # Store and recall
        self.memory.store(42.5)
        self.assertEqual(self.memory.recall(), 42.5)

        # Add to memory
        self.memory.add(7.5)
        self.assertEqual(self.memory.recall(), 50.0)

        # Subtract from memory
        self.memory.subtract(10.0)
        self.assertEqual(self.memory.recall(), 40.0)

        # Multiply memory
        self.memory.multiply(2.0)
        self.assertEqual(self.memory.recall(), 80.0)

        # Divide memory
        self.memory.divide(4.0)
        self.assertEqual(self.memory.recall(), 20.0)

        # Clear memory
        self.memory.clear()
        self.assertEqual(self.memory.recall(), 0.0)

    def test_memory_division_by_zero(self):
        """Test memory division by zero."""
        self.memory.store(10.0)
        with self.assertRaises(ZeroDivisionError):
            self.memory.divide(0.0)

    def test_history_operations(self):
        """Test history management."""
        # Initially empty
        self.assertEqual(len(self.memory.get_history()), 0)

        # Add some history
        self.memory.add_to_history("2 + 3", "5")
        self.memory.add_to_history("10 * 2", "20")

        history = self.memory.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("2 + 3 = 5", history)
        self.assertIn("10 * 2 = 20", history)

        # Clear history
        self.memory.clear_history()
        self.assertEqual(len(self.memory.get_history()), 0)

    def test_variable_operations(self):
        """Test variable storage and recall."""
        # Store variables
        self.memory.store_variable("x", 10.5)
        self.memory.store_variable("y", 20.0)

        # Recall variables
        self.assertEqual(self.memory.recall_variable("x"), 10.5)
        self.assertEqual(self.memory.recall_variable("y"), 20.0)

        # List variables
        variables = self.memory.list_variables()
        self.assertEqual(len(variables), 2)
        self.assertEqual(variables["x"], 10.5)
        self.assertEqual(variables["y"], 20.0)

        # Recall non-existent variable
        with self.assertRaises(KeyError):
            self.memory.recall_variable("z")

        # Clear variables
        self.memory.clear_variables()
        self.assertEqual(len(self.memory.list_variables()), 0)


class TestExpressionEvaluator(unittest.TestCase):
    """Test cases for ExpressionEvaluator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.evaluator = ExpressionEvaluator()

    def test_basic_expressions(self):
        """Test basic mathematical expressions."""
        # Simple arithmetic
        self.assertEqual(self.evaluator.evaluate_expression("2 + 3"), 5.0)
        self.assertEqual(self.evaluator.evaluate_expression("10 - 4"), 6.0)
        self.assertEqual(self.evaluator.evaluate_expression("6 * 7"), 42.0)
        self.assertEqual(self.evaluator.evaluate_expression("15 / 3"), 5.0)

        # Order of operations
        self.assertEqual(self.evaluator.evaluate_expression("2 + 3 * 4"), 14.0)
        self.assertEqual(self.evaluator.evaluate_expression("(2 + 3) * 4"), 20.0)

        # Power operations
        self.assertEqual(self.evaluator.evaluate_expression("2**3"), 8.0)
        self.assertEqual(self.evaluator.evaluate_expression("2^3"), 8.0)  # Should convert ^ to **

    def test_function_expressions(self):
        """Test expressions with mathematical functions."""
        # Trigonometric functions in degrees
        result = self.evaluator.evaluate_expression("sin(30)", "degrees")
        self.assertAlmostEqual(result, 0.5, places=6)

        # Logarithmic functions
        result = self.evaluator.evaluate_expression("log(100)")
        self.assertAlmostEqual(result, 2.0, places=6)

        # Square root
        result = self.evaluator.evaluate_expression("sqrt(16)")
        self.assertEqual(result, 4.0)

        # Constants
        result = self.evaluator.evaluate_expression("pi")
        self.assertAlmostEqual(result, math.pi, places=6)

    def test_complex_expressions(self):
        """Test complex mathematical expressions."""
        # Multiple operations
        result = self.evaluator.evaluate_expression("sqrt(16) + log(100) * sin(30)", "degrees")
        expected = 4.0 + 2.0 * 0.5  # 4 + 2 * 0.5 = 5
        self.assertAlmostEqual(result, expected, places=6)

        # Nested functions
        result = self.evaluator.evaluate_expression("sqrt(log(100)**2)")
        self.assertAlmostEqual(result, 2.0, places=6)

    def test_invalid_expressions(self):
        """Test handling of invalid expressions."""
        # Division by zero
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_expression("5 / 0")

        # Invalid function
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_expression("invalid_function(5)")

        # Syntax error
        with self.assertRaises(ValueError):  
            self.evaluator.evaluate_expression("2 + + 3")

    def test_symbol_replacement(self):
        """Test replacement of mathematical symbols."""
        # Test that symbols are properly replaced
        self.assertEqual(self.evaluator.evaluate_expression("6 × 7"), 42.0)
        self.assertEqual(self.evaluator.evaluate_expression("15 ÷ 3"), 5.0)
        self.assertEqual(self.evaluator.evaluate_expression("10 − 4"), 6.0)


def run_tests():
    """Run all tests and provide a summary."""
    # Create test suite
    test_suite = unittest.TestSuite()

    # Add test classes
    test_classes = [
        TestMathematicalFunctions,
        TestCalculatorMemory,
        TestExpressionEvaluator
    ]

    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")

    if result.failures:
        print("\nFAILURES:")
        for test, trace in result.failures:
            print(f"- {test}: {trace.split('AssertionError:')[-1].strip()}")

    if result.errors:
        print("\nERRORS:")
        for test, trace in result.errors:
            print(f"- {test}: {trace.split('Exception:')[-1].strip()}")

    if not result.failures and not result.errors:
        print("\n🎉 All tests passed successfully!")

    return result.wasSuccessful()


if __name__ == "__main__":
    # Run tests when script is executed directly
    success = run_tests()
    sys.exit(0 if success else 1)
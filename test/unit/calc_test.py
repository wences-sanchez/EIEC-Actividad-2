import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    """
    TEST POSITIVOS
    """

    # Testear que la resta calcula bien según sus parámetros
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertEqual(5, self.calc.substract(10, 5))
        self.assertEqual(-5, self.calc.substract(5, 10))
        self.assertEqual(15, self.calc.substract(10, -5))
        self.assertEqual(-30, self.calc.substract(-20, 10))
        self.assertEqual(0, self.calc.substract(-10, -10))

    # Testear que la división calcula bien según sus parámetros
    def test_divide_method_returns_other_correct_result(self):
        self.assertEqual(1, self.calc.divide(5, 5))
        self.assertEqual(0.5, self.calc.divide(5, 10))
        self.assertEqual(1.5, self.calc.divide(7.5, 5))

    # Testear que la multiplicación calcula bien según sus parámetros
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_other_correct_result(self, _validate_permissions):
        self.assertEqual(0, self.calc.multiply(4, 0))
        self.assertEqual(0, self.calc.multiply(0, 4))
        self.assertEqual(80, self.calc.multiply(20, 4))
        self.assertEqual(-50, self.calc.multiply(-5, 10))
        self.assertEqual(-1000, self.calc.multiply(10, -100))
        self.assertEqual(25, self.calc.multiply(-5, -5))

    # Testear que la potencia calcula bien según sus parámetros
    def test_power_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.power(500, 0))
        self.assertEqual(20, self.calc.power(20, 1))
        self.assertEqual(16, self.calc.power(2, 4))
        self.assertEqual(100, self.calc.power(10, 2))
        self.assertEqual(1024, self.calc.power(2, 10))

    # Testear que la raíz calcula bien según su parámetro
    def test_squared_root_returns_correct_result(self):
        self.assertEqual(4, self.calc.squared_root(16))
        self.assertEqual(1, self.calc.squared_root(1))

    # Testear que el logaritmo de base 10 calcula bien según su parámetro
    def test_log_10_returns_correct_result(self):
        self.assertEqual(2, self.calc.log_10(100))
        self.assertEqual(0, self.calc.log_10(1))
        self.assertEqual(1, self.calc.log_10(10))

    """
    TESTS NEGATIVOS (comprobamos que lanza excepción)
    """

    # Testear que la resta lanza excepción en caso de error en sus parámetros
    # Testear que la división lanza excepción en caso de error en sus parámetros
    # Testear que la multiplicación lanza excepción en caso de error en sus parámetros
    # Testear que la potencia lanza excepción en caso de error en su parámetro
    # Testear que la potencia lanza excepción en caso de error en sus parámetros
    # Testear que la raíz lanza excepción en caso de error en su parámetro
    # Testear que el logaritmo de base 10 lanza excepción en caso de error en su parámetro



if __name__ == "__main__":  # pragma: no cover
    unittest.main()

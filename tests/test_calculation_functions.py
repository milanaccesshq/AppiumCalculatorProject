from unittest import TestCase


class NinePlusTen(TestCase):
    def test_nine_plus_ten(self):
        from functions.calculator_functions import calculation
        self.assertEqual(calculation("12", "4", "add"), "16")
        self.assertEqual(calculation("12", "4", "sub"), "8")
        self.assertEqual(calculation("12", "4", "mul"), "48")
        self.assertEqual(calculation("12", "4", "div"), "3")

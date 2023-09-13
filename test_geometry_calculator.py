import unittest
from main import GeometryCalculator

class TestGeometryCalculator(unittest.TestCase):
    def test_circle_area(self):
        calculator = GeometryCalculator()
        # Проверяем площадь круга для положительного радиуса
        self.assertAlmostEqual(calculator.circle_area(5), 78.54, places=2)

        # Проверяем обработку отрицательного радиуса
        with self.assertRaises(ValueError):
            calculator.circle_area(-1)

    def test_triangle_area(self):
        calculator = GeometryCalculator()
        # Проверяем площадь треугольника для положительных сторон
        self.assertAlmostEqual(calculator.triangle_area(3, 4, 5), 6.0, places=2)

        # Проверяем обработку отрицательных сторон
        with self.assertRaises(ValueError):
            calculator.triangle_area(-1, 2, 3)

    def test_is_right_triangle(self):
        calculator = GeometryCalculator()
        # Проверяем, что треугольник 3-4-5 - прямоугольный
        self.assertTrue(calculator.is_right_triangle(3, 4, 5))

        # Проверяем, что треугольник 5-12-13 - прямоугольный
        self.assertTrue(calculator.is_right_triangle(5, 12, 13))

        # Проверяем, что треугольник 1-2-3 - не прямоугольный
        self.assertFalse(calculator.is_right_triangle(1, 2, 3))

if __name__ == "__main__":
    unittest.main()
import math

class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        """Вычисляет площадь круга по радиусу."""
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(a, b, c):
        """Вычисляет площадь треугольника по трем сторонам."""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными числами")

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    @staticmethod
    def is_right_triangle(a, b, c):
        """Проверяет, является ли треугольник прямоугольным по трем сторонам."""
        sides = [a, b, c]
        sides.sort()

        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6

if __name__ == "__main__":
    calculator = GeometryCalculator()

    radius = float(input())
    circle_area = calculator.circle_area(radius)
    print(f"Площадь круга с радиусом {radius} равна {circle_area:.2f}")

    a = float(input())
    b = float(input())
    c = float(input())
    triangle_area = calculator.triangle_area(a, b, c)
    is_right_triangle = calculator.is_right_triangle(a, b, c)
    print(f"Площадь треугольника с сторонами {a}, {b}, {c} равна {triangle_area:.2f}")
    if is_right_triangle:
        print("Треугольник является прямоугольным.")
    else:
        print("Треугольник не является прямоугольным.")


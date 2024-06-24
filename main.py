# Задание «Площадь и периметр квадрата»
def area_and_perimeter_of_square(a):
    perimeter = 4*a
    area = a**2
    return area, perimeter


# Задание «Площадь и периметр прямоугольника»
def area_and_perimeter_of_rectangle(a, b):
    perimeter = 2*(a+b)
    area = a*b
    return area, perimeter


# Задание «Квадратное уравнение»
def quadratic_equation(a, b, c):
    d = b**2-4*a*c
    if d < 0:
        return 'корней нет'
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        if d == 0:
            return x1
        x2 = (-b + d ** 0.5) / (2 * a)
        return x1, x2

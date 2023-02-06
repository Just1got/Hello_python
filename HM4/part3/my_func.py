"""Compouting Mandelbrot sets."""
import math


def drawing_my_func(size_y, size_x):
    """Создает монохромную матрицу для картинки.

    Параметры:
        size_x: Высота bmp картинки в пикселях
        size_y: ширина bmp картинки в пикселях

    Return:
        Список списков int в диапазоне 0-255 (0 - черный, 255 - белый).
    """
    data_matrix = [[0] * size_y for i in range(size_x)]
    minimum_size = min(size_y, size_x) - 1
    k = 10000   # коэффициент периода от 0 до 2*pi
    for i in range(int(2*math.pi * k)):
        data_matrix[int(int(minimum_size/2)*math.pow(math.sin(i/k), 3)) + int(size_x / 2)][int(int(minimum_size / 2) * math.pow(math.cos(i / k), 3)) + int(size_y / 2)] = 255
    return data_matrix

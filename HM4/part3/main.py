import bmp
import my_func
import sys


def main(width=1200, height=1200, name='draw.bmp'):
    """Создает bmp-рисунок функции x = 2*(sin(t))^3, y = 2*(cos(t))^3 при t [0, 2*pi]
    Параметры:
        width: Ширина bmp картинки в пикселях
        height: Высота bmp картинки в пикселях
    """
    pixels = my_func.drawing_my_func(width, height)
    bmp.write_grayscale(name, pixels)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
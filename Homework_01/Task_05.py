# Программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def is_int(str_):
    try:
        int(str_)
        return True
    except ValueError:
        return False

coordinate_x1 = input (f'Введите координату первой точки X: ')
if is_int(coordinate_x1):
    coordinate_x1 = int(coordinate_x1)
else:
    while not is_int(coordinate_x1) and coordinate_x1 != 'exit':
        coordinate_x1 = input (f'Введите координату первой точки X: ')

coordinate_y1 = input (f'Введите координату первой точки Y: ')
if is_int(coordinate_y1):
    coordinate_y1 = int(coordinate_y1)
else:
    while not is_int(coordinate_y1) and coordinate_y1 != 'exit':
        coordinate_y1 = input (f'Введите координату первой точки Y: ')

coordinate_x2 = input (f'Введите координату второй точки X: ')
if is_int(coordinate_x2):
    coordinate_x2 = int(coordinate_x2)
else:
    while not is_int(coordinate_x2) and coordinate_x2 != 'exit':
        coordinate_x2 = input (f'Введите координату второй точки X: ')

coordinate_y2 = input (f'Введите координату второй точки Y: ')
if is_int(coordinate_y2):
    coordinate_y2 = int(coordinate_y2)
else:
    while not is_int(coordinate_y2) and coordinate_y2 != 'exit':
        coordinate_y2 = input (f'Введите координату второй точки Y: ')

length = ((coordinate_x2 - coordinate_x1)**2 + (coordinate_y2 - coordinate_y1)**2)**0.5
print(f'A({coordinate_x1},{coordinate_y1}); B({coordinate_x2},{coordinate_y2}) -> {round(length,2)}')

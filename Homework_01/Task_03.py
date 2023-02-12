# Программа принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

coordinate_x = input (f'Введите координату точки Х: ')
while coordinate_x == '0' and coordinate_x != 'exit':
    coordinate_x = input (f'Введите координату точки Х: ')
if is_int(coordinate_x):
    coordinate_x = int(coordinate_x)

coordinate_y = input (f'Введите координату точки Y: ')
while coordinate_y == '0' and coordinate_y != 'exit':
    coordinate_y = input (f'Введите координату точки Y: ')
if is_int(coordinate_y):
    coordinate_y = int(coordinate_y)

if coordinate_x > 0 and coordinate_y > 0:
    print(f'х={coordinate_x}; y={coordinate_y} -> 1')
elif coordinate_x < 0 and coordinate_y > 0:
    print(f'х={coordinate_x}; y={coordinate_y} -> 2')
elif coordinate_x < 0 and coordinate_y < 0:
    print(f'х={coordinate_x}; y={coordinate_y} -> 3')
elif coordinate_x > 0 and coordinate_y < 0:
    print(f'х={coordinate_x}; y={coordinate_y} -> 4')

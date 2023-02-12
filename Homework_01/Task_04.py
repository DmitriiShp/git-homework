# Программа по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

num_quarter = input('Введите номер четверти: ')
while num_quarter not in ('1', '2', '3', '4') and num_quarter != 'exit': 
    num_quarter = input('Введите номер четверти: ')
if num_quarter.isdigit():
    num_quarter = int(num_quarter)

if num_quarter == 1:
    print(f'Четверть {num_quarter}: X > 0 и Y > 0')
elif num_quarter == 2:
    print(f'Четверть {num_quarter}: X < 0 и Y > 0')
elif num_quarter == 3:
    print(f'Четверть {num_quarter}: X < 0 и Y < 0')
elif num_quarter == 4:
    print(f'Четверть {num_quarter}: X > 0 и Y < 0')
    
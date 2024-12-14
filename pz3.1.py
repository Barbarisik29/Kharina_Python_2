#Вариант 27.
#1. Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
#лежит во второй или третьей координатной четверти».

while True:
    try:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        break
    except ValueError:
        print("Неправильно ввели!")
# Проверка, находится ли точка во второй или третьей четверти
if (x < 0 and y > 0) or (x < 0 and y < 0):
    print(f"Точка с координатами ({x}, {y}) лежит во второй или третьей координатной четверти.")
else:
    print(f"Точка с координатами ({x}, {y}) не лежит во второй или третьей координатной четверти.")

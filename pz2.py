#Вводим количество секунд, прошедших с начала суток
N = input( "Введите количество секунд, прошедших с начала суток: ")

while type(N) != int:  #обработка ошибок
    try:
        N = int(N)
    except:
        print('Неправильно ввели!')
        N = input("Введите количество секунд прошедших с начала суток: ")

#Находим количество секунд, прошедших с начала последней минуты
a: int = 60
b = N % a

#Выводим результат
print(f"Количество секунд, прошедших с начала последней минуты: {b}")
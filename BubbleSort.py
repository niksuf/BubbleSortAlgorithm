from random import random, seed
from time import time

def isSorted(array, size):                  # Проверка на упорядоченность
    for i in range (0, size - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def printArray(array, size):                # Вывод массива
    if isSorted(array, size):
        print('Sorted!')
    else:
        print('Unsorted!')
    for i in range (0, 10):
            print(array[i], end = '\n')
    print('\n')

def sort(array, size):                      # Сортировка массива
    for i in range (0, size):
        for j in range (0, size - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

seed(time())                                # Инициализация таймера
print('Input array size: ')
size = int(input())                         # Размер массива
random_array = []
for i in range (0, size):                   # Заполнение массива случайными числами
    random_array.append(random() * size)
printArray(random_array, size)

t1 = time()
sort(random_array, size)                    # Сортировка
t2 = time()
elapsed = 1000 * (t2-t1)                    # Время, затраченное на операцию, мс

printArray(random_array, size)
print('Time: ', elapsed, 'ms')

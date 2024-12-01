import time
from multiprocessing import Pool

def read_info(name):
    all_data = []  # Создаем список для хранения данных
    with open(name, 'r') as file:  # Открываем файл для чтения
        while True:
            line = file.readline()  # Считываем строку
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Убираем лишние пробелы и добавляем в список
    # Здесь можно было бы возвращать all_data, но это не требуется

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Создаем имена файлов

    # Линейный вызов
    start_time = time.time()  # Запоминаем стартовое время
    for name in filenames:
        read_info(name)  # Считываем информацию из файла
    linear_time = time.time() - start_time  # Вычисляем время выполнения
    print(f'Время выполнения (линейный): {linear_time:.6f} секунд')

    # Многопроцессный вызов
    start_time = time.time()  # Запоминаем стартовое время
    with Pool() as pool:  # Создаем пул процессов
        pool.map(read_info, filenames)  # Запускаем функцию для нескольких файлов
    multiprocessing_time = time.time() - start_time  # Вычисляем время выполнения
    print(f'Время выполнения (многопроцессный): {multiprocessing_time:.6f} секунд')
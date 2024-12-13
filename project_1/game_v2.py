"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число за наименьшее число попыток
    (используем бинарный поиск - уменьшать область поиска после каждой попытки)
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        count: Число попыток
    """
    count = 0
    number = np.random.randint(1, 101)
    min_int = 0
    max_int = 100
    while True:
        predict = round((min_int+max_int)/2)
        count += 1
        if number == predict:
            break
        elif number > predict:
            min_int = predict
        elif number < predict:
            max_int = predict
    return count  


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score
#score_game(random_predict)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

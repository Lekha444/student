import numpy as np

def game_core_v3(number, borders=(1, 101)):
    count = 0
    predict = np.random.randint(borders[0], borders[1]) # Учтен корректный вызов randint
    upper_bound = borders[1]
    lower_bound = borders[0]

    while number != predict and count < 20:
        count += 1
        # Уменьшаем интервал поиска
        if predict < number:
            lower_bound = predict
            predict = np.random.randint(lower_bound, upper_bound)
        elif predict > number:
            upper_bound = predict
            predict = np.random.randint(lower_bound, upper_bound)
    return count

def score_game(game_core):
    count_ls = []
    np.random.seed(1) # Фиксируем что ьы эксперимент был воиспроизводимым
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
import numpy as np
""" Игра угадай число.
    Компьютер сам загадывает и угадывает число
"""
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # препологаемое число
        
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def score_game(random_predict) -> int:
    """_summary_

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количесвто попыток
    """
    count_ls = [] # список для количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) #Находим среднее количкство попыток
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)

#Run
if __name__ == '__main__':
    score_game(random_predict)
    
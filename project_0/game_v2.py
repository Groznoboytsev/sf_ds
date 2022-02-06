"""Guess the number game.
The computer itself guesses and guesses the number
"""

from itertools import count
import numpy as np


def random_predict (number:int=np.random.randint(1,101)) ->int:
    """Guesses the number in the minimum number of attempts

    Args:
        number (int, optional): Intented number. Defaults to np.random.randint(1,101).

    Returns:
        int: Number of attempts
    """
    
    up_limit = 101 # upper limit of expected number
    down_limit = 0 # lower bound of expected number
    count = 1
    predict = 50
    
    while number != predict:
        count += 1
        
        if number > predict:
            down_limit = predict # overwrites the variable
            predict = int((predict + up_limit)/2) # estimated number
        
        elif number < predict:
            up_limit = predict
            predict = int((predict + down_limit)/2)
  
            
    return count

print(f'Количество попыток: {random_predict()}')

def score_game (random_predict) -> int:
    """Runs the game 1000 times, displays the average of the attempts

    Args:
        random_predict ([type]): function guesses

    Returns:
        int: average number of attempts
    """
    count_ls = [] # list to save the number of attempts
    np.random.seed(1) # fix RANDOM SEED
    random_array = np.random.randint(1,101,size=1000) # made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # find the average number of attempts
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)

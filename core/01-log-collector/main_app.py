import random
import logging
import algorithms
from datetime import datetime

log_timestamp = datetime.now().strftime("log_%H%M%S.log")

logging.basicConfig(
    filename=log_timestamp,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

rand_num = random.randint(1, 100) 
rand_arr = random.sample(range(1, 200), 3)
rand_mixed_arr = rand_arr + [random.randint(-50, -1)]

def main():
    
    print(algorithms.is_even(rand_num))
    print(algorithms.all_numbers_divisible_by_multiple(rand_arr))
    print(algorithms.find_smallest(rand_arr))
    print(algorithms.find_largest(rand_arr))
    print(algorithms.sum_of_digits(rand_num))
    print(algorithms.are_all_positive(rand_mixed_arr))
    print(algorithms.is_prime(rand_num))
    print(algorithms.get_factorial(random.randint(1, 10)))
    

if __name__ == '__main__':
    main()
    
    

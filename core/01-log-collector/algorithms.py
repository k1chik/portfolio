# algorithms.py

import time
import logging
import random

logger = logging.getLogger(__name__)

#logs when a function is called (with args), its return value, and execution time
def log_function_call(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function '{func.__name__}' called with args={args}, kwargs={kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logger.info(f"Function '{func.__name__}' returned:\n{result}")
        logger.info(f"Function '{func.__name__}' completed in {duration:.4f} seconds")
        return result
    return wrapper

@log_function_call
def is_even(n):
    logger.info(f"Checking if {n} is even")
    if n % 2 == 0:
        return f"{n} is divisible by 2, so Even"
    else:
        return f"{n} is NOT divisible by 2, so Odd"
    
@log_function_call
def all_numbers_divisible_by_multiple(numbers):
    rand_divisor=random.randint(1, 15)
    logger.info(f"Checking if {numbers} is divisible by {rand_divisor}")
    for n in numbers:
        if n % rand_divisor != 0:
            return f"{numbers} are NOT all divisible by {rand_divisor}, so they are not multiples of {rand_divisor}"
    return f"{numbers} ARE all divisible by {rand_divisor}, so they are multiples of {rand_divisor}"

@log_function_call
def find_smallest(numbers):
    logger.info(f"Finding the smallest number in {numbers}")
    return f"The smallest number in {numbers} is {min(numbers)}"

@log_function_call
def find_largest(numbers):
    logger.info(f"Finding the largest number in {numbers}")
    return f"The largest number in {numbers} is {max(numbers)}"

@log_function_call
def sum_of_digits(n):
    logger.info(f"Calculating sum of digits of {n}")
    total = sum(int(digit) for digit in str(abs(n)))
    return f"Sum of digits of {n} is {total}"

@log_function_call
def are_all_positive(numbers):
    logger.info(f"Checking if all numbers are positive in {numbers}")
    if all(n > 0 for n in numbers):
        return f"All numbers in {numbers} are positive"
    else:
        return f"Not all numbers in {numbers} are positive"
    
@log_function_call
def is_prime(n):
    logger.info(f"Checking if {n} is a prime number")
    if n <= 1:
        return f"{n} is NOT prime (must be >1)"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is divisible by {i}, so NOT prime"
    return f"{n} is a prime number"


@log_function_call
def get_factorial(n):
    logger.info(f"Calculating factorial of {n}")
    if n < 0:
        return f"Factorial of negative numbers is undefined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return f"Factorial of {n} is {result}"





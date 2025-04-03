import random

def generate_two_digit_array(size):
    return [random.randint(10, 99) for _ in range(size)]

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_array(size):
    return [i for i in range(size)]

def generate_reverse_sorted_array(size):
    return [i for i in range(size, 0, -1)]

def generate_partially_sorted_array(size, sorted_percent):
    sorted_size = int(size * sorted_percent / 100)
    sorted_part = [i for i in range(sorted_size)]
    random_part = [random.randint(0, 10000) for _ in range(size - sorted_size)]
    return sorted_part + random_part
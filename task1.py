import time
from array_generator import generate_random_array
from sorting_methods import insertion_sort, selection_sort, bubble_sort, quick_sort


def run_task1():
    sizes = [20, 500, 1000, 3000, 5000, 10000]
    sort_functions = [
        ("Прямок включение", insertion_sort),
        ("Прямой выбор", selection_sort),
        ("Прямой обмен", bubble_sort),
        ("Быстрая сортировка", quick_sort)
    ]

    for size in sizes:
        original_array = generate_random_array(size)
        print(f"\nРазмер массива: {size}")
        print(f"{'Метод':<15} {'Итерации':<10} {'Сравнения':<12} {'Обмены':<10} {'Время (мс)':<12}")

        for name, sort_func in sort_functions:
            arr_copy = original_array.copy()
            start_time = time.time()
            iterations, comparisons, swaps = sort_func(arr_copy)
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"{name:<15} {iterations:<10} {comparisons:<12} {swaps:<10} {elapsed_time:.2f}")
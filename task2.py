import time
from array_generator import (generate_sorted_array, generate_reverse_sorted_array,
                             generate_partially_sorted_array)
from sorting_methods import insertion_sort, selection_sort, bubble_sort, quick_sort


def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.replace(" ", "")

        if not user_input:
            print("Ошибка: Введена пустая строка. Пожалуйста, введите целое число.")
            continue

        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Ошибка: Число должно быть положительным. Попробуйте снова.")
        else:
            print("Ошибка: Введены недопустимые символы. Пожалуйста, введите целое число.")


def run_task2():
    size = get_positive_integer("Введите размер массива: ")

    array_types = [
        ("Отсортированный массив", generate_sorted_array(size)),
        ("Обратно отсортированный массив", generate_reverse_sorted_array(size)),
        ("25% отсортированный массив", generate_partially_sorted_array(size, 25)),
        ("50% отсортированный массив", generate_partially_sorted_array(size, 50)),
        ("75% отсортированный массив", generate_partially_sorted_array(size, 75))
    ]

    sort_functions = [
        ("Прямое включение", insertion_sort),
        ("Прямой выбор", selection_sort),
        ("Прямой обмен", bubble_sort),
        ("Быстрая сортировка", quick_sort)
    ]

    for array_type_name, array in array_types:
        print(f"\n{array_type_name}:")
        print(f"{'Метод':<15} {'Итерации':<10} {'Сравнения':<12} {'Обмены':<10} {'Время (мс)':<12}")

        for sort_name, sort_func in sort_functions:
            arr_copy = array.copy()
            start_time = time.time()
            iterations, comparisons, swaps = sort_func(arr_copy)
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"{sort_name:<15} {iterations:<10} {comparisons:<12} {swaps:<10} {elapsed_time:.2f}")
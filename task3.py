import time
from array_generator import generate_two_digit_array


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


def direct_selection_sort_by_product(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    def product_of_digits(x):
        return (x // 10) * (x % 10)

    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if product_of_digits(arr[j]) > product_of_digits(arr[max_idx]):
                max_idx = j
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            swaps += 1

    return arr.copy(), comparisons, swaps


def run_task3():
    size = get_positive_integer("Введите размер массива (целое число > 0): ")

    arr = generate_two_digit_array(size)
    print(f"\nИсходный массив: {arr}")

    start_time = time.time()
    sorted_arr, comparisons, swaps = direct_selection_sort_by_product(arr.copy())
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000

    print(f"Отсортированный массив: {sorted_arr}")
    print(f"Произведения цифр: {[(x // 10) * (x % 10) for x in sorted_arr]}")
    print(f"Количество сравнений: {comparisons}")
    print(f"Количество обменов: {swaps}")
    print(f"Время выполнения: {elapsed_time:.2f} мс")
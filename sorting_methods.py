def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        iterations += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        comparisons += 1 if j >= 0 else 0
        arr[j + 1] = key
        swaps += 1 if j + 1 != i else 0
    return iterations, comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    iterations = 0
    for i in range(len(arr)):
        min_idx = i
        iterations += 1
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1 if i != min_idx else 0
    return iterations, comparisons, swaps

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    iterations = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        iterations += 1
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return iterations, comparisons, swaps

def quick_sort(arr):
    comparisons = [0]
    swaps = [0]
    iterations = [0]

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        return i + 1

    def quick_sort_helper(low, high):
        iterations[0] += 1
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(arr) - 1)
    return iterations[0], comparisons[0], swaps[0]
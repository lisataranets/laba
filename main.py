from task1 import run_task1
from task2 import run_task2
from task3 import run_task3
def main():
    while True:
        print("\nМеню:")
        print("1. Сравнение методов сортировки")
        print("2. Исследование упорядоченности массивов")
        print("3. Сортировка двузначных чисел по произведению цифр")
        print("4. Выход")

        choice = input("Выберите задание (1-4): ")
        if choice == '1':
            run_task1()
        elif choice == '2':
            run_task2()
        elif choice == '3':
            run_task3()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1-4.")


if __name__ == "__main__":
    main()
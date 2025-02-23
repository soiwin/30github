

def quick_sort(array: list[int]) -> list[int]:
    pivot = len(array) // 2

    low = [i for i in range(len(array)) if array[i] < array[pivot]]


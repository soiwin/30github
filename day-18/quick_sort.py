

def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    pivot = len(array) // 2

    low = [el for el in array if el < array[pivot]]
    eq = [el for el in array if el == array[pivot]]
    high = [el for el in array if el > array[pivot]]

    return quick_sort(low) + eq + quick_sort(high)


print(quick_sort([1, 0, 0, -4, 6, -6, 6, 9, 0]))

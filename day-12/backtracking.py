def backtrack(path, start, nums, result):
    # Добавляем текущее подмножество в результат
    result.append(path.copy())

    for i in range(start, len(nums)):
        # Выбираем элемент nums[i] и добавляем его в текущий путь
        path.append(nums[i])
        # Рекурсивно продолжаем с элементами, следующими за текущим
        backtrack(path, i + 1, nums, result)
        # Откат (backtracking): убираем последний элемент, чтобы попробовать следующий вариант
        path.pop()


# Пример использования:
nums = [1, 2, 3]
result = []
backtrack([], 0, nums, result)
print(result)




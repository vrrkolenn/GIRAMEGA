# Задание 1: Объединение словарей
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

# Способ 1: Использование update() и копии
result1 = dict_1.copy()
result1.update(dict_2)

# Способ 2: Использование оператора |
result2 = dict_1 | dict_2

# Задание 2: Функции max_dict и sum_dict
def max_dict(*dicts):
    result = {}
    all_keys = set().union(*[d.keys() for d in dicts])
    for key in all_keys:
        values = [d.get(key, 0) for d in dicts if key in d]
        result[key] = max(values)
    return result

def sum_dict(*dicts):
    result = {}
    all_keys = set().union(*[d.keys() for d in dicts])
    for key in all_keys:
        values = [d.get(key, 0) for d in dicts if key in d]
        result[key] = sum(values)
    return result

# Тестовые словари для Задания 2
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

# Задание 3: Функция set_gen
def set_gen(numbers):
    result = set()
    count_dict = {}
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
            result.add(num)
        else:
            count_dict[num] += 1
            result.add(str(num) * count_dict[num])
    return result

# Задание 4: Функция superset
def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2) and set1 != set2:
        print(f"Объект {set1} является чистым супермножеством")
    elif set2.issuperset(set1) and set2 != set1:
        print(f"Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

# Тесты
def main():
    # Задание 1
    print("Задание 1:")
    print(result1)  # {1: 'a', 2: 'c', 4: 'd'}
    print(result2)  # {1: 'a', 2: 'c', 4: 'd'}

    # Задание 2
    print("\nЗадание 2:")
    print(max_dict(dict_1, dict_2))
    print(sum_dict(dict_1, dict_4, dict_3))
    print(max_dict(dict_1, dict_2, dict_3, dict_4))
    print(sum_dict(dict_1, dict_2, dict_3, dict_4))

    # Задание 3
    print("\nЗадание 3:")
    list_1 = [1, 1, 3, 3, 1]
    list_2 = [5, 5, 5, 5, 5, 5, 5]
    list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
    print(set_gen(list_1))
    print(set_gen(list_2))
    print(set_gen(list_3))

    # Задание 4
    print("\nЗадание 4:")
    set_1 = {1, 8, 3, 5}
    set_2 = {3, 5}
    set_3 = {5, 3, 8, 1}
    set_4 = {90, 100}
    superset(set_1, set_2)
    superset(set_1, set_3)
    superset(set_2, set_3)
    superset(set_4, set_2)

if __name__ == "__main__":
    main()
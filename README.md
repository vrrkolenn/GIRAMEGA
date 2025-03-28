# Проект: Работа с множествами и словарями в Python

Этот проект демонстрирует решение четырех заданий, связанных с обработкой словарей и множеств в Python. Каждое задание включает примеры кода, тесты и вывод результатов.

## Задание 1: Объединение словарей
Реализованы два способа объединения словарей:
1. Использование метода `update()` с копированием исходного словаря.
2. Использование оператора `|` (доступно в Python 3.9+).

Пример:

```python
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
result1 = dict_1.copy()
result1.update(dict_2)  # {1: 'a', 2: 'c', 4: 'd'}
result2 = dict_1 | dict_2  # {1: 'a', 2: 'c', 4: 'd'}
```

## Задание 2: Функции `max_dict` и `sum_dict`
Две функции для работы с несколькими словарями:
- `max_dict(*dicts)`: Возвращает словарь, где для каждого ключа выбрано максимальное значение среди всех переданных словарей.
- `sum_dict(*dicts)`: Возвращает словарь, где для каждого ключа суммируются значения из всех переданных словарей.

Пример тестовых данных:
```python
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}
```

## Задание 3: Функция `set_gen`
Функция `set_gen(numbers)` создает множество из списка чисел, где:
- Каждое уникальное число добавляется один раз.
- Если число повторяется, оно добавляется в виде строки, умноженной на количество повторений.

Пример:
```python
list_1 = [1, 1, 3, 3, 1]
print(set_gen(list_1))  # {1, '11', 3, '33'}
```

## Задание 4: Функция `superset`
Функция `superset(set1, set2)` определяет отношения между двумя множествами:
- Если множества равны, выводит "Множества равны".
- Если одно множество является строгим супермножеством другого, выводит соответствующее сообщение.
- В противном случае сообщает, что супермножества нет.

Пример:
```python
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
superset(set_1, set_2)  # "Объект {1, 8, 3, 5} является чистым супермножеством"
```

## Использование
1. Убедитесь, что у вас установлен Python (версия 3.9+ для оператора `|`).
2. Запустите скрипт:
   ```bash
   python script.py
   ```
3. Результаты всех заданий будут выведены в консоль.

## Тестирование
Функция `main()` содержит тесты для всех заданий. Вывод включает результаты объединения словарей, работы функций `max_dict` и `sum_dict`, генерации множеств и проверки супермножеств.

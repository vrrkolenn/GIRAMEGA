# 1
nested_tuple = (([1, 2], ['012', 'abc']), [4, 3])
result = nested_tuple[0][1][1][2]
print(result)

# 2
complex_tuple = (42, 3.14, 2+3j, ("строка",), (), [])
string_from_tuple = complex_tuple[3][0]
print(string_from_tuple)

# 3
matryoshka = (10, (3.14, (2+3j, ("строка", ()))))
final_string = matryoshka[1][1][1][0]
print(final_string)

# 4
numbers = (1, 2, 3, 4, 5)

print(numbers[0], numbers[2])
print(numbers[:3])

print(numbers[-5], numbers[-3])
print(numbers[:-2])

# 5
deep_tuple = ((1, 2, ('Ok!', 3)), ('tuple', 4), 5)
ok_string = deep_tuple[0][2][0]
print(ok_string)

# 6
my_tuple = (3, 's', 1, 5, 's')
print(len(my_tuple))
print(my_tuple.count('s'))
print(my_tuple.index('s'))

# 7
changeable_tuple = (['кит', 1, 3], 5)
changeable_tuple[0][0] = 'кот'
del changeable_tuple[0][1]
changeable_tuple[0][1] **= 2
print(changeable_tuple)

try:
    changeable_tuple[1] *= 2
except TypeError as e:
    print(f"Ошибка: {e}")

# 8
def tpl_sort(tpl):
    for item in tpl:
        if not isinstance(item, int):
            return tpl
    return tuple(sorted(tpl))

print(tpl_sort((3, 1, 4, 2)))
print(tpl_sort((3, 'a', 1, 2)))

# 9
def slicer(tpl, element):
    if element not in tpl:
        return ()
    first = tpl.index(element)
    if tpl.count(element) == 1:
        return tpl[first:]
    second = tpl.index(element, first + 1)
    return tpl[first:second+1]

print(slicer((1, 2, 3, 4, 5, 2, 6), 2))
print(slicer((1, 2, 3), 4))
print(slicer((1, 2, 3, 4), 3))

# 10
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

students = (
    Student("Иван", 20, 4.5, "Москва"),
    Student("Петр", 21, 3.8, "Санкт-Петербург"),
    Student("Мария", 19, 5.0, "Новосибирск"),
    Student("Анна", 22, 4.2, "Екатеринбург"),
    Student("Дмитрий", 20, 4.8, "Казань"),
    Student("Ольга", 21, 3.9, "Самара"),
    Student("Сергей", 19, 4.95, "Ростов-на-Дону")
)

def good_students(students):
    average_grade = sum(s.grade for s in students) / len(students)
    good = [s.name for s in students if s.grade >= average_grade]
    print(f"Ученики {', '.join(good)} в этом семестре хорошо учатся!")

good_students(students)
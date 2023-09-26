import math
from random import randint

def test_greeting():

    name = "Анна"
    age = 25

    output = f'Привет, {name}! Тебе {age} лет.'
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():

    a = 10
    b = 20

    perimeter = (a + b) * 2
    assert perimeter == 60

    area = a * b
    assert area == 200


def test_circle():

    r = 23

    area = math.pi * (r ** 2)
    assert area == 1661.9025137490005
    print(f'Площадь круга = {area}')

    length = math.pi * (r * 2)
    assert length == 144.51326206513048
    print(f'Длина окружности = {length}')


def test_random_list():

    l = []
    i = 1

    while i <= 10:
        l.append(randint(1, 100))
        i = i + 1
    l.sort()

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    uniq_numbers = set(l)
    l = list(uniq_numbers)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():

    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    print(d.values())

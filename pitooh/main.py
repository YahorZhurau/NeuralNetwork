import parser
from math import sqrt


def print_hi(name): {
    print(f'Hi, {name}'),
}


def kv(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a),
        x2 = (-b - sqrt(d)) / (2 * a),
        print(f'{x1} {x2}')
    else:
        print('sosi kak bы')


def calc(ar1, ar2):
    for i in range(0, 3):
        for j in range(0, 3):
            print(ar1[i][j])


calc([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
kv(int(input()), int(input()), int(input()))
print_hi('retard')

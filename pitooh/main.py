from math import sqrt
from random import randint, sample


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


def calc():
    ar1 = [[randint(0, 10) for i in range(3)] for j in range(3)]
    ar2 = [[randint(0, 10) for i in range(3)] for j in range(3)]
    ar = [[0 for i in range(3)] for j in range(3)]
    for i in range(0, 3):
        for j in range(0, 3):
            ar[i][j] = ar1[i][j] + ar2[i][j]
            print(f'{ar1[i][j]} {ar2[i][j]} {ar[i][j]}')


class Horny:
    def __init__(self, b, v):
        self.vaginas_size = v
        self.boobs_size = b

    speed = False

    def sex_index(self, penis=14):
        print(f'{self.boobs_size} {self.vaginas_size} {penis} I GOING TO VACUUM')

    @staticmethod
    def smoking():
        print(f'it`s so fucking cool Cigarettes')


# calc()
# kv(int(input()), int(input()), int(input()))
# print_hi('retard')

horny1 = Horny(2.5, 51)
horny1.sex_index()

horny2 = Horny(3, 14)
horny2.sex_index(9)
horny2.smoking()

print(Horny.speed)
Horny.smoking()


from tkinter import *

# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     print(f'{f}')
#
#
# fact(int(input()))

counter = 0
#
#
# def rec():
#     global counter
#     print(counter)
#     counter += 1
#     if counter < 10:
#         rec()
#
#
# rec()

d1 = int(input()) * 10
d2 = int(input()) * 10


def romb(d1, d2):
    root = Tk()
    root.geometry('1000x1000')
    root.resizable(width=False, height=False)
    canvas = Canvas(root, height=d1 * 2, width=d2 * 2)
    print(f'{d1} {d1 / 2} {d2} {d2 / 2}')
    canvas.create_line(d1 / 2, 0, d1, d2 / 2)
    canvas.create_line(d1, d2 / 2, d1 / 2, d2)
    canvas.create_line(d1 / 2, d2, 0, d2 / 2)
    canvas.create_line(0, d2 / 2, d1 / 2, 0)
    canvas.pack()
    root.mainloop()


if d1 % 2 != 0 | d2 % 2 != 0:
    print('Ты наебер!!!')
else:
    romb(d1, d2)

import collections


def fib_gen():
    (a, b) = (0, 1)
    while True:
        yield a
        (a, b) = (b, a + b)  # inversion des valeurs dans les tuples


fibonacci = fib_gen()
for i in range(10):
    print(next(fibonacci))

from typing import Callable
from matplotlib import pyplot as plt

def do_sum(N: int, pred: Callable[[int], int | float]):
    if isinstance(pred(1), int):
        res=0
    else:
        res=0.0

    for k in range(1, N + 1):
        # TODO: Is this right?
        try:
            v = pred(k)
        except OverflowError:
            continue

        res += v
    return res

def sum1(N: int, b: float | int):
    return do_sum(N, lambda k: 1 + b**k - b**k)

def sum2(N: int, b: float | int):
    return do_sum(N, lambda k: (1 + b**k) - b**k)

def sum3(N: int, b: float | int):
    return do_sum(N, lambda k: (1 - b**k) + b**k)

def main():
    max_val = 1000
    min_val = 1
    b_val = 5
    x_vals = list(range(min_val, max_val + 1))
    arr1 = [sum1(n, b_val) for n in x_vals]
    arr2 = [sum2(n, b_val) for n in x_vals]
    arr3 = [sum3(n, b_val) for n in x_vals]

    plt.plot(x_vals, arr1, 'r--')
    plt.plot(x_vals, arr2, 'bs')
    plt.plot(x_vals, arr3, 'g^')
    plt.show()

if __name__ == '__main__':
    main()

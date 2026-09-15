import random
from typing import Callable
from matplotlib import pyplot as plt

def values(N: int):
    return [1 / (k * (k+1)) for k in range(1, N + 1)]

def sum_most_to_least(N: int):
    vals = values(N)
    vals.sort()
    res = 0.0
    for val in vals:
        res += val
    return res

def sum_least_to_most(N: int):
    vals = values(N)
    vals.sort(reverse=True)
    res = 0.0
    for val in vals:
        res += val
    return res

def sum_shuffle(N: int):
    vals = values(N)
    random.seed(67)
    random.shuffle(vals)
    res = 0.0
    for val in vals:
        res += val
    return res

def sum_kahan(N: int):
    vals = values(N)
    sum = 0.0
    c = 0.0
    for val in vals:
        y = val - c
        t = sum + y
        c = (t - sum) - y
        sum = t
    return sum

def sum_theory(N: int):
    return N / (N+1)

def main():
    max_val = 10000
    min_val = 10
    step = 10
    x_vals = list(range(min_val, max_val + 1, step))
    theory = [sum_theory(n) for n in x_vals]
    f: Callable[[tuple[float, float]], float] = lambda t: abs(t[0] - t[1]) / abs(t[1])
    funcs=[sum_most_to_least, sum_least_to_most, sum_shuffle, sum_kahan]
    arrs=[[func(n) for n in x_vals] for func in funcs]
    errs=[list(map(f, zip(a, theory))) for a in arrs]

    plt.plot(x_vals, errs[0], color='red', marker='_')
    plt.plot(x_vals, errs[1], color='blue', marker='s')
    plt.plot(x_vals, errs[2], color='green', marker='^')
    plt.plot(x_vals, errs[3], color='orange', marker='o')
    plt.show()

if __name__ == '__main__':
    main()

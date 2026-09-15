import math
from typing import Callable
from matplotlib import pyplot as plt

def b_normal(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/(k * (k+1))
        res+=v

    return res

def b_telescoping(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/k - 1/(k+1)
        res+=v

    return res

def b_closed(N: int):
    return N / (N + 1)

def c_normal(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/(math.sqrt(k**2+1)+k)
        res+=v

    return res

def c_simplified(N: int):
    res=0.0
    for k in range(1, N+1):
        v=math.sqrt(k**2+1)-k
        res+=v

    return res

def main():
    max_val = 10000
    min_val = 10
    step = 10
    x_vals = [1] + list(range(min_val, max_val + 1, step))
    f: Callable[[tuple[float, float]], float] = lambda t: abs(t[0] - t[1]) / abs(t[1])
    theory = [b_closed(n) for n in x_vals]
    funcs=[b_normal, b_telescoping]
    arrs=[[func(n) for n in x_vals] for func in funcs]
    errs=[list(map(f, zip(a, theory))) for a in arrs]

    plt.plot(x_vals, errs[0], color='red', marker='_')
    plt.plot(x_vals, errs[1], color='blue', marker='s')
    plt.show()

if __name__ == '__main__':
    main()

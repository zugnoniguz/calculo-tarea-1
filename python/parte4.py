import math
from typing import Callable
from matplotlib import pyplot as plt


# ============================================================
# PARTE 4.1 - Representaciones de una suma
# ============================================================

""" Representaciones de b_N """

#   Forma original:
#      b_N = sum(1 / (k * (k + 1)))
def b_normal(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/(k * (k+1))
        res+=v

    return res

#   Forma telescópica:
#      b_N = sum(1/k - 1/(k + 1))
def b_telescoping(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/k - 1/(k+1)
        res+=v

    return res

#  Forma cerrada:
#      b_N = N / (N + 1)
def b_closed(N: int):
    return N / (N + 1)


""" Representaciones de c_N """

#   c_N = sum(1 / (sqrt(k^2 + 1) + k))
def c_normal(N: int):
    res=0.0
    for k in range(1, N+1):
        v=1/(math.sqrt(k**2+1)+k)
        res+=v

    return res

#   c_N = sum(sqrt(k^2 + 1) - k)
def c_simplified(N: int):
    res=0.0
    for k in range(1, N+1):
        v=math.sqrt(k**2+1)-k
        res+=v

    return res



# ============================================================
# PARTE 4.2 - Error relativo de b_N
# ============================================================

def main():

    max_val = 10000
    min_val = 10
    step = 10

    # N = 1, 10, 20, ..., 10000
    x_vals = [1] + list(range(min_val, max_val + 1, step))

    # Fórmula del error relativo:
    # E_rel = |b_num - b_exacto| / |b_exacto|
    f: Callable[[tuple[float, float]], float] = \
        lambda t: abs(t[0] - t[1]) / abs(t[1])

    # Valor teórico de b_N
    theory = [b_closed(n) for n in x_vals]

    # Dos formas de calcular b_N
    funcs = [b_normal, b_telescoping]

    # Resultados numéricos de ambas representaciones
    arrs = [[func(n) for n in x_vals] for func in funcs]

    # Error relativo de ambas representaciones
    errs = [list(map(f, zip(a, theory))) for a in arrs]

    # Gráfico del error relativo
    plt.plot(x_vals, errs[0], color='red', marker='_')
    plt.plot(x_vals, errs[1], color='blue', marker='s')
    plt.show()


    # ========================================================
    # PARTE 4.3 - Comparación de las dos representaciones
    # de c_N
    # ========================================================

    # Se calcula:
    #
    # D_N = |c_N^(1) - c_N^(2)|
    #
    # donde:
    #
    # c_N^(1) = sum(1 / (sqrt(k^2 + 1) + k))
    #
    # c_N^(2) = sum(sqrt(k^2 + 1) - k)

    # Cálculo de c_N con las dos representaciones
    c_normal_vals = [c_normal(n) for n in x_vals]
    c_simplified_vals = [c_simplified(n) for n in x_vals]

    # Diferencia absoluta entre ambas
    D = [
        abs(c1 - c2)
        for c1, c2 in zip(c_normal_vals, c_simplified_vals)
    ]

    # Se grafica D_N en función de N
    plt.plot(x_vals, D)
    plt.xlabel("N")
    plt.ylabel("D_N")
    plt.title("Diferencia entre las dos representaciones de c_N")
    plt.show()


    # ========================================================
    # PARTE 4.4 BONUS - Dos representaciones de b_N
    # ========================================================

    # Se compara:  1 - 1 / (N + 1)   y   N / (N + 1)
    # Matemáticamente son equivalentes

    def b_bonus_1(N: int):
        return 1 - 1 / (N + 1)

    def b_bonus_2(N: int):
        return N / (N + 1)

    # Cálculo de ambas representaciones
    b_bonus_1_vals = [b_bonus_1(n) for n in x_vals]
    b_bonus_2_vals = [b_bonus_2(n) for n in x_vals]

    # Cálculo de la diferencia absoluta entre ambas
    b_bonus_diff = [
        abs(b1 - b2)
        for b1, b2 in zip(b_bonus_1_vals, b_bonus_2_vals)
    ]

    # Se grafica la diferencia entre ambas representaciones
    plt.plot(x_vals, b_bonus_diff)
    plt.xlabel("N")
    plt.ylabel("Diferencia absoluta")
    plt.title("Diferencia entre las dos representaciones de b_N")
    plt.show()


    # ========================================================
    # PARTE 4.4 BONUS - Comparación de los términos de c_N
    # ========================================================

    # Se estudian individualmente los términos:
    # sqrt(k^2 + 1) - k    y    1 / (sqrt(k^2 + 1) + k)
    # y se analiza cómo cambia la diferencia entre ellos al aumentar k.

    # Valores de k que se van a analizar
    k_vals = list(range(1, 10001))

    # Se calcula cada representación del término
    c_term_1 = [
        math.sqrt(k**2 + 1) - k
        for k in k_vals
    ]

    c_term_2 = [
        1 / (math.sqrt(k**2 + 1) + k)
        for k in k_vals
    ]

    # Se calcula la diferencia absoluta entre ambas
    c_term_diff = [
        abs(t1 - t2)
        for t1, t2 in zip(c_term_1, c_term_2)
    ]

    # Se grafica la diferencia en función de k
    plt.plot(k_vals, c_term_diff)
    plt.xlabel("k")
    plt.ylabel("Diferencia absoluta")
    plt.title("Diferencia entre las representaciones de los términos de c_N")
    plt.show()



if __name__ == '__main__':
    main()

import random
from typing import Callable
from matplotlib import pyplot as plt



# ============================================================
# PARTE 3 - PROPIEDAD CONMUTATIVA
# ============================================================
#
# La suma matemática es conmutativa, por lo que el orden
# de los términos no debería afectar el resultado.
#
# Sin embargo, al trabajar con números de punto flotante,
# el orden puede producir resultados diferentes debido a
# los errores de redondeo.
#
# La sucesión utilizada es:
#
#              N
#             ___
# b_N =       \      1
#             /    -------
#             ‾‾‾  k(k+1)
#
# cuya fórmula cerrada es:
#
# b_N = N / (N + 1)
# ============================================================


# Genera los N términos de la sumatoria.
def values(N: int):
    return [1 / (k * (k+1)) for k in range(1, N + 1)]


# ------------------------------------------------------------
# Suma de mayor a menor módulo
# ------------------------------------------------------------
def sum_most_to_least(N: int):
    vals = values(N)
    vals.sort(reverse=True)
    res = 0.0
    for val in vals:
        res += val
    return res

# ------------------------------------------------------------
# Suma de menor a mayor módulo
# ------------------------------------------------------------
def sum_least_to_most(N: int):
    vals = values(N)
    vals.sort()
    res = 0.0
    for val in vals:
        res += val
    return res

# ------------------------------------------------------------
# Suma randomizada
# ------------------------------------------------------------
def sum_shuffle(N: int):
    vals = values(N)

    # Se fija la semilla para que el resultado sea reproducible.
    random.seed(67)
    random.shuffle(vals)

    res = 0.0
    for val in vals:
        res += val
    return res

# ------------------------------------------------------------
# Suma de Kahan
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# Valor teórico de b_N
# ------------------------------------------------------------
# Se utiliza la fórmula cerrada: b_N = N / (N + 1)
#
# Este valor se usa como referencia para calcular
# el error relativo de cada algoritmo.
def sum_theory(N: int):
    return N / (N+1)



def main():

    # ========================================================
    # PARTE 3.3
    # ========================================================
    #
    # Se evalúan los cuatro algoritmos para:
    # N = 10, 20, 30, ..., 10000
    #
    # y se grafica el error relativo en función de N.
    # ========================================================

    min_val = 10
    max_val = 10000
    step = 10
    x_vals = list(range(min_val, max_val + 1, step))

    # Valor teórico para cada N.
    theory = [sum_theory(n) for n in x_vals]

    # Se guardan las cuatro funciones de suma.
    funcs=[sum_most_to_least, sum_least_to_most, sum_shuffle, sum_kahan]

    # Fórmula de error relativo:
    # E_rel = |b_num - b_exacto| / |b_exacto|
    f: Callable[[tuple[float, float]], float] = \
        lambda t: abs(t[0] - t[1]) / abs(t[1])

    # Resultado numérico de cada algoritmo.
    arrs=[[func(n) for n in x_vals] for func in funcs]

    # Error relativo de cada algoritmo.
    errs=[list(map(f, zip(a, theory))) for a in arrs]


    # ------------------------------------------------------------
    # Gráfico del error relativo en función de cada algoritmo
    # ------------------------------------------------------------
    plt.plot(x_vals, errs[0], color='red', marker='_')
    plt.plot(x_vals, errs[1], color='blue', marker='s')
    plt.plot(x_vals, errs[2], color='green', marker='^')
    plt.plot(x_vals, errs[3], color='orange', marker='o')
    plt.show()



    # ========================================================
    # PARTE 3.4
    # ========================================================
    # Se repite el experimento utilizando:
    # N = 1000, 2000, 3000, ..., 1000000
    # para observar si aparecen diferencias a una escala mayor.
    # ========================================================

    max_val = 1000000
    min_val = 1000
    step = 1000

    x_vals_large = list(range(min_val, max_val + 1, step))

    theory_large = [sum_theory(n) for n in x_vals_large]

    arrs_large = [
        [func(n) for n in x_vals_large]
        for func in funcs
    ]

    errs_large = [
        list(map(f, zip(a, theory_large)))
        for a in arrs_large
    ]


    # Gráfico del error relativo para valores grandes de N.
    plt.plot(x_vals_large, errs_large[0], color='red', marker='_')
    plt.plot(x_vals_large, errs_large[1], color='blue', marker='s')
    plt.plot(x_vals_large, errs_large[2], color='green', marker='^')
    plt.plot(x_vals_large, errs_large[3], color='orange', marker='o')
    plt.show()



    # ========================================================
    # PARTE 3.5
    # ========================================================
    # Para la suma randomizada, se repite varias veces el cálculo para un 
    # mismo N grande para observar si siempre se obtiene el mismo resultado.
    # ========================================================

    N_random = 1000000

    # Valor teórico para este N
    theory_random = sum_theory(N_random)

    # Se repite la suma randomizada varias veces.
    random_results = [
        sum_shuffle(N_random)
        for _ in range(5)
    ]

    # Se calcula el error relativo de cada ejecución.
    random_errors = [
        abs(result - theory_random) / abs(theory_random)
        for result in random_results
    ]

    # Se muestran los resultados para poder comparar las distintas ejecuciones.
    print("Resultados de la suma randomizada:")
    for i in range(len(random_results)):
        print(
            f"Ejecución {i + 1}: "
            f"resultado = {random_results[i]}, "
            f"error relativo = {random_errors[i]}"
        )

    """
    Resultados de la suma randomizada:
    Ejecución 1: resultado = 0.9999990000010323, error relativo = 3.230752232408207e-14
    Ejecución 2: resultado = 0.9999990000010323, error relativo = 3.230752232408207e-14
    Ejecución 3: resultado = 0.9999990000010323, error relativo = 3.230752232408207e-14
    Ejecución 4: resultado = 0.9999990000010323, error relativo = 3.230752232408207e-14
    Ejecución 5: resultado = 0.9999990000010323, error relativo = 3.230752232408207e-14
    """


if __name__ == '__main__':
    main()

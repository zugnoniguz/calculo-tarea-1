from typing import Callable
from matplotlib import pyplot as plt


# ============================================================
# PARTE 2 - PROPIEDAD ASOCIATIVA
# ============================================================
#
# Se estudian tres formas diferentes de realizar la misma suma matemática:
#
#   (1 + b^k - b^k)
#
#   (1 + b^k) - b^k
#
#   (1 - b^k) + b^k
#
# Matemáticamente, las tres deberían dar el mismo resultado.
# Sin embargo, al utilizar números representados por una
# cantidad finita de bits, pueden aparecer diferencias.
# ============================================================


# Realiza una sumatoria de N términos.
def do_sum(N: int, pred: Callable[[int], int | float]):

    # "pred" es una función que recibe k y devuelve el término que se quiere sumar.
    # Determina si el resultado de pred(1) es entero o float para inicializar correctamente la variable res.
    if isinstance(pred(1), int):
        res=0
    else:
        res=0.0

    # Suma los términos desde k = 1 hasta k = N.
    for k in range(1, N + 1): 
        try:
            v = pred(k)
        except OverflowError:
            continue

        # Se acumula el resultado.
        res += v
    return res

# Primer forma: (1 + b^k) - b^k
def sum1(N: int, b: float | int):
    return do_sum(N, lambda k: 1 + b**k - b**k)

# Segunda forma: (1 + b^k) - b^k
def sum2(N: int, b: float | int):
    return do_sum(N, lambda k: (1 + b**k) - b**k)

# Tercer forma: (1 - b^k) + b^k
def sum3(N: int, b: float | int):
    return do_sum(N, lambda k: (1 - b**k) + b**k)

def main():

    # ========================================================
    # PARTE 2.2
    # ========================================================
    #
    # Se grafica  N = 1, 2, ..., 1000
    # utilizando b ∈ {2, 3, 5, 10}
    # con b de tipo int.
    # ========================================================

    max_val = 1000
    min_val = 1

    x_vals = list(range(min_val, max_val + 1))

    b_values = [2, 3, 5, 10]

    # Se repite el experimento para cada valor de b.
    for b_val in b_values:

        # Cálculo de las tres formas de realizar la suma.
        arr1 = [sum1(n, b_val) for n in x_vals]
        arr2 = [sum2(n, b_val) for n in x_vals]
        arr3 = [sum3(n, b_val) for n in x_vals]

        # Se grafican las tres implementaciones.
        plt.plot(x_vals, arr1, 'r--')
        plt.plot(x_vals, arr2, 'bs')
        plt.plot(x_vals, arr3, 'g^')

        plt.title(f"b = {b_val} (int)")
        plt.xlabel("N")
        plt.ylabel("a_N")

        plt.show()


    
    # ========================================================
    # PARTE 2.3
    # ========================================================
    # Se repite el experimento anterior, pero ahora utilizando:
    # b ∈ {2.0, 3.0, 5.0, 10.0}
    # (valores de tipo float)
    # ========================================================

    b_values_float = [2.0, 3.0, 5.0, 10.0]


    # Se repite el experimento para cada valor de b.
    for b_val in b_values_float:

        # Cálculo de las tres formas de la suma.
        arr1 = [sum1(n, b_val) for n in x_vals]
        arr2 = [sum2(n, b_val) for n in x_vals]
        arr3 = [sum3(n, b_val) for n in x_vals]

        # Se grafican las tres implementaciones.
        plt.plot(x_vals, arr1, 'r--')
        plt.plot(x_vals, arr2, 'bs')
        plt.plot(x_vals, arr3, 'g^')

        plt.title(f"b = {b_val} (float)")
        plt.xlabel("N")
        plt.ylabel("a_N")

        plt.show()



    # ========================================================
    # PARTE 2.5 - BONUS
    # ========================================================
    #
    # Esta parte es conceptual/experimental y plantea:
    #
    # - ¿Qué sucede si b <= 1?
    # - ¿Existen problemas al sumar números enteros grandes?
    # - ¿Qué ocurre utilizando valores negativos de b?
    #
    # No se agrega una implementación específica porque
    # la consigna plantea estas preguntas como investigación
    # y análisis del fenómeno.
    # ========================================================

    # ========================================================
    # PARTE 2.5 - BONUS
    # ========================================================
    # Se investiga:
    # 1. ¿Qué sucede si b <= 1?
    # 2. ¿Existen situaciones donde los valores de b enteros tengan problemas al trabajar con números grandes?
    # 3. ¿Qué sucede si utilizamos valores negativos de b?
    # ========================================================


    # ------------------------------------------------------------
    # BONUS 1 - ¿Qué sucede si b <= 1?
    # ------------------------------------------------------------
    # Se prueban distintos valores:
    # b = 1
    # b = 0
    # b = -1

    print("\n" + "=" * 60)
    print("BONUS 1 - Valores de b <= 1")
    print("=" * 60)

    bonus_b_values = [1, 0, -1]
    bonus_N = 10

    for b_val in bonus_b_values:

        print(f"\nb = {b_val}, N = {bonus_N}")

        result1 = sum1(bonus_N, b_val)
        result2 = sum2(bonus_N, b_val)
        result3 = sum3(bonus_N, b_val)

        print(f"  sum1: {result1}")
        print(f"  sum2: {result2}")
        print(f"  sum3: {result3}")


    # ------------------------------------------------------------
    # BONUS 2 - ¿Qué sucede con números enteros grandes?
    # ------------------------------------------------------------
    # Se prueban valores de b enteros grandes.
    # Se utiliza b = 10 y valores grandes de N. 

    print("\n" + "=" * 60)
    print("BONUS 2 - Números enteros grandes")
    print("=" * 60)

    large_b = 10
    large_N_values = [10, 50, 100, 200, 1000, 10000]

    for N in large_N_values:

        print(f"\nN = {N}, b = {large_b}")

        result1 = sum1(N, large_b)
        result2 = sum2(N, large_b)
        result3 = sum3(N, large_b)

        print(f"  sum1: {result1}")
        print(f"  sum2: {result2}")
        print(f"  sum3: {result3}")


    # ------------------------------------------------------------
    # BONUS 3 - Valores negativos de b
    # ------------------------------------------------------------
    # Se prueban los valores negativos de b:
    # b = -2
    # b = -3
    # b = -5
    # b = -10 

    print("\n" + "=" * 60)
    print("BONUS 3 - Valores negativos de b")
    print("=" * 60)

    negative_b_values = [-2, -3, -5, -10]
    negative_N = 10

    for b_val in negative_b_values:

        print(f"\nb = {b_val}, N = {negative_N}")

        result1 = sum1(negative_N, b_val)
        result2 = sum2(negative_N, b_val)
        result3 = sum3(negative_N, b_val)

        print(f"  sum1: {result1}")
        print(f"  sum2: {result2}")
        print(f"  sum3: {result3}")


    """
    ============================================================
    BONUS 1 - Valores de b <= 1
    ============================================================

    b = 1, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    b = 0, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    b = -1, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    ============================================================
    BONUS 2 - Números enteros grandes
    ============================================================

    N = 10, b = 10
    sum1: 10
    sum2: 10
    sum3: 10

    N = 50, b = 10
    sum1: 50
    sum2: 50
    sum3: 50

    N = 100, b = 10
    sum1: 100
    sum2: 100
    sum3: 100

    N = 200, b = 10
    sum1: 200
    sum2: 200
    sum3: 200

    N = 1000, b = 10
    sum1: 1000
    sum2: 1000
    sum3: 1000

    N = 10000, b = 10
    sum1: 10000
    sum2: 10000
    sum3: 10000

    ============================================================
    BONUS 3 - Valores negativos de b
    ============================================================

    b = -2, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    b = -3, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    b = -5, N = 10
    sum1: 10
    sum2: 10
    sum3: 10

    b = -10, N = 10
    sum1: 10
    sum2: 10
    sum3: 10
    """


if __name__ == '__main__':
    main()

import math


def n_choose_k(n, k):

    if n < k:
        return 0

    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def k_permutation(n, k):
    return math.factorial(n) / (math.factorial(n-k))


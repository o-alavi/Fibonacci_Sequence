# ==============================================
# ================== METHOD 2 ==================
cache = {}


def fib_2(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        return 1
    else:
        val = fib_2(n - 1) + fib_2(n - 2)
        cache[n] = val
        return val


for n in range(1, 35):
    print(n, '  -   ', fib_2(n))

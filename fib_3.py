# ==============================================
# ================== METHOD 3 ==================
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_3(n):
    if n == 1 or n == 2:
        return 1
    else:
        val = fib_3(n - 1) + fib_3(n - 2)
        return val


for n in range(1, 35):
    print(n, '  -   ', fib_3(n))

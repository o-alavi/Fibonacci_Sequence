# ==============================================
# ================== METHOD 1 ==================
import time
t1 = time.time()


def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        val = fib_1(n - 1) + fib_1(n - 2)
        return val


for n in range(1, 35):
    print(n, '  -   ', fib_1(n))

t2 = time.time()
print("Time Consumption (METHOD 2):  ", t2 - t1, 's')

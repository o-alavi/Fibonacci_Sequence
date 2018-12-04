# Fibonacci_Sequence
Three Methods for Calculating Fibonacci Sequence

In this project, my top priority was to show the importance of cache in reducing time consumption by the code.

The first method for finding "Fibonacci Sequence" is the conventional approach (fib_1.py).

The second method includes a simple cache for saving the previous values instead of calculating them again and again (fib_2.py).

The third method includes the same approach but by using "lru_cache" from functiontools module.
You can put "@lru_cache(maxsize=)" just before the defined function.

Good luck!

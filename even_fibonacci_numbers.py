# --------- Even Fibonacci Numbers ---------

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

from sympy import fibonacci
from itertools import count
import time
# because every n divisible by 3s Fib(n) is even
def main():
    start = time.perf_counter()

    even_fibonacci_numbers = (fibonacci(x) for x in count(3,3))
    total = 0
    for i in even_fibonacci_numbers:
        if i < 4_000_000:
            total += i
        else:
            break

    end = time.perf_counter()
    (print(f"Answer: {total}"))
    print(f"Execution time: {end - start:.4f} seconds")

if __name__ == "__main__":
    main()
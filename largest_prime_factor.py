# --------- Larges Prime Factor ---------

# The Prime factors of 13195 are 5,7,13 and 29.
# What is the larges prime factor of the number 600851475143

import time
import math
from sympy import isprime

def main():
    start = time.perf_counter()
    n = 600851475143
    gen = [i for i in range(1, int(math.sqrt(n))) if n % i == 0 and isprime(i)]
    print(f"Answer;{gen[len(gen)-1]}")
    end = time.perf_counter()
    print(f"Execution time: {end - start:.4f} seconds")

if __name__ == "__main__":
    main()